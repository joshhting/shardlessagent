import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('DISCORD_TOKEN')
APP_ID = os.getenv('SA_APP_ID')
SERVER_ID = os.getenv('DISCORD_SERVER')  # Only needed for guild commands

# For global commands
url = f"https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    commands = response.json()
    for cmd in commands:
        print(f"Name: {cmd['name']}, ID: {cmd['id']}")
else:
    print(f"Failed to fetch commands: {response.status_code} - {response.text}")
