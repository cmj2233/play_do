import random

# 随机生成1~100之间数字
answer = random.randint(1, 100)
print("====猜数字小游戏====")
print("我已经想好了1-100之间一个数字，快来猜猜！")

while True:
    try:
        guess = int(input("请输入你猜的数字："))
        if guess > answer:
            print("猜大了，再试试！")
        elif guess < answer:
            print("猜小了，再试试！")
        else:
            print(f"恭喜！猜对啦，数字就是{answer}")
            break
    except ValueError:
        print("请输入有效的整数！")
