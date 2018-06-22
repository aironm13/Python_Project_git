import pymysql
from pymysql.cursors import DictCursor # 导入DictCursor类


def select_id():
    mysqlcon = pymysql.connect(host='172.16.102.150', user='aironm', password='aironm', database='school', cursorclass=DictCursor)
    try:
        # pymsysql.connect的__enter__方法返回的就是cursor;
        # 问题：如果不想使用默认的Cursor类，则必须再connect中指定cursorclass类为cursorclass=DictCursor
        with mysqlcon as cursor:
            select_sql = "SELECT * FROM student WHERE id = %s"
            cursor.execute(select_sql, (5,))
            # fetchall返回集中所有的元素
            return cursor.fetchall()
    except Exception as e:
        print(e)
    # 问题：mysqlcon使用with返回的是cursor；mysqlcon的__exit__只会commit或rollback；而这里没有对cursor使用with；所以cursor也不会关闭释放资源；
    finally:
        # 释放cursor和mysqlcon的资源
        cursor.close()
        mysqlcon.close()

if __name__ == '__main__':
    # 使用了DictCursor，所以返回的是一个字典
    print(select_id())