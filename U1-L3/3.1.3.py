# 3.1.3 小红将账户中价值 2 亿人民币的数字货币全部转出，购买了某公司的股票，但公司经营不善，每个月都缩水为原来的一半。
# 小红从千万富翁沦落为穷光蛋（资产 < 10 元），需要几个月？此时她的资产是多少元？（打印一条消息表示）
money = 200000000
a = 0
while money <= 200000000:
    if money < 10:
        break
    money /= 2
    a += 1
print("需要%f月，此时她的资产为%f元" % (a, money))
