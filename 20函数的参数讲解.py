# ————————————————————————————————————————————函数的的传参方式————————————————————————————————————————————————
"""
def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名：{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
#位置参数——实参的顺序和形参的位置一一对应。数量也是一致————优点：简洁  缺点：可读性差，容易出错，维护难
stu = reg_stu("丽丽",28,"女", "上海")
print(stu)
#关键字传参——没有顺序关系————优点：可读性强，容易维护和扩展   缺点：代码繁琐
stu = reg_stu(name = "张三",age = 22,gender = "男",city = "成都")
print(stu)
#位置参数加关键字参数——位置参数在前，关键字参数在后
stu = reg_stu("赵四",28,gender = "男",city = "云南")
print(stu)
"""
from dataclasses import dataclass

# ————————————————————————————————————————————函数的的默认参数————————————————————————————————————————————————
#默认参数也叫缺省参数，在定义函数的时候，为参数附加默认值，调用是可以不传递有默认值的参数
#默认参数必须要放在没有默认值参数之前，可以定义多个默认参数
#函数调用时，为默认值参数传递了值，会修改以前默认的值，没有就直接使用默认值
"""
def reg_stu(name,age,gender,city="北京"):
    print(f"注册成功，姓名：{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
stu = reg_stu("李五",18,"男")
print(stu)
stu = reg_stu("李五",18,"男","成都")
print(stu)
stu = reg_stu("李五",18,city="成都")
print(stu)
"""

# ————————————————————————————————————————————函数的的不定长参数：可变参数————————————————————————————————————————————————
#基于位置参数的---*变量名，*后面不是关键字，可以使用任意合法的变量名。
# 传递的所有匹配的位置参数都会被*data收集封装成一个元组（解包和组包），并不会封装关键字参数
# def data_st(*args):
#     max_st =max(args)
#     min_st =min(args)
#     avg =round(sum(args)/len(args),1)
#     return max_st,min_st,avg
# data = data_st(45,78,34,89,22,90,57,80,98,100)
# print(data)
#基于关键字参数的--**变量名，*后面不是关键字，可以使用任意合法的变量名
#参数是以“键=值”形式传递的关键字参数，这些都会被kwargs接收，封装为一个字典类型。
"""
def data_st(*args,**kwargs):
    max_st =max(args)
    min_st =min(args)
    avg =sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg =sum(args)/len(args)
    if kwargs.get("print") :
        print(f"最大值:{max_st},最小值：{min_st},平均值：{avg}")
    return max_st,min_st,avg
data = data_st(45,78,34,89,22,90,99.88,57,80,98,100,round=4,print=True)
print(data)


def data_st(*args, **kwargs):
    # 1. 算最高分最低分
    max_st = max(args)
    min_st = min(args)

    # 2. 从 kwargs 字典里拿配置，加个默认值：如果没传，默认保留1位小数
    decimal = kwargs.get("decimal", 1)
    # 默认不打印
    do_print = kwargs.get("do_print", False)

    # 3. 真正用上用户传的配置！
    avg = round(sum(args) / len(args), decimal)

    # 4. 如果调用者开了打印开关，就打印
    if do_print:
        print(f"最大值:{max_st},最小值：{min_st},平均值：{avg}")

    # 5. 返回结果
    return max_st, min_st, avg


# 调用测试：我传了 decimal=2，所以结果保留2位；传了 do_print=True，所以会打印
data = data_st(45, 78, 34, 89, 22, 90, 99.88, 57, 80, 98, 100, decimal=2, do_print=True)
print("函数的返回值:", data)
"""

# ————————————————————————————————————————————函数的参数类型————————————————————————————————————————————————
#普通参数：数字，布尔，字典，字符串，列表，元组，集合。  特殊参数：函数
"""
def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def mul (x,y):
    return x*y
def calc (x,y,up):
    return up(x,y)
num = calc(5,7,add)
print(num)
"""

# ————————————————————————————————————————————函数的匿名函数————————————————————————————————————————————————
#匿名函数：没有名称的函数，需lambda来表达声明函数，简化简单函数的编写，他可以返回结果也可以不返回
#打印分割线
# nn =lambda :print("------------")
# nn()
# #计算两个和
# num = lambda x,y:x+y
# print(num(90,80))
#完成列表的排序，按照每个元素的字符个数，从小到大，从大到小排序
# lambda 是什么：就是一个“用完就扔的一次性小函数”。省得你为了一个简单的排序，专门去写个 def。
# key 是什么：告诉 sort()，按什么规则排。默认是按字母/数字大小，加了 key 就能按长度、按字典里的某个字段排。
# lambda i: len(i) 怎么读：对于列表里的每个元素 i，用它的长度 len(i) 作为排序的依据。
# reverse=True 是什么：加了这个就是从大到小（降序），不加就是从小到大（升序）。
"""data_list =["sgfdf","dugudnvi","yrmlasgd","hj","diqn"]
data_list.sort(key=lambda i:len(i),reverse=True )
print(data_list)
"""
# #############递归
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n-1)
# num = jc(27)
# print(num)

#——————————————————————————————————函数的案例————————————————————————————————————————————————
# 定义一个函数，计算订单总金额。输入包括：商品信息（商品名、价格、数量），优惠（优惠券、积分抵扣），运费。
# 具体规则：优惠券：商品金额满5000才可使用，且金额不能超过商品总价。
# 积分抵扣：商品总金额满5000才可使用，100积分抵1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def calculate_order_total(goods_list, coupon, points, shipping_fee):
    """
    计算订单总金额
    :param goods_list: 商品列表，例如 [{"name": "手机", "price": 4000, "quantity": 1}]
    :param coupon: 优惠券金额
    :param points: 积分数量
    :param shipping_fee: 运费
    :return: 最终订单总金额
    """
    # 1. 计算商品初始总金额
    goods_total = 0
    for item in goods_list:
        goods_total += item["price"] * item["quantity"]

    print(f"商品原价总金额: {goods_total} 元")

    # 2. 计算优惠券抵扣（规则：满5000可用，且不能超过商品总价）
    coupon_deduction = 0
    if goods_total >= 5000 and coupon <= goods_total:
        coupon_deduction = coupon
        print(f"优惠券抵扣: {coupon_deduction} 元")
    else:
        print("未满足优惠券使用条件")

    # 3. 计算积分抵扣（规则：满5000可用，100积分抵1元，只能整百抵扣，且不超过商品总价）
    points_deduction = 0
    if goods_total >= 5000:
        # 只能整百抵扣：先算出可用积分，再折算成金额
        usable_points = (points // 100) * 100
        points_deduction = usable_points // 100  # 100积分抵1元

        # 抵扣金额不能超过商品总价（注意这里通常用商品原价做上限判断）
        if points_deduction > goods_total:
            points_deduction = goods_total
        print(f"积分抵扣: {points_deduction} 元 (消耗 {usable_points} 积分)")
    else:
        print("未满足积分抵扣条件")

    # 4. 计算最终金额
    final_amount = goods_total - coupon_deduction - points_deduction + shipping_fee

    # 容错保护：金额不能为负数
    if final_amount < 0:
        final_amount = 0

    return final_amount
# ---------------- 测试运行 ----------------
my_goods = [
    {"name": "笔记本电脑", "price": 4500, "quantity": 1},
    {"name": "鼠标", "price": 200, "quantity": 2}
]
# 商品总价: 4500 + 400 = 4900（不满5000，无法使用优惠和积分）
# 修改测试数据试试满5000的情况
my_goods2 = [
    {"name": "笔记本电脑", "price": 6000, "quantity": 1},
    {"name": "鼠标", "price": 200, "quantity": 1}
]
final_price = calculate_order_total(my_goods2, coupon=500, points=15050, shipping_fee=20)
print(f"最终订单总金额: {final_price} 元")