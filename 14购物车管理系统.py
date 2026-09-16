# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车
"""
首先看需求点,实现商品的 增 删改 查 ,用字典结构来存储商品数据,分5个点
用到的东西:input for 有循环不知道次数(while) break dict 构建外观三引号多字符串
1.添加:dict1[""]=value1,但是名称不会改变,价格数量这些都可以改变,这说明名称不可变,(字典)数量和价格可以变(列表)
2.修改:dict1[""]=value1(覆盖前面所添加的),剩下的和上述一样
3.删除:del dict1[""],没有的话就返回输入错误请重新来
4.查询:dict1[""]
5.退出:跳出循环break
结构:shopping_cart={商品名称:苹果{商品价格:5,商品数量:5}{栗子.......}}
"""
#构建外观
shopping_cart = {}
print("欢迎来到购物车系统")
mum = """
################欢迎来到购物车系统################
#               1.添加购物车商品                #
#               2.修改购物车商品                #
#               3.删除购物车商品                #
#               4.查寻购物车商品                #
#               5.退出购物车系统                #
##############################################
"""
print(mum)
#添加购物车dict[""]=value1
while True:
    choice = input("请输入执行的操作:1-5")

    match choice:
        case "1":#添加购物车dict1[""]=value1
            goods_name = input("请输入修改商品的名称")
            goods_price = float(input("请输入修改的价格"))
            goods_num = int(input("请输入修改的数量"))

            #商品是否在系统里面if in
            if  goods_name in shopping_cart:
                print("商品存在,输入未存在的商品名称")
            else:
                shopping_cart[goods_name]={"price" : goods_price, "num": goods_num}
                print("商品添加完毕")
        case "2":#修改
            goods_name = input("请输入修改商品的名称")
            goods_price = float(input("请输入修改的价格"))
            goods_num = int(input("请输入修改的数量"))
            if  goods_name not in shopping_cart:
                print("商品不存在,输入存在的商品名称")
                continue
            else:
                shopping_cart[goods_name]={"price" : goods_price, "num": goods_num}
                print("商品修改完毕")

        case "3":#删除del dict[""]
            goods_name = input("请输入删除商品的名称")
            if  goods_name not in shopping_cart:
                print("商品不存在,输入存在的商品名称")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")

        case "4":#查询dict [""]
            goods_name = input("请输入查询商品的名称")
            if goods_name  in shopping_cart:
                for goods_name in shopping_cart.keys():
                    goods_info = shopping_cart[goods_name]
                    print(f"商品名称:{goods_name},商品单价:{goods_info['price']},商品数量:{goods_info['num']}")
            else:
                print("该商品不在库里")

        case "5":#退出
            print("拜拜")
            break
        case _:#其他情况
            print("非法操作,请重新输入")



