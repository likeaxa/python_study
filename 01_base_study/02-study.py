print('pytho\nn')
print("pytho\n\tn")

# 字符串的索引
s = '床前明月光'
print(s[0])
# 导数第一个
print(s[-1])
# 字符串的切片
print(s[1:4])
# 1 起始 5 结束 2 步长
print(s[1:5:2])
print(s[1:])
print(s[0:])

# 字符串格式化输出
val1 = 'A'
val2 = 'B'
print(f'{val1}对{val2}说 ： hello')
# + 可以拼接2个字符串
print("hello" + "word")

# 列表
my_list = [1, 2, 4]
print(my_list[1:])
# append insert extent
my_list.append([1, 2])
print(my_list)
my_list.insert(1, 2)
print(my_list)
my_list.extend([1, 2])
print(my_list)
# pop
my_list.pop()
print(my_list)
my_list.remove([1, 2])
print(my_list)
my_list.remove(2)
print(my_list)
my_list[0] = my_list[0] + 1
print(my_list)
# 元祖 不可修改的list 初始化把 [] 变成 （）
my_tuple = (1, 2, 3)
print(my_tuple)

map = {
    "name": "likeaxa",
    "age":"22",
    "gender":"male"
}
print(map)
print(map['name'])
map['age'] = 23
print(map)
