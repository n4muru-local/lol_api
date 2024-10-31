from request_puuid import get_puuid
from request_matchid import get_matchid
def main():
    PUUID = get_puuid() # Get PUUID from username
    print("PUUID= ",PUUID)

    print(get_matchid(PUUID))
    return 0

if __name__ == '__main__':
    main()