import sqlalchemy
from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.state import InstanceState


conn = "mysql+pymysql://aironm:aironm@172.16.102.150:3306/school"
engine = create_engine(conn, echo=True)


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    age = Column('age')

    def __repr__(self):
        return "{} id={} name={} age={}".format(self.__class__.__name__,
                                                self.id,
                                                self.name,
                                                self.age)


Session = sessionmaker(bind=engine)
session = Session()

def getstatus(entity, num):
    insp = sqlalchemy.inspect(entity)
    state = "sessionid={}, attached={}\ntransient={}, persistent={}\npending={}, deleted={}, detached={}".format(insp.session_id,
                                                                                                                 insp._attached,
                                                                                                                 insp.transient,
                                                                                                                 insp.persistent,
                                                                                                                 insp.pending,
                                                                                                                 insp.deleted,
                                                                                                                 insp.detached)
    print(num, state)
    print(insp.key)
    print('-'*30)

# 状态

student = session.query(Student).get(2)
# student实体成功从数据库中返回，所以状态persistent
getstatus(student, 1)

try:
    # 状态为transit，student只是一个实体，没有加入到session中；临时的
    student = Student(id=10, name='lisa', age=24)
    getstatus(student, 2)

    # student实体添加到session中，状态从transit转换为pending
    session.add(student)
    getstatus(student, 4)

    # # student实体现在状态是pending，删除的前提状态是persistent，不满足条件；抛出student不是持久化
    # session.delete(student)
    # getstatus(student, 5)

    # student实体被commit持久化到数据库中；并被查询返回，所以状态从pending转换为persistent持久化
    session.commit()
    getstatus(student, 6)
except Exception as e:
    session.rollback()
    print('+++ {} +++'.format(e))