

import requests
from dotenv import load_dotenv
import os


def fetch_bucket_list():
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': api_key })
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Error:", response.status_code, response.text

# if __name__ == "__main__":
#     print(fetch_bucket_list())