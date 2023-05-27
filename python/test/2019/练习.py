# 对列表下标为偶数的元素降序排序下标为奇数的不变 2020/1/19
# import random
#
# # 生成列表
# list1 = [random.randint(1,10) for i in range(20)]
# # 查看列表
# list2 = list1[1::2]
# list2.sort(reverse=True)
# list1[1::2] = list2
#
# print(list1)



# 对小于1000的数字进行分解  2020/1/19

# 封装为一个函数
# def fun(a):
#     list = [] #用来存储数字的因数(从2开始第一个能整除的数字)
#     x = a #保留一下用户输入的a 因为如果是素数 list就由1和这数字组成
#     i = 2;
#     while i <= a:  #for循环中的i在遇到第一次整除的数时不能重置为2所以使用while循环
#         if a%i == 0:
#             list.append(i)
#             a = a // i
#             i = 1
#         i += 1
#     if len(list) == 1:
#         list = [1,x]
#     return list
# a = int(input('请输入一个数字：'))
# print(fun(a))

#100以内的奇数的计算    2020/1/19
#方法1
# list = [i for i in range(100)]
# print(sum(list[1::2]))
#方法2
# sum2 = 0;
# for i in range(100):
#     if i % 2 == 1:
#         sum2 += i
# print(sum2)

# 输出有1234组成的4位素数 并且1234不重复
# list = []
# for i in [1,2,3,4]:
#     for j in [1,2,3,4]:
#         if i != j:
#             for k in [1,2,3,4]:
#                 if i != k and j != k:
#                     for l in [1,2,3,4]:
#                         if l not in [i,j,k]:
#                             list.append(i * 1000 + j * 100 + k * 10 + l)
#
# for i in list[::-1]:
#     for j in range(2,i,):
#         if i % j == 0:
#             list.remove(i)
#         break
# print(list)