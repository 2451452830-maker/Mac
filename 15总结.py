"""
数据类型	    有序性	     重复元素规则	      可变性	    索引访问	    切片操作	          典型使用场景
字符串（str）	有序	         允许重复	          不可变	    支持	        支持	            文本处理、字符序列操作
列表（list）	有序	         允许重复	          可变	    支持	        支持	            有序可重复数据集合
元组（tuple）	有序	         允许重复	          不可变	    支持	        支持	            固定数据记录、常量集合
集合（set）	无序	         不允许重复	      可变	    不支持	    不支持	        数据去重、集合逻辑运算
字典（dict）	有序          key不允许重复	 可变	    不支持	    不支持	         键值对映射、结构化数据存储
                         value 允许重复
# """
# shopping_cart = {}
# print("欢迎来到购物车系统")
# mum = """
# ################欢迎来到购物车系统################
# #               1.添加购物车商品                #
# #               2.修改购物车商品                #
# #               3.删除购物车商品                #
# #               4.查寻购物车商品                #
# #               5.退出购物车系统                #
# ##############################################
# """
# print(mum)
# while True:
#     choice = input("请输入执行的操作:1-5")
#     match choice:
#         case "1":#添加购物车dict1[""]=value1
#             goods_name = input("请输入修改商品的名称")
#             goods_price = float(input("请输入修改的价格"))
#             goods_num = int(input("请输入修改的数量"))
#             if  goods_name in shopping_cart:
#                 print("商品存在,输入未存在的商品名称")
#             else:
#                 shopping_cart[goods_name]={"price" : goods_price, "num": goods_num}
#                 print("商品添加完毕")
#         case "2":#修改
#             goods_name = input("请输入修改商品的名称")
#             goods_price = float(input("请输入修改的价格"))
#             goods_num = int(input("请输入修改的数量"))
#             if  goods_name not in shopping_cart:
#                 print("商品不存在,输入存在的商品名称")
#                 continue
#             else:
#                 shopping_cart[goods_name]={"price" : goods_price, "num": goods_num}
#                 print("商品修改完毕")
#         case "3":#删除del dict[""]
#             goods_name = input("请输入删除商品的名称")
#             if  goods_name not in shopping_cart:
#                 print("商品不存在,输入存在的商品名称")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕")
#         case "4":#查询dict [""]
#             goods_name = input("请输入查询商品的名称")
#             if goods_name  in shopping_cart:
#                 for goods_name in shopping_cart.keys():
#                     goods_info = shopping_cart[goods_name]
#                     print(f"商品名称:{goods_name},商品单价:{goods_info['price']},商品数量:{goods_info['num']}")
#             else:
#                 print("该商品不在库里")
#         case "5":#退出
#             print("拜拜")
#             break
#         case _:#其他情况
#             print("非法操作,请重新输入")
def get_goods_info():
    name = input("请输入修改商品的名称")
    price = float(input("请输入修改的价格"))
    num = int(input("请输入修改的数量"))
    return name, price, num
print("添加商品成功,商品为:",get_goods_info())

