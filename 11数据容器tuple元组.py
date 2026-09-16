#元组--tuple,不可改变内容
#基础组包
# a = (3,4,5,32,4,3423,4,234,23)
# b =3,435,345,34,5,345,34,53,4,345,3,76,5,2
# c =(3,)     #想将单个元素变为元组在其后面加上逗号
# print(a)
# print(b)
# print(c)

#解包--变量数量=容器内元素数量
# a = (3,4,5,32)
# c,v,x,n = a
# print(c)
# print(n,c)

#扩展解包--*收集剩余元素组成新的列表
# b =(3,435,345,34,5,345,34,53,4,345,3,76,5,2)
# g,*m,o=b
# print(g,m,o)
# *p,l=b
# print(p,l)

#三个变量交换值
# a=10
# b=20
# c=30
# a,b,c=c,a,b
# print(a,b,c)

"""
学号	    姓名	    语文	    数学	    英语
S001	王林	    85	    92	    78
S002	李慕婉	92	    88	    95
S003	十三	    78	    85	    82
S004	曾牛	    88	    79	    91
S005	周轶	    95	    96	    89
S006	王卓	    76	    82	    77
S007	红蝶	    89	    91	    94
S008	徐立国	75	    69	    82
S009	许木	    86	    89	    98
S010	遁天	    66	    59	    72
将上述成绩单
1.计算每个学生的总分,平均分,输出出来
2.各科成绩的最低分和最高分以及平均分输出
3.查找优秀学生(平均分)>90,差生(平均分)<60
"""
students =(
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72),
)
# #1.计算每个学生的总分,平均分,输出出来   avg:.1f---保留小数点后一位并float值
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式一：
# for s in students:#将元素遍历出来
#     total = s[2] + s[3] + s[4]#总分=各科相加
#     avg = total / 3#平均分
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

#方式2：元组解包
for id,name,c,m,e in students:#将元素遍历出来
    total = c+m+e#总分=各科相加
    avg = total / 3#平均分
    print(f"{id} \t {name} \t {c} \t {m} \t {e} \t {total} \t {avg:.1f}")

# #2.各科成绩的最低分和最高分以及平均分输出
chinese =[s[2]for s in students ]
math =[s[3]for s in students ]
english =[s[4]for s in students ]
print(f"语文最低分: {min(chinese)} ,语文最高分: {max(chinese)} ,平均分: {sum(chinese)/len(chinese)}")
print(f"数学最低分: {min(math)} ,数学最高分: {max(math)} ,平均分: {sum(math)/len(math)}")
print(f"英语最低分: {min(english)} ,英语最高分: {max(english)} ,平均分: {sum(english)/len(english)}")
# #3.查找优秀学生(平均分)>90,差生(平均分)=<60
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"优秀学生名单:{s[1]}")
#     elif avg <= 60:
#         print(f"差生学生名单:{s[1]}")
#方式二:
for id,name,c,m,e in students:
    total = c + m + e
    avg = total / 3
    if avg > 90:
        print(f"优秀学生名单:{name}")
    elif avg <= 60:
        print(f"差生学生名单:{nema}")


# # 1.计算每个学生的总分,平均分,输出出来
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分\t\t")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]}\t {total} \t {avg:.1f} ")
# 
# # 2.各科成绩的最低分和最高分以及平均分输出
# chinese = [s[2]for i in  students]
# math = [s[3]for i in  students]
# english = [s[4]for i in  students]
# for subject, scores in [("语文", chinese), ("数学", math), ("英语", english)]:
#     avg_score = sum(scores) / len(scores)
#     print(f"{subject}最低分: {min(scores)} , 最高分: {max(scores)} , 平均分: {avg_score:.1f}")
# # for s in [("语文",c),("数学",m),("英语",e)]:
# #     avg = sum(s)/len(s)
# #     print(f"min{}")
# # 3.查找优秀学生(平均分)>90,差生(平均分)<60
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"优秀学生名单:{s[1]}")
#     elif avg <= 60:
#         print(f"差生学生名单:{s[1]}")



