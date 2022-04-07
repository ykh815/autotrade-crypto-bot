#-*-coding:utf-8 -*-
import myUpbit   #우리가 만든 함수들이 들어있는 모듈
import json
import time
import pyupbit



time.sleep(10.0)

top_file_path = "/home/ykh815/autotrade-crypto-bot/UpbitTopCoinList.json"

#거래대금이 많은 탑코인 30개의 리스트
TopCoinList = myUpbit.GetTopCoinList("day",30)

#파일에 리스트를 저장합니다
with open(top_file_path, 'w') as outfile:
    json.dump(TopCoinList, outfile)


