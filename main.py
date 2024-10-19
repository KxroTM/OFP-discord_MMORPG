import discord
import os
from dotenv import load_dotenv
from assets.help import help_embed
from assets.game_embed import Embeds, Options

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

DISCORD_TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client(intents=intents)
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
            await startgame(user_allow, created_channel)
            await interaction.response.defer(ephemeral=True)
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



@tree.command(name="help", description="Recevoir de l'aide")
async def help(interaction: discord.Interaction):
    await interaction.user.send(help_embed)
    await interaction.response.send_message('Vous allez recevoir un message privé d\'ici peu !', ephemeral=True)


async def startgame(user, channel): 
    await channel.purge()
    button = Options["spawn"]
    view = discord.ui.View()
    view.add_item(button[0])
    await channel.send(embed=Embeds["spawn"], view=view)

    async def game_callback(interaction: discord.Interaction):
        button = Options["1"]
        view = discord.ui.View()
        view.add_item(button[0])
        await interaction.response.send_message(embed=Embeds["1"], view=view)

        async def game_callback(interaction: discord.Interaction):
            button = Options["2"]
            view = discord.ui.View()
            view.add_item(button[0])
            await interaction.response.send_message(embed=Embeds["2"], view=view)

            async def game_callback(interaction: discord.Interaction):
                button = Options["3"]
                view = discord.ui.View()
                view.add_item(button[0])
                await interaction.response.send_message(embed=Embeds["3"], view=view)

                async def game_callback(interaction: discord.Interaction):
                    button = Options["4"]
                    view = discord.ui.View()
                    view.add_item(button[0])
                    await interaction.response.send_message(embed=Embeds["4"], view=view)

                    async def game_callback(interaction: discord.Interaction):
                        button = Options["starting_fight"]
                        view = discord.ui.View()
                        view.add_item(button[0])
                        await interaction.response.send_message(embed=Embeds["starting_fight"], view=view)

                    button[0].callback = game_callback
                button[0].callback = game_callback     
            button[0].callback = game_callback
        button[0].callback = game_callback
    button[0].callback = game_callback







    


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


