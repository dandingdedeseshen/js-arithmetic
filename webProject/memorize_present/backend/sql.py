import pymysql
from const import sql

# 连接数据库
conn = pymysql.connect(host=sql['host'], port = sql['port'], user=sql['user'], password=sql['password'], database=sql['database'],charset='utf8')   
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  #配置数据返回格式为字典型
 # 通用查找
def select(name,fromName,filterSql):
    sql = 'SELECT {} FROM {} WHERE Is_del=0 {}'.format(str(name),str(fromName),str(filterSql))
    data = cursor.execute(sql)
    data = cursor.fetchall() 
    conn.commit()
    return data    
# 通用更新
def update(fromName,setSql,filterSql):
    sql = 'UPDATE {} SET {} WHERE 1=1 {}'.format(str(fromName),str(setSql),str(filterSql))
    data = cursor.execute(sql)
    conn.commit()
    return data  
# 通用插入
def insert(fromName,insertSql):
    sql = 'INSERT INTO {} {}'.format(str(fromName),str(insertSql))
    data = cursor.execute(sql)
    conn.commit()
    return data
class Sql():
    # 登录
    def login(parm):
        filter = ''
        if bool(parm):
            if(bool(parm['userName'])):
                filter = "AND User_name = '{}'".format(parm['userName'])
        return select('*','User_message',filter)

