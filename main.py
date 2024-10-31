from request_puuid import get_puuid
def main():
    PUUID = get_puuid() # Get PUUID from username

    print("PUUID= ",PUUID)
    return 0

if __name__ == '__main__':
    main()