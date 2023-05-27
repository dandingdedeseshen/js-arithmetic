# 连接数据库

import pymysql

conn = pymysql.connect(port = 3306 , user = 'root' , password = 'jhtxdy123' , db = 'test',charset = 'utf8')
c = conn.cursor(cursor = pymysql.cursors.DictCursor)
a = 2

c.execute("insert into test1 (视频名称,视频编号) value ('阴阳师',12345)" )
if a == 1 :
    conn.rollback()
else:
    conn.commit()


c.close()
conn.close()



