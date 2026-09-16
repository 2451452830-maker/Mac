#函数def定义:
"""
格式是def 函数名  (参数列表):
     函数体
    return 返回值
"""
# def num_money():#创建函数
#     print("usidgfiaiudahusdiasd")
#     print("1234567890987653456")
#     print("xhcgvsoduifyhqiwodsanfio")
#     print("啊是对购房苏很大功夫i是对hi四哦好的覅哦是否")
#
# num_money()#调用函数
# num_money()
# num_money()

"""
# 函数的参数与返回值--定义多个参数,参数织之间有逗号隔开,return只会返回值,没有打印的功能,要结合print来
def cir_area(r):
    area = 3.14 * r * r
    return area
#调用函数
cir = cir_area(5)
r代表的是(形式参数):函数定义时括号里面的参数,只能在函数内使用(局部参数)
5代表的是(实际参数):函数在调用是输入的参数
"""
#计算圆面积
def cir_area(r):
    """
    根据圆的半径来计算圆的面积
    :param r: 半径
    :return: 圆的面积
    """
    area = 3.14 * r * r
    return area
help(cir_area)
print("圆的面积:",cir_area(5))
#计算长方形面积,周长---返回值有多个,他们之间用逗号分割---多个返回值会封装到元组里面
# def rectangle_area_perimeter(l,w):
#     return l * w,2 * l + 2 * w
# print(rectangle_area_perimeter(5,5))
#计算圆面积和周长
# def cir_area_len(r):
#     return round(3.14 * r * r,1),round(3.14 * 2 * r,1)
# print(cir_area_len(5))#组包
# area,len = cir_area_len(5)#解包
# print(area)
# print(len)







