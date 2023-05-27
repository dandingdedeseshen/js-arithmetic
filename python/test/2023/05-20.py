import random

# # 打印99乘法表
# i = 1;
# while i < 10:
#   j = 1  
#   while j <= i:
#     print(f'{j}*{i}={i*j}\t', end='')
#     j += 1
#   print('')
#   i += 1

# # 利用for循环判断字符串中有多少个字母a
# while True:
#   str = input('请输入内容:')
#   num = 0
#   for x in str:
#     if x == 'a':
#       num += 1
#   print(f'有{num}个字母a')

# 统计一个范围内的偶数个数
# max = int(input('请输入一个范围:'))
# num = 0
# for x in range(max):
#     if(x % 2 == 0):
#       num += 1
# print(f'在0到{max}不包含{max}范围内有{num}个偶数')

# 使用for循环打印99乘法表
# for i in range(1,10):
#   for j in range(1,i + 1):
#     print(f'{j}*{i}={i*j}\t', end='')
#   print()

# 发工资
sum = 10000
for i in range(21):
  score = random.randint(1,10)
  if(score < 5):
    print(f'员工{i},绩效分{score},低于5,不发工资,下一位')
  else:
    sum -= 1000
    print(f'向员工{i}发放工资1000元,账户余额{sum}元')
    if(sum <= 0):
      break
print(f'工资发完了下个月领取吧')