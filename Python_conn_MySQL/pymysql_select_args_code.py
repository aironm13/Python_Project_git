import pymysql
from pymysql.cursors import DictCursor


mysqlcon = pymysql.connect(host='172.16.102.150', user='aironm', password='aironm', database='school')
try:
    # cursor类为DictCursor；返回的是字典
    # with mysqlcon.cursor(DictCursor) as cursor:
    # 默认cursor，则返回的是元组
    with mysqlcon.cursor() as cursor:
        select_sql_id = "SELECT * FROM student WHERE id = %s"
        # 在student表中查询id=5的记录，args必须是一个元组(5,)
        cursor.execute(select_sql_id, (5,))
        # 显示查询结果集中所有的记录
        print(cursor.fetchall())

        select_sql_age = "SELECT * FROM student WHERE name like %(name)s and age > %(age)s"
        # 使用%(name)s必须使用字典进行参数传入
        cursor.execute(select_sql_age, {'name':'tom%', 'age':25})
        # 显示查询结果集中所有的记录
        print(cursor.fetchall())

except Exception as e:
    print(e)
finally:
    if mysqlcon:
        mysqlcon.close()

