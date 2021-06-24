import discord
from discord.ext import tasks, commands
from datetime import datetime


TOKEN = 'ODUyMjc0OTMxNDc5MDg1MDg3.YMEc4g.nduPECR3E3U7u4sNIxOfMa9NEfQ'

client = discord.Client()

@tasks.loop(minutes=1)
async def test():
    channel = client.get_channel(827659439330426884)
    await channel.send("test")

@client.event
async def on_ready():
    test.start()

client.run(TOKEN)