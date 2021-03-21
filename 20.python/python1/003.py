# 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

# 10000以内判断，将该数加上100后再开平方，加上268后再开平方，如果开平方结果满足就是结果

import math

for i in range(1,10001):
    n = math.sqrt(i + 100)
    m = math.sqrt(i + 268)
    if n % 1 == 0 and m % 1 == 0:
        print(i,n,m)
        

