from dotenv import load_dotenv
import os
import requests
from datetime import datetime

def get_matchid(_PUUID, ):
    USER_NAME = os.getenv("YOUR_USER_NAME")
    USER_TAG  = os.getenv("YOUR_USER_TAG")
    REGION    = os.getenv("YOUR_REGION")
    API_KEY   = os.getenv("YOUR_API_KEY")
    PUUID = _PUUID
    start_time_string =  "2021-06-16 00:00:00"  # First match time to list output (minimum = 2021-06-16 00:00:00)
    dt = datetime.today() 
    end_time_string = f"{dt.year}-{dt.month}-{dt.day} 00:00:00"     # Time specification of endpoints (Maximum = today)
    INQUEUE_TYPE = "normal"
    START_INDEX = 0
    COUNT = 10

    START = int(datetime.strptime(start_time_string, "%Y-%m-%d %H:%M:%S").timestamp())
    END = int(datetime.strptime(end_time_string, "%Y-%m-%d %H:%M:%S").timestamp())

    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?startTime={START}&endTime={END}&type={INQUEUE_TYPE}&start={START_INDEX}&count={COUNT}&api_key={API_KEY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
