import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
TEST_URL=os.getenv('TEST_URL')
USER_AGENT=os.getenv('USER_AGENT')
test=os.getenv('test')

def execute(endpoint_url):
        return requests.get(endpoint_url,
                            headers={'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
                                    'User-Agent': USER_AGENT},).json()

if __name__ == '__main__':
    
    collection = execute(TEST_URL)
    json_str = json.dumps(collection, indent=4)
    file = 'out/test_collection.json'

    with open(file, 'w') as out_file:
        out_file.write(json_str)
