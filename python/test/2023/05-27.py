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
def fun(*arg1,a,**arg2):
  print(arg1)
  print(a)
  print(arg2)
fun(3,2,1, a = 4, b = 5, c = 6)
