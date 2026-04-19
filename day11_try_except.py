# 健壮的计算器（完整异常处理）

def calculate():
    while True:
        print("\n===== 计算器 =====")
        print("输入 q 退出程序")
        
        # 输入第一个数字
        num1_input = input("请输入第一个数字：")
        if num1_input.lower() == 'q':
            print("再见！")
            break
        
        # 输入运算符
        op = input("请输入运算符（+ - * /）：")
        if op.lower() == 'q':
            print("再见！")
            break
        
        # 输入第二个数字
        num2_input = input("请输入第二个数字：")
        if num2_input.lower() == 'q':
            print("再见！")
            break
        
        # 尝试转换数字和计算
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("错误：请输入有效的数字！")
            continue
        
        # 根据运算符计算
        try:
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("除数不能为0")
                result = num1 / num2
            else:
                raise ValueError("不支持的运算符")
        except ZeroDivisionError as e:
            print(f"错误：{e}")
            continue
        except ValueError as e:
            print(f"错误：{e}")
            continue
        else:
            print(f"{num1} {op} {num2} = {result}")
        finally:
            print("本次计算结束\n")

# 运行计算器
if __name__ == "__main__":
    calculate()