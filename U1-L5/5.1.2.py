# 5.1.2 定义两个列表，分别存储平年和闰年的每个月份的天数，按照月份打印这个月的天数
# 例：平年的 1 月有 31 天，闰年的 1 月有 31 天
month_day_P = [31,28,31,30,31,30,31,31,30,31,30,31]
month_day_R = [31,29,31,30,31,30,31,31,30,31,30,31]
for day in range(1,13):
        print("平年的%d月有%d天,闰年的%d月有%d天"%(day,month_day_P[day-1],day,month_day_R[day-1]))
