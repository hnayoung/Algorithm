cash = int(input())
juga = list(map(int, input().split()))

# 준현의 BNP (Buy and Pray) 전략
jun_cash = cash
jun_jusic = 0
for price in juga:
    if jun_cash >= price:
        shares_to_buy = jun_cash // price
        jun_jusic += shares_to_buy
        jun_cash -= shares_to_buy * price

jun_total = jun_cash + jun_jusic * juga[-1]

# 성민의 33 매매법 (TIMING)
sung_cash = cash
sung_jusic = 0
for i in range(1, len(juga)):
    # 3일 연속 상승 시 다음 날 전량 매도
    if i > 2 and juga[i-3] < juga[i-2] < juga[i-1]:
        if sung_jusic > 0:
            sung_cash += sung_jusic * juga[i]
            sung_jusic = 0
    # 3일 연속 하락 시 다음 날 전량 매수
    elif i > 2 and juga[i-3] > juga[i-2] > juga[i-1]:
        if sung_cash >= juga[i]:
            shares_to_buy = sung_cash // juga[i]
            sung_jusic += shares_to_buy
            sung_cash -= shares_to_buy * juga[i]

sung_total = sung_cash + sung_jusic * juga[-1]

# 결과 출력
if jun_total > sung_total:
    print('BNP')
elif jun_total < sung_total:
    print('TIMING')
else:
    print('SAMESAME')