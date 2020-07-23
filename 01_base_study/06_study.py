# 类和对象： 面向对象编程
# 人 ：张三 李四 王五
# 人是类
# 张三 李四 王五 是具体的对象
class Person:
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    def say(selfs, word):
        print(f'{selfs.name}说:{word}')


zhang_shan = Person('张三', '男', '2020-12-12')
zhang_shan.say('你好')
