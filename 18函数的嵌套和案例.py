# # 1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积= 底*高/2)。
# def cir_area(b,h):
#     """
#     根据传入的底和高计算三角形面积
#     :param b: 底
#     :param h: 高
#     :return: 面积
#     """
#     s = b*h/2
#     return s
# print("三角形的面积:",cir_area(5,5))
# # 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
# def count_aeiou(s):
#     """
#     计算传入的字符串中元音字母的个数
#     :param s: 输入的字符串
#     :return: 出现次数
#     """
#     num = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num += 1
#     return num
# print(count_aeiou("suidfg9q8udj-0qpndoivzbsxciyu908sfvcqyiudskzbx7tq89dna"))

# 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，
def aiu_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 学生分数列表
    :return: 最高分,最低分,平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list)/len(score_list),2)
    return max_s,min_s,avg_s
s_list = [90,88,44,22,67,89,99]
max_score,min_score,avg_score = aiu_score(s_list)
print("最高分:",max_score)
print("最低分:",min_score)
print("平均分:",avg_score)
