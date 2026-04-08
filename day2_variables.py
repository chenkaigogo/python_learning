#用户输入随机两个数，输出和、减、积、商
#定义变量
a = input("请输入第一个数：")
b = input("请输入第二个数：")
a = int(a)
b = int(b)

ab1 = a + b
ab2 = a - b
ab3 = a * b
ab4 = round(a / b,2)

print("两数和为：",ab1)
print("两数减为：",ab2)
print("两数积为：",ab3)
print("两数商为：",ab4)