#-*-coding:utf-8 -*-
import myUpbit   #우리가 만든 함수들이 들어있는 모듈
import time
import datetime
import pyupbit

import ende_key  #암복호화키
import my_key    #업비트 시크릿 액세스키

# import line_alert #라인 메세지를 보내기 위함!
import json

'''
단타를 위해 5분마다 돌지만
사실 이는 조절하셔도 됩니다. 
15분봉을 보고 15분마다 돌리셔도 되겠지요 ^^

'''

#암복호화 클래스 객체를 미리 생성한 키를 받아 생성한다.
simpleEnDecrypt = myUpbit.SimpleEnDecrypt(ende_key.ende_key)

#암호화된 액세스키와 시크릿키를 읽어 복호화 한다.
Upbit_AccessKey = simpleEnDecrypt.decrypt(my_key.upbit_access)
Upbit_ScretKey = simpleEnDecrypt.decrypt(my_key.upbit_secret)

#업비트 객체를 만든다
upbit = pyupbit.Upbit(Upbit_AccessKey, Upbit_ScretKey)

#비트코인 25%
#이더리움 15%
#알트코인 베스트 장기 보유 15% 
#알트코인 단타 16%  -> A타입(8%) : 상승장에서만 매수, B타입(8%) : 하락장일때도 매수 (언제나 매수)
#변동성 14%
#현금 15%



#--비트코인 25%---------------------------------------------------------------------------------------------------------------#
BTC_Portion = 0.25 #비트코인 비중 25%
BTC_Ticker = "KRW-BTC"
#----------------------------------------------------------------------------------------------------------------------#


#-이더리움 15%----------------------------------------------------------------------------------------------------------#
ETH_Portion = 0.15 #이더리움 비중 15%
ETH_Ticker = "KRW-ETH"
#----------------------------------------------------------------------------------------------------------------------#



#--알트코인 베스트 장기 보유 15% ------------------------------------------------------------------------------------------------------#
Best_Alt_Portion = 0.15 #비중조절로 계속 가지고갈 베스트 알트코인 비중 총 15%

#계속 비중을 나눠서 비트와 이더처럼 가지고갈 베스트 알트 코인들 
BestCoinList = ['KRW-ADA','KRW-DOT','KRW-AVAX','KRW-SOL','KRW-MATIC','KRW-ALGO','KRW-MANA','KRW-LINK','KRW-BAT','KRW-ATOM']

#베스트 알트코인에 해당되는 비중에서 위 베스트 코인 개수를 나누면 각 코인별 할당 비중이 나온다!
Each_BestCoin_Portion = Best_Alt_Portion / float(len(BestCoinList))

print("Each_BestCoin_Portion : ", Each_BestCoin_Portion)
#----------------------------------------------------------------------------------------------------------------------#25





#--알트코인 단타 16%----------------------------------------------------------------------------------------------------------#
#ALT_Portion = 0.16 #알트는 16% 비중인데 A타입과 B타입 각각 8%로 나눔
# A타입(8%) : 상승장에서만 매수, B타입(8%) : 하락장일때도 매수 (언제나 매수)
#상승장 기준 일봉 기준 5일 이동평균선이 증가추세이면서 현재가가 이평선위에 있을때!!

ALT_Atype_Portion = 0.08 #A타입 비중 8%
ALT_Btype_Portion = 0.08 #B타입 비중 8%
#----------------------------------------------------------------------------------------------------------------------#





#-- 변동성 돌파 14%----------------------------------------------------------------------------------------------------------#
DolPa_Coin = 0.14 #변동성 돌파(매매 횟수가 적고 하루안에 바로 현금화 되므로 사실상 현금) 14%

MaxDolPaCoinCnt = 5.0 #최대 변동성돌파 코인 매수 개수

#변동성 돌파할 코인 비중 
Each_DolPa_Portion = DolPa_Coin / MaxDolPaCoinCnt

DolPaCoinList = list() #변동성 돌파 코인 리스트

#파일에 저장된 경우 읽어 온다
dolpha_type_file_path = "./DolPaCoin.json"
try:
    with open(dolpha_type_file_path, "r") as json_file:
        DolPaCoinList = json.load(json_file)

except Exception as e:
    print("Exception:", e)



#시간 정보를 가져옵니다. 봇이 15분마다 돌다가 아침 9시 즉 hour변수가 0이 된다면 매도합니다.
time_info = time.gmtime()
hour = time_info.tm_hour
min = time_info.tm_min
print(hour,min)



#----------------------------------------------------------------------------------------------------------------------#



#--현금 15%----------------------------------------------------------------------------------------------------------#
Cash_Portion = 0.15 #현금 비중 15%
#----------------------------------------------------------------------------------------------------------------------#






#----------------------------------------------------------------------------------------------------------------------#
ALT_Atype_MaxCnt = 2.0 #A타입 알트코인의 매수 개수 최대치!
ALT_Atype_Greed_Gap = 0.2 #A타입 그리드(거미줄)간 간격 0.2면 0.2%마다 매수 주문을 깔아놓는다는이야기!
ALT_Atype_First_Buy_Rate = 0.2 #A타입 첫 매수시 들어갈 금액 비중

AltAtypeList = list() #A타입 알트 코인들 리스트

#파일에 저장된 경우 읽어 온다
atype_file_path = "./AltATypeCoin.json"
try:
    with open(atype_file_path, "r") as json_file:
        AltAtypeList = json.load(json_file)

except Exception as e:
    print("Exception:", e)
#----------------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------------#
ALT_Btype_MaxCnt = 3.0 #B타입 알트코인의 매수 개수 최대치!
ALT_Btype_Greed_Gap = 0.4 #B타입 그리드(거미줄)간 간격 0.4면 0.4%마다 매수 주문을 깔아놓는다는이야기!
ALT_Btype_First_Buy_Rate = 0.1 #B타입 첫 매수시 들어갈 금액 비중


AltBtypeList = list() #B타입 알트 코인들 리스트

#파일에 저장된 경우 읽어 온다
btype_file_path = "./AltBTypeCoin.json"
try:
    with open(btype_file_path, "r") as json_file:
        AltBtypeList = json.load(json_file)

except Exception as e:
    print("Exception:", e)
#----------------------------------------------------------------------------------------------------------------------#



#원화 마켓에 상장된 모든 코인들을 가져온다.
Tickers = pyupbit.get_tickers("KRW")



MinimunCash = 5000.0 #업비트 최소 매수매도 금액!
#MinimunGap =  0.03 #목표비중에서 3%비중이 차이가 나야 조절!

Target_Revenue_Rate = 1.1 #단타 목표 수익율 1.1%


#내가 가진 잔고 데이터를 다 가져온다.
balances = upbit.get_balances()

TotalMoney = myUpbit.GetTotalMoney(balances) #총 원금
TotalRealMoney = myUpbit.GetTotalRealMoney(balances) #총 평가금액
#내 총 수익율
TotalRevenue = (TotalRealMoney - TotalMoney) * 100.0/ TotalMoney

print("-----------------------------------------------")
print ("Total Money:", myUpbit.GetTotalMoney(balances))
print ("Total Real Money:", myUpbit.GetTotalRealMoney(balances))
print ("Total Revenue", TotalRevenue)
print("-----------------------------------------------")

curr = datetime.datetime.now()
Sdate = curr.strftime("%Y-%m-%d")
Syear = curr.strftime("%Y")
Smon = curr.strftime("%m")
Shour = curr.strftime("%H")
Smin = curr.strftime("%M")

try:
    start_flag = (Shour == "09" and Smin == "00")
    if start_flag:  #매일 개장시(0900) 금액/수익율 기록
        if not (os.path.isdir(LOG_DIR)):
            os.makedirs(os.path.join(LOG_DIR))
        if not (os.path.isdir("{}/{}".format(LOG_DIR, Syear))):
            os.makedirs(os.path.join("{}/{}".format(LOG_DIR, Syear)))
        with open(LOG_FILE.format(LOG_DIR, Syear, Smon), "a") as log:
            log.write("{} | 원금: {}, 평가금: {}, 수익율: {}\n".format(Sdate, TotalMoeny, TotalRealMoney, TotalRevenue))
except Exception as e:
    print("Logging error")
#----------------------------------------------------------------------------------------------------------------------#
#A타입의 알트코인별 최대 매수 금액(할당 금액) = (총평가금액 * 할당비중(20%) / 최대코인개수)
ALT_Atype_CoinMaxMoney = ((TotalRealMoney * ALT_Atype_Portion) / ALT_Atype_MaxCnt)

#A타입의 알트코인의 첫 매수 금액 = 최대 매수 금액(할당 금액) * 첫매수비중
ALT_Atype_FirstEnterMoney = ALT_Atype_CoinMaxMoney * ALT_Atype_First_Buy_Rate

#절반팔고 절반은 나중에 파려면 업비트 최소 주문금액 5천원의 2배인 1만원은 첫 매수에 들어가야 하는데 2.5를 곱해서 12500원 정도의 최소치를 정해논다
if ALT_Atype_FirstEnterMoney < MinimunCash * 2.5:
    ALT_Atype_FirstEnterMoney = MinimunCash * 2.5

#A타입의 알트코인의 총 물타기 금액 = 최대 매수 금액(할당 금액) * (1.0 - 첫매수비중)
ALT_Atype_TotalWaterMoney = ALT_Atype_CoinMaxMoney * (1.0 - ALT_Atype_First_Buy_Rate)

#A타입의 총 거미줄 매수할 시작 금액! (총물타기 금액 / 최소주문금액 5000 * 1.5(보정))
ALT_Atype_Greed_Money = (MinimunCash * 1.5)

#정률로(모든 그리드가 다 같은 금액 매수한다는 가정) 실제로 가능한 최대 거미줄 개수 
ALT_Atype_Maximun_Greed_Cnt = ALT_Atype_TotalWaterMoney / ALT_Atype_Greed_Money




print ("->ALT_Atype_CoinMaxMoney:", ALT_Atype_CoinMaxMoney)
print ("->ALT_Atype_FirstEnterMoney", ALT_Atype_FirstEnterMoney)
print ("->ALT_Atype_TotalWaterMoney", ALT_Atype_TotalWaterMoney)
print ("->ALT_Atype_Maximun_Greed_Cnt", ALT_Atype_Maximun_Greed_Cnt)
print ("->ALT_Atype_Greed_Money", ALT_Atype_Greed_Money)


print("-----------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------#
#B타입의 알트코인별 최대 매수 금액(할당 금액) = (총평가금액 * 할당비중(20%) / 최대코인개수)
ALT_Btype_CoinMaxMoney = ((TotalRealMoney * ALT_Btype_Portion) / ALT_Btype_MaxCnt)

#B타입의 알트코인의 첫 매수 금액 = 최대 매수 금액(할당 금액) * 첫매수비중
ALT_Btype_FirstEnterMoney = ALT_Btype_CoinMaxMoney * ALT_Btype_First_Buy_Rate

#절반팔고 절반은 나중에 파려면 업비트 최소 주문금액 5천원의 2배인 1만원은 첫 매수에 들어가야 하는데 2.5를 곱해서 12500원 정도의 최소치를 정해논다
if ALT_Btype_FirstEnterMoney < MinimunCash * 2.5:
    ALT_Btype_FirstEnterMoney = MinimunCash * 2.5


#B타입의 알트코인의 총 물타기 금액 = 최대 매수 금액(할당 금액) * (1.0 - 첫매수비중)
ALT_Btype_TotalWaterMoney = ALT_Btype_CoinMaxMoney * (1.0 - ALT_Btype_First_Buy_Rate)

#A타입의 총 거미줄 매수할 시작 금액! 최소주문금액 5000 * 1.5(보정)
ALT_Btype_Greed_Money = (MinimunCash * 1.5)

#정률로(모든 그리드가 다 같은 금액 매수한다는 가정) 실제로 가능한 최대 거미줄 개수 
ALT_Btype_Maximun_Greed_Cnt = ALT_Btype_TotalWaterMoney / ALT_Btype_Greed_Money




print ("->ALT_Btype_CoinMaxMoney:", ALT_Btype_CoinMaxMoney)
print ("->ALT_Btype_FirstEnterMoney", ALT_Btype_FirstEnterMoney)
print ("->ALT_Btype_TotalWaterMoney", ALT_Btype_TotalWaterMoney)
print ("->ALT_Btype_Maximun_Greed_Cnt", ALT_Btype_Maximun_Greed_Cnt)
print ("->ALT_Btype_Greed_Money", ALT_Btype_Greed_Money)

print("-----------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------#



#알트코인 개수를 프린트!
print("len(AltAtypeList)",len(AltAtypeList))
print("len(AltBtypeList)",len(AltBtypeList))






#----------------------------------------------------------------------------------------------------------------------#



#비트코인이 매수된 상태!
if myUpbit.IsHasCoin(balances,BTC_Ticker) == True:

    #현재 코인의 총 매수금액
    NowCoinTotalMoney = myUpbit.GetCoinNowRealMoney(balances,BTC_Ticker)

    Rate = NowCoinTotalMoney / TotalRealMoney
    print("--------------> BTC rate : ", Rate)

    #비트코인 목표 비중과 현재 비중이 다르다.
    if Rate != BTC_Portion:

        #갭을 구한다!!!
        GapRate = BTC_Portion - Rate
        print("--------------> BTC Gaprate : ", GapRate)

        GapMoney = TotalRealMoney * abs(GapRate)

        #갭이 음수면 비트코인 비중보다 수익이 나서 더 많은 비중을 차지하고 있는 경우
        if GapRate < 0:
            
            #최소 5천원 곱하기 1.2 보다 큰 금액의 갭이다. 
            if GapMoney >=  MinimunCash * 1.2 and abs(GapRate) >= (BTC_Portion / 20.0): 
                print("--------------> SELL BITCOIN!!!!")

                #수익율을 구한다.
                revenue_rate = myUpbit.GetRevenueRate(balances,BTC_Ticker)

                #타겟 수익율보다 높을때만 매도해서 비중을 맞춘다! (손해볼때는 비중조절을 하지 않는다.)
                if revenue_rate > Target_Revenue_Rate:
                
                    #그 갭만큼 수량을 구해서 
                    GapAmt = GapMoney / pyupbit.get_current_price(BTC_Ticker)

                    #시장가 매도를 한다.
                    balances = myUpbit.SellCoinMarket(upbit,BTC_Ticker,GapAmt)

                    
                    # line_alert.SendMessage("ReBalance !!! : " + BTC_Ticker + " by SELL:" )



        #갭이 양수면 비트코인 비중이 적으니 추매할 필요가 있는 경우
        else:

            #최소 5천원 보다 큰 금액의 갭이다. 
            if GapMoney >=  MinimunCash and abs(GapRate) >= (BTC_Portion / 20.0):

                balances = myUpbit.BuyCoinMarket(upbit,BTC_Ticker,GapMoney)
                
                # line_alert.SendMessage("ReBalance !!! : " + BTC_Ticker + " by BUY:" )
                print("--------------> BUY BITCOIN!!!!")

#비트코인이 매수되지 않은 상태
else:

    if BTC_Portion > 0:
        BtcMoney = TotalRealMoney * BTC_Portion


        if BtcMoney < MinimunCash:
            BtcMoney = MinimunCash

        #30% 매수 
        balances = myUpbit.BuyCoinMarket(upbit,BTC_Ticker,BtcMoney)
        print("--------------> BUY BITCOIN!!!!")
#----------------------------------------------------------------------------------------------------------------------#





#----------------------------------------------------------------------------------------------------------------------#
#이더리움이 매수된 상태!
if myUpbit.IsHasCoin(balances,ETH_Ticker) == True:

    #현재 코인의 총 매수금액
    NowCoinTotalMoney = myUpbit.GetCoinNowRealMoney(balances,ETH_Ticker)

    Rate = NowCoinTotalMoney / TotalRealMoney
    print("--------------> ETH rate : ", Rate)

    #이더리움 목표 비중과 현재 비중이 다르다.
    if Rate != ETH_Portion:

        #갭을 구한다!!!
        GapRate = ETH_Portion - Rate
        print("--------------> ETH Gaprate : ", GapRate)

        GapMoney = TotalRealMoney * abs(GapRate)

        #갭이 음수면 이더리움 비중보다 수익이 나서 더 많은 비중을 차지하고 있는 경우
        if GapRate < 0:
            
            #최소 5천원 곱하기 1.2 보다 큰 금액의 갭이다.  
            if GapMoney >=  MinimunCash * 1.2 and abs(GapRate) >= (ETH_Portion / 20.0):

                #수익율을 구한다.
                revenue_rate = myUpbit.GetRevenueRate(balances,ETH_Ticker)

                #타겟 수익율보다 높을때만 매도해서 비중을 맞춘다! (손해볼때는 비중조절을 하지 않는다.)
                if revenue_rate > Target_Revenue_Rate:

                    #그 갭만큼 수량을 구해서 
                    GapAmt = GapMoney / pyupbit.get_current_price(ETH_Ticker)

                    #시장가 매도를 한다.
                    balances = myUpbit.SellCoinMarket(upbit,ETH_Ticker,GapAmt)
                    
                    # line_alert.SendMessage("ReBalance !!! : " + ETH_Ticker + " by SELL:" )

                    print("--------------> SELL Eherium!!!!")


        #갭이 양수면 이더리움 비중이 적으니 추매할 필요가 있는 경우
        else:

            #최소 5천원보다 크다
            if GapMoney >=  MinimunCash and abs(GapRate) >= (ETH_Portion / 20.0):

                balances = myUpbit.BuyCoinMarket(upbit,ETH_Ticker,GapMoney)
            
                # line_alert.SendMessage("ReBalance !!! : " + ETH_Ticker + " by BUY:" )
                print("--------------> BUY Eherium!!!!")
              
#이더리움이 매수되지 않은 상태
else:
    if ETH_Portion > 0:
        #20% 매수 
        EthMoney = TotalRealMoney * ETH_Portion

        if EthMoney < MinimunCash:
            EthMoney = MinimunCash

        balances = myUpbit.BuyCoinMarket(upbit,ETH_Ticker,EthMoney)
        print("--------------> BUY Eherium!!!!")
#----------------------------------------------------------------------------------------------------------------------#








#----------------------------------------------------------------------------------------------------------------------#
#베스트 코인 리스트를 순회한다
print("----------------BUY LOGIC------------------------")
for ticker in BestCoinList:
    try: 
        #매수 된 상태
        if myUpbit.IsHasCoin(balances,ticker) == True:
            print("")




            ####################################################################################################################
            #그런데 이 로직은 추가된 로직으로 이전에 알트코인 단타로직을 타서 AltAtypeList나 AltBtypeList에 들어가 있고 지정가 주문등이 걸려 있을 수 있다.
            #무조건 비중조절 하는 플래그
            MustAdjust = False
            if myUpbit.CheckCoinInList(AltAtypeList,ticker) == True or myUpbit.CheckCoinInList(AltBtypeList,ticker) == True:
                 #일단 모든 지정가 주문을 취소한다!
                myUpbit.CancelCoinOrder(upbit,ticker)
                #무조건 비중 조절을 해야 한다!
                MustAdjust = True



            #A타입의 알트 코인이었다면 리스트에서 제거 해준다!
            if myUpbit.CheckCoinInList(AltAtypeList,ticker) == True:
                AltAtypeList.remove(ticker)

                #파일에 리스트를 저장합니다
                with open(atype_file_path, 'w') as outfile:
                    json.dump(AltAtypeList, outfile)


            #B타입의 알트 코인이었다면 리스트에서 제거 해준다!
            if myUpbit.CheckCoinInList(AltBtypeList,ticker) == True:
                AltBtypeList.remove(ticker)

                #파일에 리스트를 저장합니다
                with open(btype_file_path, 'w') as outfile:
                    json.dump(AltBtypeList, outfile)
            ########################################################################################################################



            NowCoinTotalMoney = myUpbit.GetCoinNowRealMoney(balances,ticker)

            Rate = NowCoinTotalMoney / TotalRealMoney
            print("---BEST-------> ",ticker, " rate : ",  Rate)

            #베스트 알트코인 목표 비중과 현재 비중이 다르다.
            if Rate != Each_BestCoin_Portion:

                #갭을 구한다!!!
                GapRate = Each_BestCoin_Portion - Rate
                print("---BEST-------> ",ticker," Gaprate : ", GapRate)

                GapMoney = TotalRealMoney * abs(GapRate)

                #갭이 음수면 해당 코인 비중보다 수익이 나서 더 많은 비중을 차지하고 있는 경우
                if GapRate < 0:
                    
                    #최소 5천원 곱하기 1.2 보다 큰 금액의 갭이다.  
                    if GapMoney >=  MinimunCash * 1.2 and abs(GapRate) >= (Each_BestCoin_Portion / 20.0):

                        #수익율을 구한다.
                        revenue_rate = myUpbit.GetRevenueRate(balances,ticker)

                        #타겟 수익율보다 높을때만 매도해서 비중을 맞춘다! (손해볼때는 비중조절을 하지 않는다. 단 이전에 알트단타매매에 있던 코인은 무조건 비중조절로 맞추준다!)
                        if revenue_rate > Target_Revenue_Rate or MustAdjust == True:

                            #그 갭만큼 수량을 구해서 
                            GapAmt = GapMoney / pyupbit.get_current_price(ticker)

                            #시장가 매도를 한다.
                            balances = myUpbit.SellCoinMarket(upbit,ticker,GapAmt)
                            print("----BEST------> SELL ",ticker,"!!!!")
                                        
                            # line_alert.SendMessage("ReBalance !!! : " + ticker + " by SELL:" )


                #갭이 양수면 해당 코인 비중이 적으니 추매할 필요가 있는 경우
                else:

                    #최소 5천원보다 크고 
                    if GapMoney >=  MinimunCash and abs(GapRate) >= (Each_BestCoin_Portion / 20.0):

                        balances = myUpbit.BuyCoinMarket(upbit,ticker,GapMoney)
                        print("-----BEST------> BUY ",ticker,"!!!!")
                        
                        # line_alert.SendMessage("ReBalance !!! : " + ticker + " by BUY:" )
                    

        #매수되지 않은 상태
        else:

            if Each_BestCoin_Portion > 0:
                AltMoney = TotalRealMoney * Each_BestCoin_Portion

                if AltMoney < MinimunCash:
                    AltMoney = MinimunCash

                balances = myUpbit.BuyCoinMarket(upbit,ticker,AltMoney)
                print("--------------> BUY ", ticker, "!!!!")

    except Exception as e:
        print("Exception:", e)
#----------------------------------------------------------------------------------------------------------------------#






#----------------------------------------------------------------------------------------------------------------------#
## 탑 코인 리스트를 파일에서 읽어서 TopCoinList에 넣는다. ##
top_file_path = "./UpbitTopCoinList.json"

TopCoinList = list()

try:
    with open(top_file_path, "r") as json_file:
        TopCoinList = json.load(json_file)

except Exception as e:
    TopCoinList = myUpbit.GetTopCoinList("day",30)
    print("Exception:", e)

#----------------------------------------------------------------------------------------------------------------------#

#내가 픽한 코인들..
LovelyCoinList = ['KRW-MED','KRW-BORA','KRW-WAVES','KRW-VET','KRW-THETA','KRW-ALGO','KRW-TRX','KRW-NEAR','KRW-DOT','KRW-XRP','KRW-ADA','KRW-SOL','KRW-DOGE','KRW-MATIC','KRW-ATOM','KRW-LTC','KRW-LINK','KRW-BCH','KRW-XLM','KRW-MANA','KRW-SAND','KRW-AXS','KRW-XTZ','KRW-AVAX','KRW-AAVE','KRW-ETC','KRW-BAT']
#----------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------#
#도달 수익을 임시 저장할 파일
revenue_file_path = "./RevenueDict.json"

revenueDic = dict() #딕셔너리다!!!

#파일을 읽어서 리스트를 만듭니다. 맨 처음엔 없을테니 당연이 예외처리 로그 나옵니다.
try:
    with open(revenue_file_path, "r") as json_file:
        revenueDic = json.load(json_file)

except Exception as e:
    print("Exception :", e)





#이평선 정배열 단타친 코인 리스트
maup_file_path = "./MaUpDict.json"

maupList = list() #

#파일을 읽어서 리스트를 만듭니다. 맨 처음엔 없을테니 당연이 예외처리 로그 나옵니다.
try:
    with open(maup_file_path, "r") as json_file:
        maupList = json.load(json_file)

except Exception as e:
    print("Exception :", e)


#----------------------------------------------------------------------------------------------------------------------#






for ticker in Tickers:
    try: 
        #아침 9시 정각에 파일 삭제처리를 한다! 사실 hour == 0 and min == 0 으로 해도 무관하다
        #하지만 우리 봇이 5분에 1번 실행되게 되어 있으므로 min < 4 이 조건 역시 유효하다.
        if hour == 0 and min < 4:
            if myUpbit.CheckCoinInList(maupList,ticker) == True:

                #보유하지 않고 있다면 리스트에서 제거해준다!!!
                if myUpbit.IsHasCoin(balances,ticker) == False:

                    # 리스트에서 제거 해준다!
                    maupList.remove(ticker)

                    #파일에 리스트를 저장합니다
                    with open(maup_file_path, 'w') as outfile:
                        json.dump(maupList, outfile)


            if myUpbit.CheckCoinInList(DolPaCoinList,ticker) == True:

                #보유하지 않고 있다면 리스트에서 제거해준다!!!
                if myUpbit.IsHasCoin(balances,ticker) == False:
                    #리스트에서 제거 해준다!
                    DolPaCoinList.remove(ticker)

                    #파일에 리스트를 저장합니다
                    with open(dolpha_type_file_path, 'w') as outfile:
                        json.dump(DolPaCoinList, outfile)
                #보유하고 있다
                else:
                    #내가 픽한 코인이 아닌 경우는 손절처리 하자!! 내가 픽한 코인은 존버!!!!
                    if myUpbit.CheckCoinInList(LovelyCoinList,ticker) == False:


                        #수익율을 구한다.
                        revenue_rate = myUpbit.GetRevenueRate(balances,ticker)

                        if revenue_rate < Target_Revenue_Rate:
                            #걸려있는 지정가 주문을 모두 취소하고!
                            myUpbit.CancelCoinOrder(upbit,ticker)

                            #시장가로 남은물량 모두 매도처리합니다!
                            balances = myUpbit.SellCoinMarket(upbit,ticker,upbit.get_balance(ticker))

                            #보유하던 보유하지 않던 하루 지나야 리스트에서 제거 해준다!
                            DolPaCoinList.remove(ticker)

                            #파일에 리스트를 저장합니다
                            with open(dolpha_type_file_path, 'w') as outfile:
                                json.dump(DolPaCoinList, outfile)
                                    
                            # line_alert.SendMessage("DOLPA End CUT!!! : " + ticker + " Revenue:" + str(revenue_rate) )

        
    except Exception as e:
        print("---:", e)









#----------------------------------------------------------------------------------------------------------------------#

#탑코인 리스트를 1위부터 30위 순으로 순회한다!
print("----------------BUY LOGIC------------------------")
for ticker in TopCoinList:
    try: 
        print("---->" , ticker)
        #변동성 돌파면 스킵한다!
        if myUpbit.CheckCoinInList(DolPaCoinList,ticker) == True:   
            continue

        #베스트 코인이라면 스킵한다!
        if myUpbit.CheckCoinInList(BestCoinList,ticker) == True:
            continue

        #이미 매수된 코인이라면 스킵한다!
        if myUpbit.IsHasCoin(balances,ticker) == True:
            continue

        #내가 픽한 코인들만 매수 대상으로 삼는다!
        if myUpbit.CheckCoinInList(LovelyCoinList,ticker) == True:
            print("---------> Target Coin ---> ", ticker)


            ################일봉 데이타를 읽어 해당 코인이 상승장인지 알아본다################
            time.sleep(0.05)
            df = pyupbit.get_ohlcv(ticker,interval="day") #일봉 데이타를 가져온다.

            #이평선을 구한다!
            ma5_before3 = myUpbit.GetMA(df,5,-3) #그제
            ma5_before = myUpbit.GetMA(df,5,-2) #어제
            ma5_now = myUpbit.GetMA(df,5,-1) #현재

            now_price = pyupbit.get_current_price(ticker) #코인 현재가격

            IsUpTrend = False #상승장 여부

            #5일선이 증가 추세면서 현재가격이 5일선 위에 있을 때 상승장!!!!
            if ma5_before3 < ma5_before < ma5_now < now_price:
                IsUpTrend = True #상승장이다!!!!

            ######################################################################


            
            ################5분봉 데이타를 읽고 지표에 의거 매수를 한다!################
            time.sleep(0.05)
            df_5 = pyupbit.get_ohlcv(ticker,interval="minute5") #5분봉 데이타를 가져온다.

            #RSI지표를 구한다.
            rsi_before4 = myUpbit.GetRSI(df_5,14,-4)
            rsi_before3 = myUpbit.GetRSI(df_5,14,-3)
            rsi_before = myUpbit.GetRSI(df_5,14,-2)

            print ("rsi14 --> ",rsi_before4,rsi_before3,rsi_before)


            #MA지표를 구한다.
            ma5_before2 = myUpbit.GetMA(df_5,5,-3)
            ma5_before = myUpbit.GetMA(df_5,5,-2)
            ma5_now = myUpbit.GetMA(df_5,5,-1)

            print ("ma5 --> ",ma5_before2,ma5_before,ma5_now)

            ma10_before2 = myUpbit.GetMA(df_5,10,-3)
            ma10_before = myUpbit.GetMA(df_5,10,-2)
            ma10_now = myUpbit.GetMA(df_5,10,-1)

            
            print ("ma10 --> ",ma10_before2,ma10_before,ma10_now)

            ma20_before2 = myUpbit.GetMA(df_5,20,-3)
            ma20_before = myUpbit.GetMA(df_5,20,-2)
            ma20_now = myUpbit.GetMA(df_5,20,-1)


            print ("ma20 --> ",ma20_before2,ma20_before,ma20_now)


            ma60_before2 = myUpbit.GetMA(df_5,60,-3)
            ma60_before = myUpbit.GetMA(df_5,60,-2)
            ma60_now = myUpbit.GetMA(df_5,60,-1)

            
            print ("ma60 --> ",ma60_before2,ma60_before,ma60_now)


            #현재 전략 RSI지표가 30이하로 들어 간뒤 상승으로 변경 될때! (즉 꺾인 꼭지가 30이하면 조건 만족!) 혹은 5,10,20,60선이 정배열이면서 상승하고 있고 현재가가 5선 위에 있는 상승추세일때
            if (rsi_before4 > rsi_before3 and rsi_before3 < rsi_before and rsi_before3 <= 30.0) or (rsi_before < 70.0 and myUpbit.CheckCoinInList(maupList,ticker) == False and ma5_before2 < ma5_before and ma10_before2 < ma10_before and ma20_before2 < ma20_before and ma60_before2 < ma60_before and ma60_now < ma20_now < ma10_now < ma5_now < now_price):

                print("IN Target!!!")
                bAlreadyBTypeBuyDone = False

                #아무때나 매수 가능한 B타입이 아직 매수가능 코인 개수가 남아 있을때! (B타입 리스트 개수가 최대매수코인 개수보다 작을 경우)
                if len(AltBtypeList) < ALT_Btype_MaxCnt:
                    #시장가로 매수한다!
                    balances = myUpbit.BuyCoinMarket(upbit,ticker,ALT_Btype_FirstEnterMoney)


                    if (ma5_before2 < ma5_before and ma10_before2 < ma10_before and ma20_before2 < ma20_before and ma60_before2 < ma60_before and ma60_now < ma20_now < ma10_now < ma5_now < now_price):
                        #매수된 코인을 maupList 리스트에 넣고 이를 파일로 저장해둔다!
                        maupList.append(ticker)
                        
                        #파일에 리스트를 저장합니다
                        with open(maup_file_path, 'w') as outfile:
                            json.dump(maupList, outfile)




                    #수익율 당연히 코인명(키)과 수익율(값)을 파일저장한다!
                    revenueDic[ticker] = 0  #당연히 첫 매수니 수익율을 0이다!

                    #파일에 리스트를 저장합니다
                    with open(revenue_file_path, 'w') as outfile:
                        json.dump(revenueDic, outfile)

                    bAlreadyBTypeBuyDone = True


                    #매수된 코인을 AltBtypeList 리스트에 넣고 이를 파일로 저장해둔다!
                    AltBtypeList.append(ticker)
                    
                    #파일에 리스트를 저장합니다
                    with open(btype_file_path, 'w') as outfile:
                        json.dump(AltBtypeList, outfile)





                    #평균 매입 단가를 읽어옵니다!
                    avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
                    #매입 수량
                    coin_volume = upbit.get_balance(ticker)

                    target_price =  avgPrice * (1.0 + (Target_Revenue_Rate/100.0)) #목표 수익 가격

                    #지정가 매도를 주문을 넣는다(익절) 단 절반만 익절한다!!!
                    myUpbit.SellCoinLimit(upbit,ticker,target_price,coin_volume * 0.5)
                    

                    #그리고 그 밑에 그리드(거미줄) 라인을 갭차이 만큼 쭉 깔아놓는다! (물타기 매수 주문들)

                    total_water_money = ALT_Btype_TotalWaterMoney
                    water_money = ALT_Btype_Greed_Money
                    #아래는 물타기 라인을 긋는 로직이다. 거미줄 만들기!
                    for i in range(1,int(ALT_Btype_Maximun_Greed_Cnt)+1): #ALT_Btype_Greed_Gap 0.3이라면 손실율 -0.3,-0.6,-0.9....마다 물타기 라인을 만든다.

                        water_price = avgPrice * (1.0 - ((ALT_Btype_Greed_Gap/100.0) * i)) # 0.3% 하락한 지점의 가격

                        print("----> water_price",water_price)

                        #그럼 그 금액으로 얼마큼의 수량을살 수 있느냐?
                        water_volume = water_money / water_price #필요 금액에서 타겟 가격을 나누면 된다 

                        #실제 물타는 매수 라인 주문을 넣는다.
                        myUpbit.BuyCoinLimit(upbit,ticker,water_price,water_volume)
                        time.sleep(0.2)

                        #매수한 금액만큼 빼준다
                        total_water_money -= water_money

                        #그런데 남은 금액이 미니멈 캐시보다 적다면 중단!!!!
                        if total_water_money < MinimunCash:
                            break

                        #3의 배수마다 물타기 금액을 2배 증가 시켜 준다!
                        if i % 3 == 0:
                            water_money *= 2


                        #만약 현재 남은 금액이 다음 매수할 금액보다 적다면 
                        if total_water_money < water_money:
                            water_money = total_water_money #남은 금액을 넣어준다!

                    # line_alert.SendMessage("DANTA B START : " + ticker)

                #상승장일때는 A타입 코인 리스트를 만들 수 있다! (매수할 수 있다)
                if IsUpTrend == True and bAlreadyBTypeBuyDone == False:

                    #아무때나 매수 가능한 A타입이 아직 매수가능 코인 개수가 남아 있을때! (A타입 리스트 개수가 최대매수코인 개수보다 작을 경우)
                    if len(AltAtypeList) < ALT_Atype_MaxCnt:
                        #시장가로 매수한다!
                        balances = myUpbit.BuyCoinMarket(upbit,ticker,ALT_Atype_FirstEnterMoney)

                        if (ma5_before2 < ma5_before and ma10_before2 < ma10_before and ma20_before2 < ma20_before and ma60_before2 < ma60_before and ma60_now < ma20_now < ma10_now < ma5_now < now_price):
                            #매수된 코인을 maupList 리스트에 넣고 이를 파일로 저장해둔다!
                            maupList.append(ticker)
                            
                            #파일에 리스트를 저장합니다
                            with open(maup_file_path, 'w') as outfile:
                                json.dump(maupList, outfile)


                        #수익율 당연히 코인명(키)과 수익율(값)을 파일저장한다!
                        revenueDic[ticker] = 0  #당연히 첫 매수니 수익율을 0이다!

                        #파일에 리스트를 저장합니다
                        with open(revenue_file_path, 'w') as outfile:
                            json.dump(revenueDic, outfile)




                        #매수된 코인을 AltAtypeList 리스트에 넣고 이를 파일로 저장해둔다!
                        AltAtypeList.append(ticker)
                        
                        #파일에 리스트를 저장합니다
                        with open(atype_file_path, 'w') as outfile:
                            json.dump(AltAtypeList, outfile)



                        #평균 매입 단가를 읽어옵니다!
                        avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
                        #매입 수량
                        coin_volume = upbit.get_balance(ticker)

                        target_price =  avgPrice * (1.0 + (Target_Revenue_Rate/100.0)) #목표 수익 가격

                        #지정가 매도를 주문을 넣는다(익절) 단 절반만 익절한다!!!
                        myUpbit.SellCoinLimit(upbit,ticker,target_price,coin_volume * 0.5)


                        #그리고 그 밑에 그리드(거미줄) 라인을 갭차이 만큼 쭉 깔아놓는다! (물타기 매수 주문들)

                        total_water_money = ALT_Atype_TotalWaterMoney
                        water_money = ALT_Atype_Greed_Money
                        #아래는 물타기 라인을 긋는 로직이다. 거미줄 만들기!
                        for i in range(1,int(ALT_Atype_Maximun_Greed_Cnt)+1): #ALT_Btype_Greed_Gap 0.3이라면 손실율 -0.3,-0.6,-0.9....마다 물타기 라인을 만든다.


                            water_price = avgPrice * (1.0 - ((ALT_Atype_Greed_Gap/100.0) * i)) # 1% 하락한 지점의 가격

                            print("----> water_price",water_price)

                            #그럼 그 금액으로 얼마큼의 수량을살 수 있느냐?
                            water_volume = water_money / water_price #필요 금액에서 타겟 가격을 나누면 된다 

                            #실제 물타는 매수 라인 주문을 넣는다.
                            myUpbit.BuyCoinLimit(upbit,ticker,water_price,water_volume)
                            time.sleep(0.2)

                            #매수한 금액만큼 빼준다
                            total_water_money -= water_money

                            #그런데 남은 금액이 미니멈 캐시보다 적다면 중단!!!!
                            if total_water_money < MinimunCash:
                                break

                            #3의 배수마다 물타기 금액을 2배 증가 시켜 준다!
                            if i % 3 == 0:
                                water_money *= 2


                            #만약 현재 남은 금액이 다음 매수할 금액보다 적다면 
                            if total_water_money < water_money:
                                water_money = total_water_money #남은 금액을 넣어준다!

                        # line_alert.SendMessage("DANTA A START : " + ticker)


            ######################################################################






    except Exception as e:
        print("---:", e)

print("--------------------------------------------------")
print("--------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------#





#----------------------------------------------------------------------------------------------------------------------#
#고점수익율 대비 0.3%수익율 감소가 있다면 팔아버린다!
tralling_stop_rate = 0.3

#이미 보유하고 있는 코인인 매도 대상이다!!
print("----------------SELL LOGIC------------------------")
for ticker in Tickers:
    try: 
        print("---->" , ticker)

        #베스트 코인이라면 스킵한다!
        if myUpbit.CheckCoinInList(BestCoinList,ticker) == True:
            continue

        #변동성 돌파면 스킵한다!
        if myUpbit.CheckCoinInList(DolPaCoinList,ticker) == True:   
            continue


        #이미 보유하고 있다며!! 비트코인과 이더리움은 제외! 이미 위에서 매수매도 처리를 하니깐!
        if myUpbit.IsHasCoin(balances,ticker) == True and ticker != BTC_Ticker and ticker != ETH_Ticker:
            

            #수익율을 구한다.
            revenue_rate = myUpbit.GetRevenueRate(balances,ticker)


            print("---------> Has coin : ", ticker, " revenue_rate --> ", revenue_rate)


            #그런데 이전 고점수익율이 타겟 수익율보다 높다???
            if revenueDic[ticker] >= Target_Revenue_Rate:
                #이 안에 들어왔다는 이야기는 지정가 주문이 체결되 절반은 팔렸다는 이야기가 된다
                #그럼 남은 절반의 물량은 어떻게 할 것인가?

                #트레일링 스탑 기능을 사용해 수익율을 갱신할때마다 파일에 저장하고 고점수익율 대비 0.3%정도 떨어지면 나머지 물량을 정리하자!!!
                if revenueDic[ticker] - tralling_stop_rate > revenue_rate:
                    
                    #걸려있는 지정가 주문을 모두 취소하고!
                    myUpbit.CancelCoinOrder(upbit,ticker)

                    #시장가로 남은물량 모두 매도처리합니다!
                    balances = myUpbit.SellCoinMarket(upbit,ticker,upbit.get_balance(ticker))


                    #A타입의 알트 코인이었다면 리스트에서 제거 해준다!
                    if myUpbit.CheckCoinInList(AltAtypeList,ticker) == True:
                        AltAtypeList.remove(ticker)

                        #파일에 리스트를 저장합니다
                        with open(atype_file_path, 'w') as outfile:
                            json.dump(AltAtypeList, outfile)

                        
                        # line_alert.SendMessage("DANTA A END : " + ticker)


                    #B타입의 알트 코인이었다면 리스트에서 제거 해준다!
                    if myUpbit.CheckCoinInList(AltBtypeList,ticker) == True:
                        AltBtypeList.remove(ticker)

                        #파일에 리스트를 저장합니다
                        with open(btype_file_path, 'w') as outfile:
                            json.dump(AltBtypeList, outfile)

                        
                        # line_alert.SendMessage("DANTA B END : " + ticker)

            #여기선 물타기 주문이 걸려서 평단과 수량이 변경된 경우 이를 새로 변경된 평단과 수량으로 익절 주문을 다시 걸어준다!!!

            #코인의 평균 단가
            avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)

            #수익 목표가
            target_price =  avgPrice * (1.0 + (Target_Revenue_Rate/100.0)) 

            #지정가 주문 데이터를 읽는다.
            orders_data = upbit.get_order(ticker)

            #모든 주문을 뒤진다!
            for order in orders_data:
                if order['side'] == 'ask' : #매도 주문인데 
                    if float(order['price']) != float(pyupbit.get_tick_size(target_price)): #현재 평단의 익절 라인과 같지 않다면 물이타졌다는 이야기니까! 갱신해야 한다!

                        upbit.cancel_order(order['uuid']) #해당 주문 취소 시키고! 다시 새 주문을 거다
                        time.sleep(0.2)

                        #해당 코인의 현재 보유 수량
                        coin_volume = upbit.get_balance(ticker)

                        #지정가 매도를 주문을 다시 넣는다(익절) 역시 절반만 건다!
                        myUpbit.SellCoinLimit(upbit,ticker,target_price,coin_volume * 0.5)
                        


            #저장된 수익율보다 현재 수익율이 클때만 갱신시켜준다!
            if revenueDic[ticker] < revenue_rate:

                #현재 수익율을 코인티커와 함께 저장해 두자!
                revenueDic[ticker] = revenue_rate 

                #파일에 리스트를 저장합니다
                with open(revenue_file_path, 'w') as outfile:
                    json.dump(revenueDic, outfile)


    except Exception as e:
        print("---:", e)


print("--------------------------------------------------")
print("--------------------------------------------------")
    







#변동성 돌파 전략
print("----------------DOLPHA LOGIC------------------------")



dolpha_tralling_stop_rate = 0.5

for ticker in Tickers:
    try: 

        print("---->" , ticker)
        #장투하는 비트코인, 이더리움, 베스트 코인이라면 스킵한다!
        if myUpbit.CheckCoinInList(BestCoinList,ticker) == True or ticker == BTC_Ticker or ticker == ETH_Ticker:
            continue

        #현재 단타중인 코인이라면 역시 스킵한다!!
        if myUpbit.CheckCoinInList(AltAtypeList,ticker) == True or myUpbit.CheckCoinInList(AltBtypeList,ticker) == True:
            continue

        #그 나머지는 어디에도 해당되지 않는다!
        #코인 보유하고 있다면 변동성 돌파에 의해 매수된 코인이다!
        if myUpbit.IsHasCoin(balances,ticker) == True and myUpbit.CheckCoinInList(DolPaCoinList,ticker) == True:
            print("DOLPHA sell")

            #수익율을 구한다.
            revenue_rate = myUpbit.GetRevenueRate(balances,ticker)


            print("---------> Has coin : ", ticker, " revenue_rate --> ", revenue_rate)
            #타겟 수익율 확보!
            if revenueDic[ticker] >= Target_Revenue_Rate:
                #트레일링 스탑 기능을 사용해 수익율을 갱신할때마다 파일에 저장하고 고점수익율 대비 0.5%정도 떨어지면 나머지 물량을 정리하자!!!
                if revenueDic[ticker] - dolpha_tralling_stop_rate > revenue_rate:
                    #걸려있는 지정가 주문을 모두 취소하고!
                    myUpbit.CancelCoinOrder(upbit,ticker)

                    #시장가로 남은물량 모두 매도처리합니다!
                    balances = myUpbit.SellCoinMarket(upbit,ticker,upbit.get_balance(ticker))

                    
                    # line_alert.SendMessage("DOLPA End!!! : " + ticker + " Revenue:" + str(revenue_rate) )



            #저장된 수익율보다 현재 수익율이 클때만 갱신시켜준다!
            if revenueDic[ticker] < revenue_rate:

                #현재 수익율을 코인티커와 함께 저장해 두자!
                revenueDic[ticker] = revenue_rate 

                #파일에 리스트를 저장합니다
                with open(revenue_file_path, 'w') as outfile:
                    json.dump(revenueDic, outfile)


        else:
            #거래량 많은 탑코인 30만 대상으로 삼는다!
            if myUpbit.CheckCoinInList(TopCoinList,ticker) == True: 


                print("DOLPHA buy")
                print("!!!!! Target Coin!!! :",ticker)


                
                time.sleep(0.05)
                df = pyupbit.get_ohlcv(ticker,interval="day") #일봉 데이타를 가져온다.
                rsi_before = myUpbit.GetRSI(df,14,-2)
                ma5_now = myUpbit.GetMA(df,5,-1) #현재

                Range = (float(df['high'][-2]) - float(df['low'][-2])) * 0.5
                
                #이전 종가가 오늘의 시가..
                #어제의 고가와 저가의 변동폭에 0.5를 곱해서
                #오늘의 시가와 더해주면 목표 가격이 나온다!
                target_price = float(df['close'][-2]) + Range
                
                #현재가
                now_price = float(df['close'][-1])

                print(now_price , " > ", target_price)



                #이를 돌파했다면 변동성 돌파 성공!!
                if now_price >=  target_price and len(DolPaCoinList) < MaxDolPaCoinCnt and myUpbit.CheckCoinInList(DolPaCoinList,ticker) == False and rsi_before < 50 and ma5_now <= now_price:
                    print("!!!!!!!!!!!!!!!First Buy GoGoGo!!!!!!!!!!!!!!!!!!!!!!!!")

                    if Each_DolPa_Portion > 0:
                        DolPaMoney = TotalRealMoney * Each_DolPa_Portion


                        if DolPaMoney < MinimunCash:
                            DolPaMoney = MinimunCash

                        #매수 
                        balances = myUpbit.BuyCoinMarket(upbit,ticker,DolPaMoney)

                        #수익율 당연히 코인명(키)과 수익율(값)을 파일저장한다!
                        revenueDic[ticker] = 0  #당연히 첫 매수니 수익율을 0이다!

                        #파일에 리스트를 저장합니다
                        with open(revenue_file_path, 'w') as outfile:
                            json.dump(revenueDic, outfile)


                        #매수된 코인을 DolPaCoinList 리스트에 넣고 이를 파일로 저장해둔다!
                        DolPaCoinList.append(ticker)
                        
                        #파일에 리스트를 저장합니다
                        with open(dolpha_type_file_path, 'w') as outfile:
                            json.dump(DolPaCoinList, outfile)




                        #평균 매입 단가를 읽어옵니다!
                        avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
                        #매입 수량
                        coin_volume = upbit.get_balance(ticker)

                        minimun_target_price =  avgPrice * (1.0 + (Target_Revenue_Rate/100.0)) #목표 수익 가격
                        
                        minimun2_target_price =  avgPrice * (1.0 + (Target_Revenue_Rate * 2.0/100.0)) #목표 수익 가격

                        First_target_price = avgPrice + Range * 0.5

                        if First_target_price < minimun_target_price:
                            First_target_price = minimun_target_price


                        Second_target_price = avgPrice + Range

                        if Second_target_price < minimun2_target_price:
                            Second_target_price = minimun2_target_price

                        #지정가 매도를 주문을 넣는다(익절) 단 25%만 익절한다!!!
                        myUpbit.SellCoinLimit(upbit,ticker,First_target_price,coin_volume * 0.25)

                        #지정가 매도를 주문을 넣는다(익절) 단 25%만 익절한다!!!
                        myUpbit.SellCoinLimit(upbit,ticker,Second_target_price,coin_volume * 0.25)


                        
                        # line_alert.SendMessage("DOLPA START : " + ticker)



    except Exception as e:
        print("---:", e)


#----------------------------------------------------------------------------------------------------------------------#






