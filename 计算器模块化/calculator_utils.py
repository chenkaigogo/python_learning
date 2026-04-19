# calculator_utils.py

def get_number(prompt):
    """从用户输入获取一个浮点数，如果输入无效则返回 None"""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return None
        try:
            return float(user_input)
        except ValueError:
            print("错误：请输入有效的数字！")
        

def get_operator():
    """获取运算符，返回运算符字符串或 None（退出）"""
    while True:
        op = input("请输入运算符（+ - * /）：")
        if op.lower() == 'q':
            return None
        if op in ('+', '-', '*', '/'):
            return op
        print("错误：不支持的运算符！")