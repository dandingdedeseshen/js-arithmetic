# 推导式
# arr = [[1,2,3],[4,5,6]]
# trupl = (j+len(i) for i in arr for j in i)
# for i in trupl:
#   print(i)

#修饰符
def test(func):
    print('This is test function step1')
    func()
    print('This is test function step2')
    
@test
def func():
    print('This is func...')
 