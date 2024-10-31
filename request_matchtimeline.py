from dotenv import load_dotenv
import pandas as pd

import os
import requests

load_dotenv()
def get_match_timeline(_matchID,_PUUID):
    PUUID = _PUUID
    MATCHID = _matchID
    REGION    = os.getenv("YOUR_REGION")
    API_KEY   = os.getenv("YOUR_API_KEY")


    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{MATCHID}/timeline?api_key={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return 0
    
    # PUUIDからparticipantIdを取得
    participants = json_data['metadata']['participants']
    my_participant_id = str(participants.index(PUUID) + 1)  # 配列のインデックスに+1してparticipantIdに


    # 自分のデータのみを格納するリスト
    my_data = []
    for frame in json_data['info']['frames']:
        participant_data = frame['participantFrames'].get(my_participant_id)
        if participant_data:
            my_data.append(participant_data['championStats'])

    # データフレームに変換して表示
    df = pd.DataFrame(my_data)
    return df