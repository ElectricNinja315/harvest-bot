# imports
import discord
from bot.constants import *
from bot.safety import token

client = discord.Client()   # initialize client object


@client.event
async def on_ready():
    ready_operations(client)


@client.event
async def on_message(message):
    # help function
    if message.content == "!big noob help":
        await client.send_message(message.channel, github)

    # meme functions
    elif message.content == "!meme music":
        await client.send_message(message.channel, "!music " + meme_music)

    elif message.content.startswith("!copy"):
        to_copy = message.content[6:]   # text to copy
        name = message.author.id  # username

        fo = open(r'userstexts/%s.txt' % name, "w")  # init file object
        fo.write(to_copy)   # write text to copy to document
        fo.close()  # close file object

        await client.send_message(message.channel, "Your message has been saved.")

    elif message.content == "!paste":
        name = message.author.id
        fo = open(r'userstexts/%s.txt' % name, "r")  # init file object
        await client.send_message(message.channel, fo.read())   # send the user's text

client.run(token)
