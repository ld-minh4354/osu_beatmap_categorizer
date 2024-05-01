import discord
import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR

# some inits
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# to note that we have logged in the server
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# main program
if __name__ == '__main__':
    # get token
    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'raw', 'token.txt'), 'r')
    token = f.read()
    f.close()

    # run bot
    client.run(token)
