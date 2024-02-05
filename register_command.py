import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = "1202429232068952145"
SERVER_ID = "940407143696314400"
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

# global commands are cached and only update every hour
# url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

# while server commands update instantly
# they're much better for testing
url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands'

json = [
  {
    'name': 'cascade',
    'description': 'Cascade into a random joke',
    'options': [
        {
            "name": "arg",
            "description": "Subject matter",
            "type": 3,
            "required": True
        }
    ]
  }
]

response = requests.put(url, headers={
  'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())