import pymysql

class Sql():
    def __init__(self):
        pass

    #存储视频数据
    def save_data(self,form_name,list):

        # 数字不能直接作为表的名字
        table_name = str( form_name)
        conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'test' ,charset = 'utf8')
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

        # sql语句创建一个新表
        create_table = '''create table {} (
        timer varchar(100) CHARACTER SET utf8,av int(10),
        av_name varchar(100) CHARACTER SET utf8 , comment int(10),mid int(20),play int(10),
         danmu int(10),like_num int(10) ,favorite int(10) ,coin int(10),class_name varchar(10) CHARACTER SET utf8
         PRIMARY KEY (timer, `av`)
         )'''

        # 存储up主的信息
        insert = 'insert into {} (timer,av ,av_name , comment,mid,play , danmu , like_num ,favorite,coin,class_name) values (now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            cursor.execute(create_table.format(table_name))
        except:
            print('该分类的数据表已存在，将跳过创建')
        finally:
            print('开始将up主的视频信息存入数据库')
            cursor.executemany(insert.format(table_name) , list)

        conn.commit()
        cursor.close()
        conn.close()
 
    def select(self ,name,table,name1,name2):
        print('查找数据')
        # 配置数据库连接
        conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'test' ,charset = 'utf8')
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        
        select = 'select {} from {} where {} = {}'
        data = cursor.execute(select.format(str(name),str(table),str(name1),str(name2)))
        data = cursor.fetchall() 

        cursor.close()
        conn.close()

        return data

    def select2(self,name,table,name1,name2,name3,name4):
        print('查找数据2')
        # 配置数据库连接
        conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'test' ,charset = 'utf8')
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        
        select = 'select {} from {} where {} = {} AND {} = {}'
        data = cursor.execute(select.format(str(name),str(table),str(name1),str(name2),str(name3),str(name4)))
        data = cursor.fetchall() 

        cursor.close()
        conn.close()

        return data
    
    def insert(self,tuple):
        # print('向{}添加数据'.format(str(form)))
        # 配置数据库连接
        conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'test' ,charset = 'utf8')
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

        insert1 = 'insert into %s(%s,%s) value("%s","%s")'
        insert2 = 'insert into %s(%s,%s,%s,%s) value(%s,%s,%s,now())'
        if  len(tuple) == 5 :
            data = cursor.execute(insert1%tuple)
        if len(tuple) == 8:
            data = cursor.execute(insert2%tuple)

        data = cursor.fetchall()
        
        conn.commit()
        cursor.close()
        conn.close()

        return data

    def special_sql(self,str1,mid,num):
        print('开始查找')
        # 配置数据库连接
        conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'test' ,charset = 'utf8')
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
        

       
        data = cursor.execute(str1.format(str(mid),str(num)))
        data = cursor.fetchall() 

        
        conn.commit()
        cursor.close()
        conn.close()

        return data

if __name__ == '__main__':
    aid = '16794231'
    time = '"2020-05-11 15:25%"'
    str1 = 'SELECT * FROM `video` where mid = {} AND timer like {}'

    data = Sql.special_sql(1,str1,aid,time)

    print(data)

