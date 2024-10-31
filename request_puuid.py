from dotenv import load_dotenv
import os
import requests

load_dotenv()
def get_puuid():
    USER_NAME = os.getenv("YOUR_USER_NAME")
    USER_TAG  = os.getenv("YOUR_USER_TAG")
    REGION    = os.getenv("YOUR_REGION")
    API_KEY   = os.getenv("YOUR_API_KEY")
    url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{USER_NAME}/{USER_TAG}?api_key={API_KEY}"
    
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('puuid')
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None