#字符串不可改变
# find()	        在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1	            s.find('Python')
# count()	        统计子串在字符串中出现的次数	                                    s.count('H')
# upper()	        将字符串中的所有字母转换为大写	                                s.upper()
# lower()	        将字符串中的所有字母转换为小写	                                s.lower()
# split()	        将字符串按指定分隔符分割成列表	                                s.split()
# strip()	        去除字符串两端的空白字符或指定字符	                                s.strip() / s.strip('*')
# replace()	        将字符串中的指定子串替换为新的子串	                                s.replace('H','C')
# startswith()	    检查字符串是否以指定子串开头，返回布尔值	                        s.startswith('P')
# endswith()        检查字符串是否以指定子串结尾，返回布尔值                            s.endswith('P')

# #检验输入的邮箱是否正确
# s =input("输入邮箱账号")
# q =input("输入密码")
# if s.count("@")==1 and s.count(".")>=1:
#     print("登录成功")
# else:
#     print("登陆失败")

#输入一个字符串判断是否为回文
# s = input("输入字符串")
# if s == s[::-1]:
#     print("对了")
# else:
#     print("错了")

# #将用户输入的10个字符串,反转并大写,记录到列表中,将内容遍历出来
# num =[]                         #建立新的列表,等待返回值
# for i in range(10):             #循环10次
#     s = input("输入10个字符串")
#     new_s =s[::-1].upper()      #先反转再大写
#     num.append(new_s)           #添加到新的列表
#     print(new_s)
# for i in num :                  #遍历出来
#     print(i)
