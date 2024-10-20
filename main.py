import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


import os
from dotenv import load_dotenv
from assets.help import *
from assets.game_embed import *
from assets.fight import *
from assets.object.spawn import *

load_dotenv()


DISCORD_TOKEN = os.getenv("BOT_TOKEN")

tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    synced_commands = await tree.sync()
    print(f'{client.user} Connected | {len(synced_commands)} commands.')

@tree.command(name="start", description="Start the game")
async def start(interaction: discord.Interaction):
    user_allow = interaction.user
    created_channel = await interaction.guild.create_text_channel(interaction.user.name + " game")
    category_game = discord.utils.get(interaction.guild.categories, name='Game')
    if category_game is None:
        category_game = await interaction.guild.create_category('Game')
    await created_channel.edit(category=category_game)

    channel_permissions = created_channel.overwrites_for(interaction.guild.default_role)
    channel_permissions.send_messages = False
    channel_permissions.read_messages = False
    channel_permissions.read_message_history = False

    await created_channel.set_permissions(interaction.guild.default_role, overwrite=channel_permissions)

    channel_permissions = created_channel.overwrites_for(user_allow)
    channel_permissions.send_messages = True
    channel_permissions.read_messages = True
    channel_permissions.read_message_history = True
    await created_channel.set_permissions(user_allow, overwrite=channel_permissions)

    await interaction.response.send_message(f'Votre jeu commence sur ce channel : <#{created_channel.id}>', ephemeral=True)

    starting_embed = discord.Embed(
        title="Game starting", 
        color=0x055a28)
    starting_embed.set_image(url="https://c.tenor.com/LcT6NDXYBisAAAAC/tenor.gif")

    options = [
        discord.SelectOption(label="Commencer une partie", value="option_1", description="Commencer une nouvelle partie", emoji="🆕"),
        discord.SelectOption(label="Continuer une partie", value="option_2", description="Reprendre une partie depuis une sauvegarde", emoji="⏩"),
        discord.SelectOption(label="Aide", value="option_3", description="Besoin d'aide ?", emoji="❓"),
        discord.SelectOption(label="Quitter", value="option_4", description="Quitter le jeu", emoji="🚪"),
    ]

    select = discord.ui.Select(
        placeholder="Sélectionner votre choix...",
        options=options
    )

    async def select_callback(interaction: discord.Interaction):
        choice = select.values[0] 
        if choice == "option_1":
            await interaction.response.defer(ephemeral=True)
            await startgame(user_allow, created_channel)
        elif choice == "option_2":
            await interaction.response.send_message("Vous avez choisi de continuer une partie !", ephemeral=True)
        elif choice == "option_3":
            await interaction.user.send(help_embed)
            await interaction.response.defer(ephemeral=True)
        elif choice == "option_4":
            await interaction.channel.delete()
            category_game = discord.utils.get(interaction.guild.categories, name='Game')
            if category_game is not None:
                if len(category_game.channels) == 0:
                    await category_game.delete()

    select.callback = select_callback

    view = discord.ui.View()
    view.add_item(select)

    await created_channel.send(embed=starting_embed,view=view)



async def startgame(user, channel):
    await channel.send(embed=Embeds["spawn"])
    
    def check(m):
        return m.author == user and m.content.lower() == 'suivant' or m.content.lower() == 's'

    msg = await client.wait_for('message', check=check)
    await channel.send(embed=Embeds["1"])

    msg = await client.wait_for('message', check=check)
    await channel.send(embed=Embeds["2"])

    msg = await client.wait_for('message', check=check)
    await channel.send(embed=Embeds["3"])

    msg = await client.wait_for('message', check=check)
    await channel.send(embed=Embeds["4"])

    msg = await client.wait_for('message', check=check)
    await channel.send(embed=Embeds["starting_fight"])

    msg = await client.wait_for('message', check=check)

    fight_embed = create_fight_embed(spawn_mob)
    await channel.send(embed=fight_embed)






@tree.command(name="help", description="Recevoir de l'aide")
async def help(interaction: discord.Interaction):
    await interaction.user.send(help_embed)
    await interaction.response.send_message('Vous allez recevoir un message privé d\'ici peu !', ephemeral=True)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$end'):
        if message.channel.category.name == 'Game':
            await message.channel.delete()
            category_game = discord.utils.get(message.guild.categories, name='Game')
            if category_game is not None:
                if len(category_game.channels) == 0:
                    await category_game.delete()



client.run(DISCORD_TOKEN)


