import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

DISCORD_TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} Connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        user_allow = message.author
        created_channel = await message.guild.create_text_channel(message.author.name+" game")
        category_game = discord.utils.get(message.guild.categories, name='Game')
        if category_game is None:
            category_game = await message.guild.create_category('Game')
        await created_channel.edit(category=category_game)



        channel_permissions = created_channel.overwrites_for(message.guild.default_role)
        channel_permissions.send_messages = False
        channel_permissions.read_messages = False
        channel_permissions.read_message_history = False

        await created_channel.set_permissions(message.guild.default_role, overwrite=channel_permissions)

        channel_permissions = created_channel.overwrites_for(user_allow)
        channel_permissions.send_messages = True
        channel_permissions.read_messages = True
        channel_permissions.read_message_history = True
        await created_channel.set_permissions(user_allow, overwrite=channel_permissions)

        await created_channel.send('Welcome to the game!')

    if message.content.startswith('$end'):
        await message.channel.delete()
        category_game = discord.utils.get(message.guild.categories, name='Game')
        if category_game is not None:
            if len(category_game.channels) == 0:
                await category_game.delete()




client.run(DISCORD_TOKEN)
