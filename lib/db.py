#coding:utf-8
"""数据库操作"""
import pymysql
import sys
sys.path.append("..")#提升包的搜索路径提升到项目路径下

from config import config as cf

#获取连接方法
def get_conn():
    conn=pymysql.connect(
        host=cf.db_host,
        port=cf.db_port,
        user=cf.db_user,
        password=cf.db_password,
        db=cf.db,
        charset='utf8'
    )
    return conn
#读取查询操作
def db_query(sql):
        conn=get_conn()
        cur=conn.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        cf.logging.debug(sql)#debug大写表常量，小写表方法
        cf.logging.debug(result)
        conn.close()

        return  result



#修改操作
def db_change(sql):
    conn=get_conn()
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()

if __name__=='__main__':
    result=db_query("select * from user where name='张三'")
    print(result)
