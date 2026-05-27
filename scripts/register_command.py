import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = "1202429232068952145"
FOF_APP_ID = "1229179810425868300"
SERVER_ID = os.getenv('DISCORD_SERVER')
# SERVER_ID = os.getenv('TEST_SERVER')
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
  },
  {
    'name': 'replicate',
    'description': 'Resets the counter'
  },
  # {
  #   'name': 'trolleyproblem',
  #   'description': 'Generate a trolley problem',
    # 'options': [
    #     {
    #         'name': 'meme',
    #         'description': '"Enabled" to allow for meme options',
    #         'type': 3,
    #         'required': True
    #     }
    # ]
  # },
  {
    'name': 'list_lottery_entries',
    'description': 'Lists lottery entries'
  },
  {
    'name': 'draw_lottery',
    'description': 'Randomly choose a lottery entry'
  },
  {
    'name': 'plus_1_lottery',
    'description': 'Adds someone to the lottery',
    'options': [
        {
            "name": "arg",
            "description": "Person to be added",
            "type": 3,
            "required": True
        }
    ]
  },
  {
    'name': 'minus_1_lottery',
    'description': 'Removes someone from the lottery',
    'options': [
        {
            "name": "arg",
            "description": "Person to be removed",
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