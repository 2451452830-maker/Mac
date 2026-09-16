# #for遍历输入的字符串
# q =input("请输入字符串")
# for m in q :
#     print(f"值为",{m})
# else:
#     print("ok")


#案例计算1-100奇数之和
# total =0
# for i  in range(1,101):
#     if i % 2 == 1 :
#         total += i
# print("和为", total)
#计算100-800之间4倍数的数字和
# total = 0
# for i in range(100,800):
#     if i % 4 == 0:
#         total += i
# print("值为",total)


# total = 0
# for i in range(100,801,4):
#
#         total += i
# print("值为",total)


# total =sum(range(100,801,4))
# print(total)


# total = 0
# n =int(input("请输入一个整数"))
# for i in range(0,n+1,3):
#     total += i
# print(total)

# total  =0           #循环次数
# num = int(input("请输入一个数"))
# for i in range(1,num+1):
#     total += i ** 2
# print(f"平方和为{total}")

#打印一个长m宽n的长方形
# m =int(input("长:"))
# n =int(input("宽:"))
# for i in range (m):
#     for i in range (n):
#         print("*",end=" ")
#     print()

#输入一个整数 n（1 <= n <= 9），用 * 打印一个三角形图案：第一行 1 个星号，第二行 2 个星号，……，第 n 行 n 个星号。
# n = int(input("输入一个整数"))
# for i in range(1,n+1):
#     for q in range(i):
#         print("*",end=" ")
#     print()

# #输入一个整数 n（n >= 1），在 1 到 n 之间，找出第一个能被 7 整除的数，并输出。如果不存在，则输出“没有找到”。
# n = int(input("输入一个整数"))
# for i in range(1,n+1):
#     if i % 7 == 0:
#         print(f"第一个能被7整除的是{i}")
#         break
# else:
#     print("not")
#倒三角形
# n = int(input("输入一个整数"))
# for i in range(n,0,-1):
#     for q in range(i):
#         print("*",end="\t")
#     print()

# for q in range(30,20,-1):
#     print(q)

#九九乘法表
# for i in range(1,10):
#     for q in range(1,i+1):
#         print(f"{i} * {q} = {i * q}", end="\t")
#     print()


# while True:
#     account = input("账号")
#     password = input("密码")
#     if account ==""  or password =="":
#         print("输入的值不能为空,重新输入")
#         continue
#     if account == "123" and password =="000":
#         print("成功")
#         break
#     elif account == "321" and password =="111":
#         print("成功")
#         break
#     elif account == "222" and password=="333":
#         print("成功")
#         break
#     else:
#         print ("账号或者密码错误")



"""
    1.系统随机生成一个随机数
    2.用户根据提示猜数字，并将所猜的数字输入系统
    3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
    4.如果猜对，系统自动退出，游戏结束
"""
# import random
# random_a = random.randint(1,100)
# a = int(input("请输入一个数"))
# while True:
#     if a < random_a :
#         print("小了")
#     elif a > random_a :
#         print("大了")
#     else:
#         if a == random_a:
#         print("猜对了")
#     break

# import random
# random_a = random.randint(1,100)
# while True:
#     a = int(input("请输入一个数："))
#
#     if a < random_a:
#         print("小了")
#     elif a > random_a:
#         print("大了")
#     else:
#         print("猜对了")
#         break


