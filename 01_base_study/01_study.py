import random

print(1 + 1)
print(3 - 1)
print(3 * 4)
print(27 / 3)
print(27 // 3)

width = 3
height = 4
# 变量不能数字开头 可以数字结尾
print(width * height)

box_width = 3
box_height = 5
BOX_HEIGHT = 6
# 多个单词的变量用下划线分割
print(box_width * box_height)
# python 大小写是分割的
print(box_width * BOX_HEIGHT)

# python if 语句
age = 19
if age > 18:
    print("可以进入")
else:
    print('年纪太小 不能进入')

# if elif else 语句
score = 80
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')

# for 语句
for i in range(5):
    print(i)
for i in range(1, 5):
    print(i)

# 1 是起始位置 5 是终点 2 是步长
for i in range(1, 5, 2):
    print(i)
# while 语句
n = 1
while n < 10:
    n = n + 1
    print(n)
else:
    print('循环结束')

# for 循环嵌套 输出乘法口诀表
print('for 嵌套输出 口诀表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={j * i}', end=' ')
    print()
# while 循环嵌套 输出乘法口诀表
print('while 嵌套输出 口诀表')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={j * i}', end=' ')
        j = j + 1
    else:
        i = i + 1
        print()
# for 和 while 的不同
# for 后面接受的是个序列
# while 后面接受的是个判断
# for while 混合用法
print('for while 嵌套输出 口诀表')
for i in range(1, 10):
    j = 1
    while j <= i:
        print(f'{i}*{j}={j * i}', end=' ')
        j = j + 1
    else:
        print()

# break 结束整个循环
# 注释掉 避免后面的程序 需要卡这里
# while True:
#     s = input('输入：（0）退出：')
#     if s == '0':
#         break
#     print('你输入的是 ', s)

# continue
for s in 'python':
    if s == 'y':
        continue
    print(s)

# 猜数字的游戏
# 键盘输入的是 string 类型 咱们定义的 是int 类型 2者不能对比
target = random.randint(1,100)
while True:
    s = int(input('输入 1到 100之间的整数：'))
    if s < target:
        print('猜小了')
    elif s > target:
        print('猜大了')
    else:
        print('猜对了')
        break
print('游戏结束')

# 只能猜5次的 猜数字的游戏
target = random.randint(1,100)
total = 5
count = 0
while True:
    s = int(input('输入 1到 100之间的整数：'))
    if s < target:
        print('猜小了')
    elif s > target:
        print('猜大了')
    else:
        print('猜对了')
        break
    count = count +1
    if count == total :
        print('你已经猜了5次了 游戏结束')
        break
print('游戏结束')
