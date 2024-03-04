import base64
import requests
import json
from requests.auth import HTTPBasicAuth
import os


# Request URL - API for creating a new page as a child of another page
URL = 'https://novaspikes.atlassian.net/wiki/rest/api/content/'

# Request Headers
HEADERS = {
    'Content-Type': 'application/json;charset=iso-8859-1',
}

def create_confluence_page_if_not_exists(page_title: str, server_name: str):
    # todo: Check if page exists
    
    # Set the title and content of the page to create
    page_html = f'<p>{page_title} is a member of the {server_name} discord server.</p>'

    # Request body
    data = {
        'type': 'page',
        'title': page_title,
        'ancestors': [{'id':os.getenv('CONFLUENCE_PARENT_PAGE_ID')}],
        'space': {'key':os.getenv('CONFLUENCE_SPACE_KEY')},
        'body': {
            'storage':{
                'value': page_html,
                'representation':'storage',
            }
        }
    }

    # We're ready to call the api
    try:
        r = requests.post(url=URL, data=json.dumps(data), headers=HEADERS, auth=(os.getenv('CONFLUENCE_EMAIL'), os.getenv('CONFLUENCE_TOKEN')))

        # Consider any status other than 2xx an error
        if not r.status_code // 100 == 2:
            print("Error: Unexpected response {}, {}".format(r.status_code, r.reason))
        else:
            print(f'Page created for {page_title}')

    except requests.exceptions.RequestException as e:

        # A serious problem happened, like an SSLError or InvalidURL
        print("Error: {}".format(e))