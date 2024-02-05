from cascade import cascade
import discord
import os
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
    if interaction.user.bot:
        return
    print(interaction.user.display_name, arg)

    cascade(arg)
    await interaction.response.send_message(joke)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=os.getenv('DISCORD_SERVER')))
    print("Shardless Agent is ready")

client.run(os.getenv('DISCORD_TOKEN'))