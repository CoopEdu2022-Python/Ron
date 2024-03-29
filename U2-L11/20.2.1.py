class B:
    m = 100
    n = 99

    def __init__(self):
        self.m = 98
        self.n = 97

    def __del__(self):
        A.m = 96
        A.n = 95

    def __func1(self):
        self.m += 94
        self.n += 93

    def func2(self):
        self.m -= 92
        self.n -= 91

    @classmethod
    def func3(cls):
        cls.m += 90
        cls.n += 89

    def func4(cls, self):
        cls.m -= 88
        cls.n -= 87
        self.m -= 86
        self.n -= 85

    @staticmethod
    def func5():
        print(84)

    def func6(cls):
        cls.m += 83
        cls.n += 82


# 1.5.1  统计属性、方法的数量
# Builtin method（2），Static method（1）
# Class attribute（2），Class method（1）
# Instance Attribute（2），Instance method（4）

# 1.5.2 分析主程序输出
# 98,97

# 1.5.3 分析主程序输出
# False

# 1.5.4  分析主程序输出
# 98,97

# 1.5.5  分析主程序输出
# 190,188

# 1.5.6  分析主程序输出
# False

# 1.5.7  分析主程序输出
# -76,-75,100,99


# 1.5.8  分析主程序输出
# 100,99


# 1.5.9  分析主程序输出
# 8
