#猜数字游戏
import random

# 生成随机数
secret = random.randint(1, 100)
guess_count = 0

print("===== 猜数字游戏 =====")
print("我已经想好了一个1-100之间的整数。")
print("输入0可以随时退出游戏。\n")

while True:
    user_input = input("请输入你猜的数字：")
    
    # 检查是否输入0退出
    if user_input == "0":
        print("游戏结束，下次再来！")
        break
    
    # 检查输入是否为数字
    if not user_input.isdigit():
        print("无效输入，请输入一个整数！")
        continue
    #将字符串转为整数
    guess = int(user_input)
    
    # 检查范围
    if guess < 1 or guess > 100:
        print("请输入1-100之间的数字！")
        continue
    #计数猜了多少次
    guess_count += 1
    # 比较
    if guess < secret:
        print("太小了，再大一点。")
    elif guess > secret:
        print("太大了，再小一点。")
    else:
        print(f"恭喜你！猜中了！数字就是{secret}。")
        print(f"你总共猜了{guess_count}次。")
        break