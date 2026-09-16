from typing import NamedTuple

print(type(10))#type()获取指定的字面量或变量的类型
print(type("nihao"))
print(type(2.1))
print(type(True))
print(type(False))
print(type(None))

a = 0.9
print(a)
print(type(a))

#isinstance(数据,类型)结果为bool值,判断数据是否为指定的类型,如果是:T  否则:F
print(isinstance(a, int))
print(isinstance(a, bool))
print(isinstance(a, float))


#字符串分单引号 双引号 三引号(多行字符串),前两种不能进行换行
print('nihao')
print("nihao")
print("""
nihao:
    buhao
    diandoubuhao
""")
#转义字符: \'表单引号 \"表双引号 \n换行 \t制表符
print('is\'你好')
print("is\"你好")
print("is\n你好")
print("is\n\t你好")

#字符串拼接:+号将两个字符串链接起来
a ="nihao"
b ="no"
print(a+b)
print(b+a)
#将int类型转换为字符串str
name = "钱风"
age =20
hobby ="唱跳"
print(name+str(age)+hobby)

#字符串的格式化:占位符%s
name = "钱风"
age =20
hobby ="唱跳"
print("%s,%s,%s"%(name,age,hobby))

#第二种:  f"..{}.."  常用
name = "钱风"
age =20
hobby ="唱跳"
print(f"{name},{age},{hobby}")