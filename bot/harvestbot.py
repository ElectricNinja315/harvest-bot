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
        name = message.author.id  # id

        fo = open(r'userstexts/%s.txt' % name, "w")  # init file object
        fo.write(to_copy)   # write text to copy to document
        fo.close()  # close file object

        await client.send_message(message.channel, "Your message has been saved.")

    elif message.content == "!paste":
        name = message.author.id
        try:    # if the user has already copied something
            fo = open(r'userstexts/%s.txt' % name, "r")  # init file object
            await client.send_message(message.channel, fo.read())   # send the user's text
            fo.close()
        except FileNotFoundError:   # if nothing is copied
            await client.send_message(message.channel, "You do not currently have anything copied.")

client.run(token)
