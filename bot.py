# imports
import discord
import asyncio
from constants import *
from safety import token

client = discord.Client()


@client.event
async def on_ready():
    ready_operations(client)


@client.event
async def on_message(message):
    if message.content == "!big noob help":
        await client.send_message(message.channel, github)

client.run(token)