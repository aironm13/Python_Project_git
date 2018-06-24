import sqlalchemy
import random
# 导入元类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
conn = "mysql+pymysql://aironm:aironm@172.16.102.150:3306/school"
engine = sqlalchemy.create_engine(conn, echo=True)
Session = sessionmaker(bind=engine)
session = Session()



# class Sqlalche:
#     def __init__(self, type='mysql+pymysql', host='172.16.102.150', user='aironm', password='aironm', port=3306, database='school'):
#         self.type = type
#         self.host = host
#         self.user = user
#         self.password = password
#         self.port = port
#         self.database = database
#         conn = "{}://{}:{}@{}:{}/{}".format(self.type,
#                                             self.user,
#                                             self.password,
#                                             self.host,
#                                             self.port,
#                                             self.database)
#         # 创建mysql+pymysql连接的引擎
#         self.engine = sqlalchemy.create_engine(conn, echo=True)
#         # 创建session；用来操作
#         self.Session = sessionmaker(bind=self.engine)
#         self.session = self.Session()
#
#     # rows形参接收实参之后返回一个元组
#     def add(self, *rows):
#         try:
#             # 使用for循环迭代rows元组对象
#             for row in rows:
#                 self.session.add(row)
#             # if len(rows) == 1:
#             # add()：一次只能放入一个Student的实例
#             #     self.session.add(*rows)
#             # elif len(rows) > 1:
#             # add_all()：提交的必须是一个序列集合，可以放入多个Student的实例
#             #     self.session.add_all(rows)
#             self.session.commit()
#         except Exception as e:
#             print(e)
#             self.session.rollback()





class Student(Base):
    __tablename__ = 'student'
    # id字段是Integer，主键，自增长
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    # name字段是string，不能为空
    name = Column('name', String(64), nullable=False)
    # age字段是Integer，可以为空
    age = Column('age', Integer)

    def __repr__(self):
        return "{} id={} name={} age={}".format(self.__class__.__name__,
                                                self.id,
                                                self.name,
                                                self.age)

# --------------------------------------------------
# # 不使用定义的Sqlalche类；
# # 执行对象数据库数据的操作时，必须用到sessionmaker()
# Session = sessionmaker(bind=engine)
# session = Session()

# # 用面向对象方式定义一条数据记录
# s1 = Student(name='Qiyu', age=27)
# print(s1.name, s1.age)
# # 使用session的add方法生成插入SQL语句
# session.add(s1)
# # 使用session的commit方法使数据持久化
# session.commit()
# print(s1)
# --------------------------------------------------


# 插入记录；add()，add_all()
# sqlalche = Sqlalche()
# INSERT插入一条记录
# s1 = Student(name='tom', age=20)
# print(s1.name, s1.age)
# sqlalche.add(s1)

# INSERT插入多条记录
# s2 = Student(name='jerry', age=random.randint(20, 30))
# s3 = Student(name='tim', age=random.randint(20, 30))
# s4 = Student(name='piter', age=random.randint(20, 30))
# sqlalche.add(s2, s3, s4)

# 查询数据；query()
# 生成一个query对象；这个对象并没有把数据都取回来；而是类似懒加载
# student1 = session.query(Student)
# 通过list迭代student对象，把数据拿出并塞到Student类进行实例化
# print(list(student1))

# get()方法；使用主键查询
# student2 = session.query(Student).get(2)
# print(student2)

# 修改：修改的前提是实体必须是persistent状态
# 成功查询并返回主键为2的实体
# student = session.query(Student).get(2)
# print(student)
# # 修改实体的age为40
# student.age = 40
# print(student)
# # 此时使用add；则会生成UPDATE更新语句而不是INSERT插入语句
# session.add(student)
# # 成功之后使实体持久化
# session.commit()

# # 删除：删除的前提是实体必须是persistent状态；如果一个未知的数据则会抛出未持久的异常
# try:
#     student = Student(name='lining', age=43)
#     session.delete(student)
#     session.commit()
# except Exception as e:
#     session.rollback()
#     # 抛出+++ Instance '<Student at 0x1c7a2fc4710>' is not persisted +++；这个实体不是持久的persisten
#     print("+++ {} +++".format(e))
