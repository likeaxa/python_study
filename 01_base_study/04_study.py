# 文件读取
f = open('file', encoding='utf-8')
str = f.read()
print(str)
f.close()
# 文件写入
f = open('write_test', mode='w', encoding='utf-8')
f.write('likeaxa\n')
f.write('they is a good day')
f.close()