# 导入:
from urllib.parse import quote_plus as urlquote

from requests import session
from sqlalchemy import BIGINT, Column, String, create_engine, text
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
    data_size = Column(
        BIGINT, server_default=text("0"), nullable=False, comment="unit: KB"
    )


# 初始化数据库连接:
# engine = create_engine(
#     "mysql+pymysql://root:p@3Sw0rd@192.168.78.213:3306/test?charset=utf8mb4",
#     echo=True,
# )

engine = create_engine(
    f"mysql+pymysql://root:{urlquote('p@3Sw0rd')}@192.168.78.213:3306/airflow?charset=utf8mb4",
    echo=True,
)

# Base.metadata.create_all(engine)

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

# Session.session_factory()

Session.add(User(id=2, name="test"))
Session.commit()
