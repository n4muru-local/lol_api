from request_puuid import get_puuid
from request_matchid import get_matchid
from request_matchtimeline import get_match_timeline



import matplotlib.pyplot as plt
def main():
    PUUID = get_puuid() # Get PUUID from username
    print("PUUID= ",PUUID)
    MATCH_ID = get_matchid(PUUID)[0]
    print("MATCH_ID= ",MATCH_ID)

    df = get_match_timeline(MATCH_ID,PUUID)
    # プロットのサイズを設定
    plt.figure(figsize=(14, 8))

        # 各カラムを折れ線グラフとしてプロット
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)

    # ラベルや凡例を設定
    plt.xlabel("Frame Index")
    plt.ylabel("Value")
    plt.title("Champion Stats Time Series")
    plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1))  # 凡例を外に配置

    # グラフを表示
    plt.show()

    return 0

if __name__ == '__main__':
    main()