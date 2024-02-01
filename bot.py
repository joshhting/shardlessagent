import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(
    name="cascade",
    description="Cascade into a random joke",
    guild=discord.Object(id=os.getenv('DISCORD_SERVER'))
)
async def slash_command(interaction, arg: str):
    # select joke
    f = open("lines.txt", "r")
    jokes = f.readlines()
    joke = random.choice(jokes).replace('#', arg)

    await interaction.response.send_message(joke)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=os.getenv('DISCORD_SERVER')))
    print("Shardless Agent is ready")

client.run(os.getenv('DISCORD_TOKEN'))