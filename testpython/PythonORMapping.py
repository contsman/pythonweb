# 导入:
from sqlalchemy import Column, String, create_engine,Integer,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    userid = Column(INTEGER, primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
## add user by Python ORMapping
# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(username='Bob1',password='1234567')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

#query user by Python ORMapping
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
print(type(session.execute('select * from users where userid = 1').first()))
user = session.query(User).filter(User.userid==5).one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.username)
# 关闭Session:
session.close()