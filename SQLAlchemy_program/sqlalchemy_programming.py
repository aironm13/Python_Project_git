import sqlalchemy
from sqlalchemy import Column, Integer, String


# 创建一个connect连接引擎
# echo=True：引擎记录所有语句；默认输出stdout
engine = sqlalchemy.create_engine("mysql+pymysql://aironm:aironm@172.16.102.150:3306/school", echo=True)


# 导入元类
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# 创建基类，便于实体类继承；是一个api接口
Base = declarative_base()

# 创建实体类
class Student(Base):
    # 设置表名为类的属性
    __tablename__ = 'student'
    # Column类指定对应的字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    # 第一个参数是字段名，如果和属性名不一致，一定要手动指定
    # age = Column('age', Integer)
    age = Column(Integer)

    def __repr__(self):
        return '{} id={} name={} age={}'.format(self.__class__.__name__,
                                                self.id,
                                                self.name,
                                                self.age)

# 使用SQLAlchemy创建表
# 创建继承自Base的所有表
# Base.metadata.create_all(engine)

# 删除继承自Base的所有表
# Base.metadata.drop_all(engine)

# 创建session
from sqlalchemy.orm import sessionmaker

# 返回type创建的一个类；self.class_ = type(class_.__name__, (class_,), {})
Session = sessionmaker(bind=engine)
session = Session() # 实例化