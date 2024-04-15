from db import update_stats
from trolley import TrolleyProblem
import confluence
import discord
import os
import time
from dotenv import load_dotenv

load_dotenv()

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# tree = discord.app_commands.CommandTree(client)
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__(self, track1, track2, user):
        super().__init__()
        self.track1 = track1
        self.track2 = track2
        self.user = user

    @discord.ui.button(label="Pull the lever", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        if self.user == interaction.user:
            self.disable_all_items()
            print(update_stats(self.track1, self.track2))
            button.label = "You pulled the lever!"
        await interaction.response.edit_message(view=self) # Send a message when the button is clicked

    @discord.ui.button(label="Don't pull the lever", style=discord.ButtonStyle.primary, emoji="❌") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback2(self, button, interaction):
        if self.user == interaction.user:
            self.disable_all_items()
            print(update_stats(self.track2, self.track1))
            button.label = "You didn't pull the lever."
        await interaction.response.edit_message(view=self) # Send a message when the button is clicked

@bot.slash_command()
async def trolleyproblem(ctx):
    tp = TrolleyProblem()
    prompt = tp.generateProblem(True)
    discord_view = MyView(tp.track1, tp.track2, ctx.user)

    await ctx.respond(prompt, view=discord_view)

bot.run(os.getenv('FOF_TOKEN'))