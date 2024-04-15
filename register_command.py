import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = "1202429232068952145"
FOF_APP_ID = "1229179810425868300"
SERVER_ID = "940407143696314400"
BOT_TOKEN = os.getenv('FOF_TOKEN')

# global commands are cached and only update every hour
# url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

# while server commands update instantly
# they're much better for testing
url = f'https://discord.com/api/v10/applications/{FOF_APP_ID}/guilds/{SERVER_ID}/commands'

json = [
  # {
  #   'name': 'cascade',
  #   'description': 'Cascade into a random joke',
  #   'options': [
  #       {
  #           "name": "arg",
  #           "description": "Subject matter",
  #           "type": 3,
  #           "required": True
  #       }
  #   ]
  # },
  {
    'name': 'trolleyproblem',
    'description': 'Generate a trolley problem',
    # 'options': [
    #     {
    #         'name': 'meme',
    #         'description': '"Enabled" to allow for meme options',
    #         'type': 3,
    #         'required': True
    #     }
    # ]
  }
]

response = requests.put(url, headers={
  'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())