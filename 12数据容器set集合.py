# #定义:无序,可改,不可重复
# s ={0,102301,4,34,435,6,45}
# s1 =set()#空集合
# print(s1 , s)
"""
add                 添加元素到集合中           s.add("t")
remove              删除指定元素               s.remove("t") 
pop                 随机删除元素               s.pop()
clear               清空元素                  s.clear()
difference          两个元素之间的补集          s.difference(s1)
union               两个元素之间的并集          s.union(s1)
intersection        两个元素之间的交集          s.intersection(s1)
"""
#add
# s3 = {1,4,6,34,5,75,6,2,45,2,34,26}
# s4 = {1,4,7,90,5,2}
# s3.add(90)
# print(s3)

# #remove
# s3.remove(26)
# print(s3)

# #pop
# s3.pop()
# print(s3)

# #clear
# s3.clear()
# print(s3)

# #difference补集
# s3.difference(s4)
# s4.difference(s3)
# print(s3)
# print(s4)

# #union并集
# print(s3.difference(s4))

# #intersection交集
# print(s4.intersection(s3))


# #选修足球学生名单
football_set = {'王林', '曾牛', '徐立国', '遁天', '天运子', '韩立', '厉飞雨', '乌丑', '紫灵'}
# #选修篮球学生名单
basketball_set = {'张铁', '墨居仁', '王林', '姜老道', '曾牛', '王蝉', '韩立', '天运子', '李化元', '厉飞雨', '云露'}
# #选修法语学生名单
french_set = {'许木', '王卓', '十三', '虎咆', '姜老道', '天运子', '红蝶', '厉飞雨', '韩立', '曾牛'}
# #选修艺术学生名单
art_set = {'遁天', '天运子', '韩立', '虎咆', '姜老道', '紫灵'}

# 1.找出同时选修了 法语 和艺术的学生
print(french_set.intersection(art_set))

# 2.找出同时选修了所有四门课程的学生----&交集
fa_set=basketball_set & art_set & french_set & football_set
print(fa_set)
# 3.找出选修了足球，但是没有选修篮球的学生
print(football_set.difference(basketball_set))
#方法2:减号---差集
fb_set2 = (football_set - basketball_set)
print(fb_set2)
# 4.统计每一个学生选修的课程数量
all_set = football_set | basketball_set | french_set | art_set
print(all_set)
all_list=[*football_set,*basketball_set,*french_set,*art_set]
for s in all_set:
    print(f"{s}  选修了{all_list.count(s)}")




