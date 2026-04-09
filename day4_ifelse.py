# 改进版计算器
# 用户输入两个数字和运算符，输出计算结果

# 输入
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符（+ - * /）：")
num2 = float(input("请输入第二个数字："))

# 判断并计算
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if  num2 == 0:
        print("错误：除数不能为0！")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result,2)}")
else:
    print("不支持的运算符，请使用 + - * /")