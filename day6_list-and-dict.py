# 学生成绩管理系统
# 学生成绩管理系统（无函数版本）

students = []  # 存储学生信息，每个学生是字典 {"name": "张三", "score": 85}

while True:
    # 显示菜单
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 查询学生成绩")
    print("4. 计算平均分")
    print("5. 退出系统")
    print("============================")
    
    choice = input("请选择操作（1-5）：")
    
    # 1. 添加学生
    if choice == "1":
        name = input("请输入学生姓名：")
        # 检查是否重复
        exists = False
        for stu in students:
            if stu["name"] == name:
                exists = True
                break
        if exists:
            print("该学生已存在！")
        else:
            score_input = input("请输入学生成绩：")
            # 简单判断是否为数字（后续可优化）
            if score_input.replace('.', '').isdigit():
                score = float(score_input)
                students.append({"name": name, "score": score})
                print(f"学生{name}添加成功！")
            else:
                print("成绩必须是数字！")
    
    # 2. 查看所有学生
    elif choice == "2":
        if len(students) == 0:
            print("暂无学生信息。")
        else:
            print("\n所有学生成绩：")
            print("姓名\t\t成绩")
            print("-" * 20)
            for stu in students:
                print(f"{stu['name']}\t\t{stu['score']}")
    
    # 3. 查询学生成绩
    elif choice == "3":
        name = input("请输入要查询的学生姓名：")
        found = None
        for stu in students:
            if stu["name"] == name:
                found = stu
                break
        if found:
            print(f"{name}的成绩是：{found['score']}")
        else:
            print("未找到该学生。")
    
    # 4. 计算平均分
    elif choice == "4":
        if len(students) == 0:
            print("暂无学生信息，无法计算平均分。")
        else:
            total = 0
            for stu in students:
                total = total + stu["score"]
            avg = total / len(students)
            print(f"共有{len(students)}名学生，平均分是：{avg:.2f}")
    
    # 5. 退出
    elif choice == "5":
        print("感谢使用，再见！")
        break
    
    # 输入无效
    else:
        print("无效选择，请重新输入。")