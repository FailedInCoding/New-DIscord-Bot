import discord
from discord import message
import os

client = discord.Client()

TOKEN = 'ODUyMjc0OTMxNDc5MDg1MDg3.YMEc4g.nduPECR3E3U7u4sNIxOfMa9NEfQ'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(Message):
    if message.author == client.user:
        return

    if message.content.startwidth('$Hallo'):
        await message.channel.send('Hassam is gay')

client.run(TOKEN)