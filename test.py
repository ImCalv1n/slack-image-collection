import requests
import shutil
import os
import json
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
URL=os.getenv('URL')
USER_AGENT=os.getenv('USER_AGENT')
CHANNEL=os.getenv('CHANNEL')

def execute(endpoint_url):
        return requests.get(endpoint_url,
                            headers={'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
                                    'User-Agent': USER_AGENT},
                            params={
                                'channel': CHANNEL,
                            }).json()

def grab_file(endpoint_url):
    #file = endpoint_url.split('/')[6]

    #file_name = 'files/' + file
    file_name = 'files/image.jpg'

    print(file_name)
    print(endpoint_url)

    response = requests.get(endpoint_url,
                            headers={'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
                                    'User-Agent': USER_AGENT}
                            )
    
    print(response.headers.get("content-type"))

    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
    
    else:
        print("could not download file " + file_name)


if __name__ == '__main__':

    messages = execute(URL)
    json_str = json.dumps(messages, indent=4)
    file = 'out/test_collection.json'

    with open(file, 'w') as out_file:
        out_file.write(json_str)
    
    #test_url = 'https://media.geeksforgeeks.org/wp-content/uploads/20210224040124/JSBinCollaborativeJavaScriptDebugging6-300x160.png'
    #grab_file(test_url)
    grab_file(messages["messages"][1]["files"][0]["permalink_public"])
