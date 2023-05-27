# import  re
# #读取人名文件
# file1 = open('name.txt',encoding='utf-8')
# a = file1.read().split('\n')
# #b为储存出现人名及次数的字典
# b ={}
# #读取书籍
# file2 = open('随便.txt',encoding='utf-8')
# c = file2.read().replace('\n','')
# for i in a:
#     if i != '':
#         b[i] = 0
#
# def find(x):
#     a = re.findall(x,c)
#     b[x] = len(a)
#     return b
# for i in b:
#     find(i)
# print(b)



import re
file1 = open('name.txt','r',encoding='utf-8')
a = file1.read().split('\n')
dict1 ={i:0 for i in a }
file2 = open('遮天.txt',encoding='utf-8')
b = file2.read().replace('\n','')

for i in dict1:
    dict1[i] = b.count(i)

print(dict1)
