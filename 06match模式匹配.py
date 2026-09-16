# #每周的每一天都有事情做
# day = input("请输入星期几:")
#
# match day:
#     case "1":
#         print('周一:开会')
#     case "2":
#         print('周2:项目')
#     case "3":
#         print('周3:总结')
#     case "4":
#         print('周4:排查')
#     case "5":
#         print('周5:下周安排')
#     case "6"|"7":
#         print('周末:休息')
#     case _:
#         print("错误")

#基于match来建立一个计算器
num1 =float(input("请输入一个数:"))
num2 =float(input("请输入一个数:"))
oper =input("请输入运算符:")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1+num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2!=0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case "//" if num2!=0:
        print(f"{num1} // {num2} = {num1 // num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    case _:
        print("输入错误")
