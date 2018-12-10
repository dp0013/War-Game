import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio 
import os
#from keep_alive import keep_alive

#establish Discord client:
client = discord.Client()

#provide action upon initition of a chat; specifically, notify the user that the bot is online with the message "I'm in" followed by identifying itself with its ReplBot ID:
@client.event
async def on_ready():
  print("This is", client.user)
  print("I'm in")

#tell bot how to handle new messages:
@client.event
async def on_message(message):
    #only respond to messages that aren't from us:
    if message.author != client.user:
      #send a new message to the same channel where we received a message:
      await client.send_message(message.channel, message.content[::-1])


#start web server before the bot:
#keep_alive()
#pulls secret Discord token from the '.env':
#token = os.environ.get("DISCORD_BOT_SECRET")
#client.run(token)

# DELETE THIS TOKEN AND USE THE ABOVE "token" VARIABLE POINTING TO THE
#DISCORD_BOT_SECRET BEFORE POSTING TO REPL!!!
client.run(NTE0NDQxMzk5NTg0OTQ4MjU2.DtWm9A.q6aAl1LqYlmbf5WOfVsPe7hr1xs)
