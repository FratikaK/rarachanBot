import discord
from config import Config

client = discord.Client()


@client.event
async def on_ready():
    print("rarachan Bot Start!")


token = Config().get_string("Token")
if token is None:
    print("Token nodes None.")
else:
    client.run(token)
