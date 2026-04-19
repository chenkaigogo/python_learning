# 用函数重构计算器
#定义四个加减乘除函数
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误：除数不能为0"
    else:
        return x / y

# 计算器主程序
print("简单计算器")
num1 = float(input("请输入第一个数字："))
op = input("请输入运算符（+ - * /）：")
num2 = float(input("请输入第二个数字："))

if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":
    result = divide(num1, num2)
else:
    result = "不支持的运算符"

print(f"结果：{result}")