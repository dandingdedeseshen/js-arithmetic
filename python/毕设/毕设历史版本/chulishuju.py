# 播放量占比分析
# import matplotlib
# import matplotlib.pyplot as plt
# import pymysql
# import pandas as pd
# conn = pymysql.connect(host = 'localhost' , port =3306 , user = 'root' , passwd = 'cdy1113' , db = 'bilibili')
# sql = 'select view from bilibili_data'
# data = pd.read_sql(sql=sql,con=conn)
# # print(data)
#
# plt.rcParams['font.sans-serif']=['Simhei']
# plt.rcParams['axes.unicode_minus']=False
# ziti = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

# 构造数据
def test():
    i=int(0)
    j=int(0)
    k=int(0)
    l=int(0)
    n=int(0)
    # view=data
    view = 2
    if view<500:
        i=i+1;
    elif 500<=view and view<1000:
        j=j+1;
    elif 1000<=view and view<5000:
        k=k+1;
    elif 5000<=view and view<20000:
        l=l+1;
    else:
        n=n+1;
    sum=i+j+k+l+n
    return (i,j,k,l,n,sum)
def view_percent():
    return (test()[0],test()[1],test()[2],test()[3],test()[4] )/test()[5]
# labels = ['<500','500-1000','1000-5000','5000-20000','>20000']
# # 绘制饼图
# plt.pie(x = view_percent, # 绘图数据
# labels=labels, # 添加水平标签
# autopct='%.1f%%' # 设置百分比的格式，这里保留一位小数
# )
# # 添加图标题
# plt.title('播放量占比')
# # 显示图形
# plt.show()

view_percent()