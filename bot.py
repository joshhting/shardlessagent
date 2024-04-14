from cascade import cascade
import confluence
import discord
import os
import time
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
    # await tree.sync(guild=discord.Object(id=os.getenv('DISCORD_SERVER')))
    print("Shardless Agent is ready")
    # server = list(filter(lambda x: x.id == os.getenv('DISCORD_SERVER'), client.guilds))[0]
    server = client.get_guild(int(os.getenv('DISCORD_SERVER')))
    for member in server.members:
        confluence.create_confluence_page_if_not_exists(str(member), server.name)
        time.sleep(3)

client.run(os.getenv('DISCORD_TOKEN'))