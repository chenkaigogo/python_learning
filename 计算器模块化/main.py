# main.py
import calculator_operations as ops
import calculator_utils as utils

def calculate():
    print("===== 计算器 =====")
    print("输入 q 可随时退出程序")
    
    while True:
        # 获取第一个数字
        num1 = utils.get_number("\n请输入第一个数字：")
        if num1 is None:
            print("再见！")
            break
        
        # 获取运算符
        op = utils.get_operator()
        if op is None:
            print("再见！")
            break
        
        # 获取第二个数字
        num2 = utils.get_number("请输入第二个数字：")
        if num2 is None:
            print("再见！")
            break
        
        # 执行运算
        try:
            if op == '+':
                result = ops.add(num1, num2)
            elif op == '-':
                result = ops.subtract(num1, num2)
            elif op == '*':
                result = ops.multiply(num1, num2)
            elif op == '/':
                result = ops.divide(num1, num2)
        except ZeroDivisionError as e:
            print(f"错误：{e}")
            continue
        else:
            print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    calculate()