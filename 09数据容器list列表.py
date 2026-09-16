"""列表常见方法:
append()        在列表尾部加一个元素                                s.append(10086)
insert()        在指定索引之前,插入元素                          s.insert(0,92)
remove()        删除列表第一个匹配到的值                          s.remove()
pop()           删除指定索引位置的元素(如果未指定索引,就删最后一个)    s.pop()/ s.pop()
sort()          对列表进行排序(同一数据类型)                      s.sort()
reverse()       反转列表元素                                   s.reverse()
count()          统计某个元素出现几次                            s. count()
index()         查找某个元素第一次出现的索引                      s.index()
extend()        把另一个列表的一堆元素加进来                          s.extend()
clear()         清空列表                                       s.clear()
copy()          复制列表
"""
from unittest.util import sorted_list_difference

# #用户输入10个数字,存入列表,并排序,输出最小和最大和平均值
# s_list = []
# for i in range(10):
#     s = int(input("输入数字"))#输入数字
#     s_list.append(s)
# print("数字列表",s_list)
#
# #排序
# s_list .sort()
# print("排序后",s_list)
# #min,max,sum
# print("最小值",s_list[0])
# print("最大值",s_list[-1])
# #sum()求和,len()获取元素的个数
# print("平均值",sum(s_list)/len(s_list))

# #合并列表,去重,排序,输出最大最小平均
# s_list1=[1,2,3,4,5,6,7,8,9,10]
# s_list2=[1,32,57,89,43,67,90,3,6,9]
# #合并
# s_list=s_list1+s_list2
# print(s_list)
"""
去重
# new_list=[]
# for s in s_list:
#     if s not in new_list:
#         new_list.append(s)
# new_list.sort()
"""
#print(new_list)#去重后的
# print("最大值",new_list[-1])
# print("最小值",new_list[0])
# print("平均值",sum(new_list)/len(new_list))

#列表的推导式--按照一定规律生成一个列表
#生成1-20的数字的平方
#生成1-20---range(1,21)
"""
[要插入的值 for i in 序列/列表]
s_list = [i**2 for i in range(1,21)]
print(s_list)
"""
#从一个列表中提取所有的奇数,计算平方,生成新的列表--[要插入的值 for i in 序列/列表 if 条件]
# s_list =[1,2,4,7,8,5,3,90,89,77,66]
# s1_list= [i**2 for i in s_list if i%2==1]
# s1_list.sort()
# print(s1_list)
# 并对合并后的列表进行元素的去重，然后排好序(升序)后输出到控制台
"""
list1 = ['M', 'A', 'C', 'E', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'F', 'G']
list3 = ['W', 'A', 'D']
s_list =list1 + list2 + list3
print(s_list)
new_list =[]
for i in s_list :
     if i not in new_list :
        new_list.append(i)
new_list.sort()
print(new_list)
"""



# 2.将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# 将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
# # 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
#推导式--for i in
"""list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
s_list =[i**2 for i in list1 if i%3==0 or i%5==0 ]
s_list.reverse()
print(s_list)
"""

# 3.将如下列表中的正数提取出来，封装为一个新的列表。
# #将如下列表中的正数提取出来，封装为一个新的列表。list1 = [11, 2, 31, 4, -5, 15, 17, 28,
# # 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list1 = [11, 2, 31, 4, -5, 15, 17, 28,49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
new_list =[ i for i in list1 if i>0 ]
new_list.sort()
print(new_list)

