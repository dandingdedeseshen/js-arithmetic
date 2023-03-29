import pymysql
from const import sql
import time

# 连接数据库
conn = pymysql.connect(host=sql['host'], port = sql['port'], user=sql['user'], password=sql['password'], database=sql['database'],charset='utf8')  

# 配置自动提交模式防止sql长时间未响应关闭
conn.autocommit(True)
conn.timeout = 60 * 60 * 5

cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  #配置数据返回格式为字典型
 # 通用查找
def select(name,fromName,filterSql):
    sql = 'SELECT {} FROM {} WHERE Is_del=0 {}'.format(str(name),str(fromName),str(filterSql))
    data = cursor.execute(sql)
    data = cursor.fetchall() 
    conn.commit()
    return data

 # 通用查找-没有伪删
def selectDel(name,fromName,filterSql):
    sql = 'SELECT {} FROM {} WHERE 1=1 {}'.format(str(name),str(fromName),str(filterSql))
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
            if('userName' in parm):
                filter = "AND User_name = '{}'".format(parm['userName'])
        return select('*','User_message',filter)

    # 上传文件
    def uploadFile(parm):
        filter = ''
        if bool(parm):
            if('fileName' in parm):
                timeStr = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                filter = "(File_name, Upload_time, Upload_user) VALUE ('{}', '{}', '{}')".format(str(parm['fileName']),str(timeStr),str(parm['userName']))
        return insert('File_message',filter)

    # 查找文件
    def findFile(parm):
        filter = ''
        if bool(parm):
            if('userName' in parm):
                filter = "AND Upload_user = '{}'".format(parm['userName'])
            if('identity' in parm and not parm['identity']):
                filter = "AND Upload_user != 'xiaoliu' AND Upload_user != 'xiaocao'"
        return selectDel('*','File_message',filter)
    

