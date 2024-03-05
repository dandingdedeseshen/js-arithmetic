import my_utils.str_util
from my_utils import file_util

# 在list中插入一批元素
# list = [1,2,3,4]
# group = (1,2,4)
# list.extend(group)
# print(list)
# print(type(list))

# 去固定的字符
# str = '石头人，原神呀，炸弹人'
# list = str.split('，')
# res1 = list[1][0:2]
# res2 = str[4:6:1]
# print(res2)

# 函数参数
# def fun(a,b,c):
#   print(a,b,c)
# fun(3,b = 2, c = 1)
# def fun(*arg1,a,**arg2):
#   print(arg1)
#   print(a)
#   print(arg2)
# fun(3,2,1, a = 4, b = 5, c = 6)

# 自定义包
str1 = my_utils.str_util.str_reverse('324342')
str2 = my_utils.str_util.substr('1234567890', 4, 8)
print(str1)
print(str2)
file_util.append_to_file('text.txt')

# 排序
# list = [1,2,3, 4, 5,6,7,8]
# print(sorted(list, key=lambda x: abs(5 - x)))

# filter函数
# list = {True,True,False,True}
# l = any(list)
# print(type(l))
# print(l)

# dir
# dic = {'a':1,'b':2}
# print(dir(dic))
