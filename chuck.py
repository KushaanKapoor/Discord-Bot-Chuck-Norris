import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import urllib.request, json

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

jokes = open("jokes.txt").readlines()


@client.event
async def on_ready():
     print("Chuck Norris has arrived!")
@client.event
async def on_message(message):
    message.content = message.content.casefold()
    userID = message.author.id
    botID = 447399994924859393
    dialogue = ["I am gonna roundhouse kick you <@%s>" % (userID), "You are a foool! <@%s>" % (userID), "How did you **DARE** to wake me up from my week long nap!? <@%s>" % (userID), "Why dont you take a long rope and hang yourself with it instead of typing such bullshit. <@%s>" % (userID), "Think thrice before you try to talk to me <@%s>. Youre just a mere human." % (userID), "IS THAT ALL YOU GOT!? <@%s>" % (userID), "Did you say something? <@%s>" % (userID)]
    if message.author.id!='447399994924859393':
        if "<@%s>" % (447399994924859393) in message.content:
                await client.send_message(message.channel, "No one can mention Chuck Norris! not even Chuck Norris himself!")
        if "chuck" in message.content:
            if "chuck" and "bored" in message.content:
                await client.send_message(message.channel, "So am I, <@%s> , So am I" % (userID))
            elif "chuck" and "joke" in message.content:
                await client.send_message(message.channel, random.choice(jokes))
            else:
                await client.send_message(message.channel, random.choice(dialogue))


        
client.run("NDQ3Mzk5OTk0OTI0ODU5Mzkz.DeHOfA.sjf6e6OvCFOL93TSFinAZW8EDBA")
