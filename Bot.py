import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODA1MTIzMzk0NjAwNjk3OTI4.YBWTlw.1CVBMhcbeOK7yj8ExBqtx-8Ls-8')