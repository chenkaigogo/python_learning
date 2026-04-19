# 学生成绩管理系统（函数进阶版）

students = []  # 全局变量

def add_student():
    name = input("请输入学生姓名：")
    # 检查是否存在
    for stu in students:
        if stu["name"] == name:
            print("该学生已存在！")
            return
    score_input = input("请输入学生成绩：")
    if score_input.replace('.', '').isdigit():
        score = float(score_input)
        students.append({"name": name, "score": score})
        print(f"学生{name}添加成功！")
    else:
        print("成绩必须是数字！")

def show_all():
    if len(students) == 0:
        print("暂无学生信息。")
        return
    print("\n所有学生成绩：")
    print("姓名\t\t成绩")
    print("-" * 20)
    for stu in students:
        print(f"{stu['name']}\t\t{stu['score']}")

def query_student():
    name = input("请输入要查询的学生姓名：")
    for stu in students:
        if stu["name"] == name:
            print(f"{name}的成绩是：{stu['score']}")
            return
    print("未找到该学生。")

def calc_average():
    if len(students) == 0:
        print("暂无学生信息，无法计算平均分。")
        return
    total = 0
    for stu in students:
        total += stu["score"]
    avg = total / len(students)
    print(f"共有{len(students)}名学生，平均分是：{avg:.2f}")

# 主程序
while True:
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 查询学生成绩")
    print("4. 计算平均分")
    print("5. 退出系统")
    print("============================")
    
    choice = input("请选择操作（1-5）：")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        query_student()
    elif choice == "4":
        calc_average()
    elif choice == "5":
        print("感谢使用，再见！")
        break
    else:
        print("无效选择，请重新输入。")