import pymysql
from pymysql.cursors import DictCursor

# 创建connect连接对象
mysqlcon = pymysql.connect(host='172.16.102.150', user='aironm', password='aironm', database='school', cursorclass=DictCursor)


def select_id(num=0):
    try:
        # 返回mysqlcon的cursor对象
        with mysqlcon.cursor() as cursor:
            select_sql = "SELECT * FROM student WHERE id = %s"
            # 如果select_sql语句没有查到num，则返回空元组或空列表；
            cursor.execute(select_sql, (num,))
            return cursor.fetchall()
        # 没有mysqlcon的上下文；所有需要手动commit
        mysqlcon.commit()
    # 如果抛出异常则回滚
    except Exception as e:
        print(e)
        mysqlcon.rollback()
    # 在finally中关闭mysqlcon的连接，释放资源
    finally:
        if mysqlcon:
            mysqlcon.close()

if __name__ == '__main__':
    print(select_id(5))