# #算术运算符:加 减 乘 除 整除 取余/求模 幂指数
# print(10+4)
# print(10-4)
# print(10*4)
# print(10/4)
# print(10//4)
# print(10%4)
# print(10**4)
#
# #算数运算符的优先级:幂指数---乘,除,整除,取余---加,减
# print("此算数的结果",0.9*6-76+98//2)

#案例输入两个数x和y,分别输出x+y和x-y的值xy,x/y,x%y
#float(..)---将其他类型转化为浮点数
# x =float(input("请输入"))
# y =float(input("请输入"))
# print("和为",x+y)
# #精度损失:由于计算机底层是二进制,二进制无法精确所以小鼠所以涉及浮点数运算可能会损失精度
# print("余为",x-y)
# print("积为",x*y)
# print("商为",x/y)
# print(x//y)
# print(x%y)

#案例输入三个整数的平均数
# x=int(input("请输入"))
# y=int(input("请输入"))
# z=int(input("请输入"))
# print("平均数为",(x+y+z)//3)

#求梯形的面积 上底为q 下底为w 高为r
# q=int(input("上底为"))
# w=int(input("下底为"))
# r=int(input("高为"))
# print("梯形的面积为",(q+w)*r//2)

#身体质量IBM(体重除身高**2)
# q=float(input("体重"))
# w=float(input("身高"))
# print(q/w**2)

#赋值运算:= += -= *= /= //= %= **=
# num = 20
#
# num +=10
# print('和',num)
# num -=10
# print(num)
# num *=3
# print(num)
# num /=3
# print(num)
# num//=2
# print(num)
# num %=3
# print(num)
# num **=3
# print(num)

#比较运算符:== != > >= < <=
# a =2**3
# b =90/3
# print('结果为',a==b)
# print('结果为',a!=b)
# print('结果为',a<b)
# print('结果为',a<=b)
# print('结果为',a>b)
# print('结果为',a>=b)

#逻辑运算符:and or not
# a =int(input("输入一个整数"))
# print(4 <= a <=15)
# print(a <=1 or a>= 9)

