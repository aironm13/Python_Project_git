import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, String, Integer, Date, Enum, ForeignKey
import enum


Base = declarative_base()

conn = "mysql+pymysql://aironm:aironm@172.16.102.150:3306/test"
engine = create_engine(conn, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'


# 创建表的实体类
class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(64), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    dept_emps = relationship('Dept_emp')

    def __repr__(self):
        return "{} emp_no={} name={} {} gender={} dept_emp={}".format(self.__class__.__name__,
                                                          self.emp_no,
                                                          self.first_name,
                                                          self.last_name,
                                                          self.gender,
                                                          self.dept_emps)

class Department(Base):
    __tablename__ = 'departments'

    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False, unique=True)

    def __repr__(self):
        return "{} dept_no={} name={}".format(type(self).__name__,
                                              self.dept_no,
                                              self.dept_name)

class Dept_emp(Base):
    __tablename__ = 'dept_emp'
    # emp_no，dept_no联合主键
    # ForeignKey('employees.emp_no', ondelete='CASCADE')：定义外键约束
    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4), ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "{} emp_no={} dept_no={}".format(type(self).__name__,
                                                self.emp_no,
                                                self.dept_no)


def show(rows):
    for row in rows:
        print(row)
    print('\n\n')

# 查询
# # 1，使用隐式内连接
# # 等价SELECT * FROM employees, dept_emp WHERE employees.emp_no = dept_emp.emp_no AND employees.emp_no = 10010;
# results = session.query(Employee, Dept_emp).filter(Employee.emp_no == Dept_emp.emp_no).filter(Employee.emp_no == 10010)
# show(results)
# # 查询结果如下
# # (Employee emp_no=10010 name=Duangkaew Piveteau gender=MyEnum.F, Dept_emp emp_no=10010 dept_no=d004)
# # (Employee emp_no=10010 name=Duangkaew Piveteau gender=MyEnum.F, Dept_emp emp_no=10010 dept_no=d006)

# 2，使用join
# 问题：只返回一条记录
results = session.query(Employee).join(Dept_emp).filter(Employee.emp_no == 10010)
show(results)
# 问题：只返回一条记录
results = session.query(Employee).join(Dept_emp, Employee.emp_no == Dept_emp.emp_no).filter(Employee.emp_no == 10010)
show(results)

# 问题的原因：query(Employee)只能返回一个实体对象；需要修改实体类Emplyee，增加属性用来存放部门信息；来解决这个问题

# 解决;使用relationship
# 解决之后输出：dept_emp就是查询的部门信息
# Employee emp_no=10010 name=Duangkaew Piveteau gender=MyEnum.F dept_emp=[Dept_emp emp_no=10010 dept_no=d004, Dept_emp emp_no=10010 dept_no=d006]
