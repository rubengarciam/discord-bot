import discord
import os
from keep_alive import keep_alive

client = discord.Client()
links_channel = client.get_channel(850621499958362125)
my_secret = os.environ['TOKEN']
emoji = '\N{ROBOT FACE}'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    # Do not run in #links
    if message.channel.id != "850621499958362125":
      # If message contains embeds
      if message.embeds:
        # For every embed, if contains an url
        for embed in message.embeds:
          if embed.url:
            await links_channel.send(message.author.name + ' shared ' + embed.url)
            await message.add_reaction(emoji)
          

keep_alive()
client.run(my_secret)