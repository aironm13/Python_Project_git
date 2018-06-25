from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import enum


Base = declarative_base()

conn = "mysql+pymysql://aironm:aironm@172.16.102.150:3306/test"
engine = create_engine(conn, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'

class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column('emp_no', Integer, primary_key=True)
    birth_date = Column('birth_date', Date, nullable=False)
    first_name = Column('first_name', String(14), nullable=False)
    last_name = Column('last_name', String(16), nullable=False)
    gender = Column('gender', Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    def __repr__(self):
        return "{} emp_no={} name={} {} gender={}".format(self.__class__.__name__,
                                                          self.emp_no,
                                                          self.first_name,
                                                          self.last_name,
                                                          self.gender.value)


def show(emps):
    for emp in emps:
        print(emp)
    print('\n\n')



# 查询
from sqlalchemy import or_, and_, not_

# # filter相当于SQL中的where；条件Employee.emp_no > 10015
# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# show(emps)

# # 与;&;and_
# # &两边的条件都必须使用括号，否则会引发不可预知的结果
# emps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.gender == MyEnum.M))
# show(emps)
#
# # and_中的条件使用逗号分隔
# emps = session.query(Employee).filter(and_(Employee.emp_no > 10015, Employee.gender == MyEnum.M))
# show(emps)

# # 或：|，or_
# # |
# emps = session.query(Employee).filter((Employee.emp_no > 10018) | (Employee.emp_no < 10003))
# show(emps)
#
# # or_
# emps = session.query(Employee).filter(or_(Employee.emp_no > 10018, Employee.emp_no < 10003))
# show(emps)

# # # 非：not_,~:表示取反
# # not_
# emps = session.query(Employee).filter(not_(Employee.emp_no < 10018))
# show(emps)
# # ~
# emps = session.query(Employee).filter(~(Employee.emp_no < 10018))
# show(emps)

# # in
# emplists = [10010, 10015, 10392]
# emps = session.query(Employee).filter(Employee.emp_no.in_(emplists))
# show(emps)

# # not in
# emplists = [10010, 10015, 10392]
# emps = session.query(Employee).filter(Employee.emp_no.notin_(emplists))
# show(emps)

# # like
# emps = session.query(Employee).filter(Employee.last_name.like('P%'))
# show(emps)

# # 排序
# # 升序
# emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.emp_no)
# show(emps)
# # 降序；desc()
# emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.emp_no.desc())
# show(emps)
# # 多列排序
# emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.last_name).order_by(Employee.emp_no.desc())
# show(emps)

# # 分页
# # limit # 显示结果的前4条记录
# emps = session.query(Employee).limit(4)
# show(emps)
# # offset：偏移多少条记录
# emps = session.query(Employee).limit(4).offset(18)
# show(emps)


# # all，first，one等方法
# emps = session.query(Employee)
# # all返回列表容器，查不到返回空列表
# print(emps.all())
#
# # 取匹配结果的首行，查不到返回None
# print(emps.first())
#
# # 查询结果有且只能有一行，否则抛出异常
# print(emps.one())


# # 聚合函数
# from sqlalchemy import func
# query = session.query(func.count(Employee.emp_no))
# print(query.one()) # 有且只有一个结果返回
# print(query.scalar()) # 取one()返回元组的第一个元素
#
# # max/min/avg
# print(session.query(func.max(Employee.emp_no)).scalar())
# print(session.query(func.min(Employee.emp_no)).scalar())
# print(session.query(func.avg(Employee.emp_no)).scalar())
#
# # group_by：分组
# # 等价SELECT gender, COUNT(emp_no) FROM employees GROUP BY gender;
# # 按照gender字段分组；COUNT(emp_no)的数值
# print(session.query(Employee.gender, func.count(Employee.emp_no)).group_by(Employee.gender).all())

# 关联查询
