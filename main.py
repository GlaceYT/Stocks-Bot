import discord
from discord.ext import commands
import os

# Intents setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Prefix for the bot commands
bot = commands.Bot(command_prefix='!', intents=intents)

# Load commands from the commands folder
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and not filename.startswith('__'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')  # Await the extension loading
                print(f'Loaded extension: {filename[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {filename[:-3]}: {e}')
bot.run('MTI1MjE1OTYwMTg5MDE2NDc4Mg.Gn5BJx.vwSFpiSvzJE_Wg6XhnaSvb_2XPWBh7lgzkzT-0')
