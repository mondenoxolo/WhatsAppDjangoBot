#Ninja
import requests
from dotenv import load_dotenv
import os

def fetch_random_quote(category):
    # category = input('Category: ')
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': api_key })
    
    if response.status_code == requests.codes.ok:
        if response.json() == []:
            return f"Category not available"
        else: 
            quote = response.json()
        
            return quote
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    category = input("Category: ")
    print(fetch_random_quote(category))

