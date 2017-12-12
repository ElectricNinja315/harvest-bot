# imports
import discord
import asyncio
from constants import *
from safety import token

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content == "!big noob help":
        await client.send_message(message.channel, "See my GitHub for more information on my commands.")
        await client.send_message(message.channel, "https://github.com/ElectricNinja315/harvest-bot")

client.run(token)