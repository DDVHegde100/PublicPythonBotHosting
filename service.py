import os
import discord
from discord.ext import commands

client=commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print('Initiating Instant Kill...')

client.run(os.getenv('TOKEN'))
