import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',port = 3306,user='root',password='admin',database='flow',charset='utf8')   
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  #配置数据返回格式为字典型

class Sql():
    def select(name,fromName,filterSql):
        sql = 'SELECT {} FROM {} WHERE isDel=0 {}'.format(str(name),str(fromName),str(filterSql))
        data = cursor.execute(sql)
        data = cursor.fetchall() 
        conn.commit()
        return data    

    def update(fromName,setSql,filterSql):
        sql = 'UPDATE {} SET {} WHERE 1=1 {}'.format(str(fromName),str(setSql),str(filterSql))
        data = cursor.execute(sql)
        conn.commit()
        return data  

    def insert(fromName,insertSql):
        sql = 'INSERT INTO {} {}'.format(str(fromName),str(insertSql))
        data = cursor.execute(sql)
        conn.commit()
        return data 
