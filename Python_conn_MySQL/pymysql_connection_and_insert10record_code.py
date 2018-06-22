import pymysql
import random

# 创建一个connect连接对象
mysqlcon = pymysql.connect(host='172.16.102.150', user='aironm', password='aironm', database='school')
# 测试连接是否正常；
print(mysqlcon.ping(False))
try:
    # cursor()使用上下文
    with mysqlcon.cursor() as cursor:
        # 创建一个SQL语句
        insert_sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
        # 循环10次，准备插入10条记录
        for i in range(1, 10):
            # execute中对应的数据必须是一个元组('tom{}'.format(i), random.randint(20, 40))
            cursor.execute(insert_sql, ('tom{}'.format(i), random.randint(20, 40)))
    # 持久化到磁盘上
    mysqlcon.commit() # 提交；持久化到磁盘中
except Exception as e:
    print(e)
    mysqlcon.rollback() # 如果抛出异常，则回滚
finally:
    if mysqlcon:
        mysqlcon.close() # 关闭mysqlcon连接
