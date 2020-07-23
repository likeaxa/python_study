# 最简单的函数示编程 完成学生管理系统
"""

*****************
欢迎使用学生管理系统
1 显示所有学生的信息
2 新增学生信息
3 查询学生信息
4 修改学生信息
5 删除学生信息
0 退出系统
*****************
"""
# 初始化所有学生的信息
student_data = [
    {
        "id": "12345455",
        "name": "A",
        "address": "guangzhou",
        "sex": "nan"
    }, {
        "id": "12345455",
        "name": "B",
        "address": "guangzhou",
        "sex": "nan"
    }, {
        "id": "12345455",
        "name": "C",
        "address": "guangzhou",
        "sex": "nan"
    }, {
        "id": "12d345455",
        "name": "",
        "address": "guangzhou",
        "sex": "nan"
    }
]


# 1 显示所有学生的信息
def show_all():
    for student in student_data:
        print(student)


# 2 新增学生信息
def create_student():
    name = input('请输入学生名称')
    age = input('请输入学生性别')
    address = input('请输入学生地址')
    student = {
        "name": name,
        "age": age,
        "address": address
    }
    student_data.append(student)


# 3 查询学生信息
def find_student():
    name = input('请输入学生的名称')
    for student in student_data:
        if name == student['name']:
            print(student)
            return student
    print('查询不到该学生')
    return None

# 4 修改学生信息
def update_student():
    student = find_student()

    if student is None:
        print('查询不到该学生')
        return
    student_data.remove(student)
    create_student()


# 5 删除学生信息
def remove_student():
    student = find_student()
    if student is not None:
        student_data.remove(student)

def output():
    print(''''
*****************
欢迎使用学生管理系统
1 显示所有学生的信息
2 新增学生信息
3 查询学生信息
4 修改学生信息
5 删除学生信息
0 退出系统
*****************'''
          )


while True:
    output()
    op = input("请输入查询的序号")
    if op == '1':
        show_all()
    elif op == '2':
        create_student()
    elif op == '3':
        find_student()
    elif op == '4':
        update_student()
    elif op == '5':
        remove_student()
    elif op == '0':
        break
