import sqlite3
import os

#数据库文件路径
DB_FILE_PATH = ''
#表名称
TABLE_NAME = ''
#是否打印sql
SHOW_SQL = True

def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

#获取游标对象
def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

#删除表操作
def drop_table(conn,table):
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('创建数据表[Course]成功！')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

#创建表操作
def create_table(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print("执行sql:[{}]".format(sql))
        cu.execute(sql)
        conn.commit()
        print("创建数据库表[course]成功！")
        close_all(conn, cu)
    else:
        print("Error. sql = {}".format(sql))

#关闭数据库游标对象和数据库连接对象

def close_all(conn, cu):
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()

#数据库操作
'''sqlite插入数据'''
def sqlite_insert(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            cu.execute(sql,data)
            conn.commit()
            close_all(conn,cu)

def sqlite_update(conn, sql,data):  #sqlite更新数据
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            cu.execute(sql, data)
            conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def sqlite_delete(conn, sql,data):  #sqlite删除数据
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            cu.execute(sql, data)
            conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
    
def sqlite_delete_all(conn, sql):   #sqlite删除全部数据
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            cu.execute(sql, data)
            conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def sqlite_fetchall(conn, sql): #查询所有数据
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        rows = cu.fetchall()
        return rows
    else:
        return None

def sqlite_fetchone(conn, sql, data):   #查询一条数据
    if sql is not None and sql != '':
        if data is not None:
            d = (data,)
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('执行sql:[{}],参数:[{}]'.format(sql,data))
            cu.execute(sql,data)
            row = cu.fetchone()
            return row
        else:
            return None
    else:
        return None

def sqlite_fetchkey(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        cu.execute(sql)
        row = cu.fetchone()
        return row
    else:
        return None
