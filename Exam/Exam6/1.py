# 1. 判断是否为 3 的幂
# 定义一个函数 is_power_of_3_v1(n)，参数为整数，判断 n 是否为 3 的幂
# 定义另一个函数 is_power_of_3_v2(n)，用另一种方式，判断 n 是否为 3 的幂
# n 的取值范围为 -2^31 <= n <= 2^31 - 1
def is_power_of_3_v1(n):
    if n==1:
        return True
    if n%3==0:
        return is_power_of_3_v1(n/3)
    else:
        return False


print(is_power_of_3_v1(12))


def is_power_of_3_v2(n):
    while 1:
        if n==1:
            return True
        if n%3==0:
            n=n/3
        else:
            return False


print(is_power_of_3_v2(6))