# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# 创建对象的基类:
Base = declarative_base()


# pip3 install sqlacodegen
class User(Base):
    # 表的名字:
    __tablename__ = "user"

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine(
    "mysql+pymysql://root:p@3Sw0rd@192.168.78.212:3306/airflow?charset=utf8mb4",
    echo=True,
)
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        expire_on_commit=False,
    )
)

Session.get()
