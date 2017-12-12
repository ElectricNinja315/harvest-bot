# imports
import discord
from bot.constants import *
from bot.safety import token

client = discord.Client()


@client.event
async def on_ready():
    ready_operations(client)


@client.event
async def on_message(message):
    if message.content == "!big noob help":
        await client.send_message(message.channel, github)
    elif message.content == "!meme music":
        await client.send_message(message.channel, "!music " + meme_music)

client.run(token)