import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('FOF_TOKEN')
FOF_APP_ID = "1229179810425868300"
SERVER_ID = "940407143696314400"  # Only needed for guild commands

command_id = "1311777100276957288"
url = f"https://discord.com/api/v10/applications/{FOF_APP_ID}/guilds/{SERVER_ID}/commands/{command_id}"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:  # 204 means success (No Content)
    print(f"Command {command_id} deleted successfully.")
else:
    print(f"Failed to delete command: {response.status_code} - {response.text}")

