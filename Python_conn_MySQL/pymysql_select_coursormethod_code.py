import pymysql
from pymysql.cursors import DictCursor

# cursorclass=DictCursor如果定义：feth方法返回的是字典类型；列表包含字典
mysqlcon = pymysql.connect(host='172.16.102.150', user='aironm', password='aironm', database='school', cursorclass=DictCursor)

try:
    # mysqlcon.cursor(DictCursor)也可以定义
    with mysqlcon.cursor() as cursor:
        # 定义查询语句
        select_sql = "SELECT * FROM student"
        # 返回影响的行数
        rows = cursor.execute(select_sql)
        # fetchone()返回查询结果的下一行
        print(1, cursor.fetchone())
        # fetchmany()返回一个元组列表，如果有数据，默认返回一个元组的元组列表
        print(2, cursor.fetchmany(12))
        # fetchall()返回查询结果的剩余记录
        print(3, cursor.fetchall())

except Exception as e:
    print(e)
finally:
    if mysqlcon:
        mysqlcon.close()

