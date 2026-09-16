# #字典dict定义:以键值对(key:value)来存储数据,特点:key是不可变类型:str,tuple,int,float,   key不能重复(重复的话,后面的值会覆盖前面的)
# dict1 = {"a":123 ,"b":5678 ,"c":237468}
# print(dict1)
# #访问
# print(dict1["c"],dict1["a"])
"""
添加	    字典名称[key]= value	    往指定字典中添加key-value键值对	                      dict["涛哥"]=688
删除	    字典名称.pop(key)	        删除字典中指定的key，并返回该key对应的value	          score = dictl.pop("涛哥
	    del字典名称[key]	        删除字典中指定的键值对	                                del dicti["涛哥"]
修改	    字典名称[key]=value	    修改字典中指定的key对应的值	                            dicti["小智"] = 658
查询	    字典名称[key]	            根据key获取value	                                    dict["涛哥"]
	    字典名称.get(key)	        根据key获取value	                                    dictl.get("涛哥")
	    字典名称.keys()	        获取所有的key	                                        dictl.keys()
	    字典名称.values()	        获取所有的value	                                    dictl.values()
	    字典名称.items()	        获取所有的key-value键值对	                            dictl.items()
"""
dict1 = {"a":123 ,"b":5678 ,"c":237468}
print(dict1)
#添加
dict1["h"] = 900
print(dict1)
#修改
dict1["h"]=800
print(dict)
#查询
print(dict1["c"])
print(dict1.get("c"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#删除
score = dict1.pop("c")
print(score)
print(dict1)
del dict1["h"]
print(dict1)
#遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for items in dict1.items():
    print(f"{items[0]} : {items[1]}")

for k,v in dict1.items():
        print(f"{k} : {v}")