# 函数
# 函数的作用
# 1 降低编程的难度
# 2 增加代码的复用性

# 1+ 2+ 。。。+ 100

n = 1
s = 0
while n <= 100:
    s, n = s + n, n + 1
print(s)


def addCount(n ,m):
    s = 0
    while n <= m:
        s, n = s + n, n + 1
    return s

print(addCount(5,10))