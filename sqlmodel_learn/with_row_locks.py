from time import sleep
from typing import Optional
from urllib.parse import quote_plus as urlquote

from sqlmodel import Field, Session, SQLModel, create_engine


# # 表的名字:
# __tablename__ = "user"
class UserLock(SQLModel, table=True):
    # 表的结构:
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


user_1 = UserLock(name="Deadpond")

# engine = create_engine("sqlite://")
engine = create_engine(
    f"mysql+pymysql://root:{urlquote('p@3Sw0rd')}@192.168.78.213:3306/airflow?charset=utf8mb4",
    echo=True,
)

# 创建表
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(user_1)
    session.commit()
    # 刷新
    session.refresh(user_1)

with Session(engine) as session:
    # WHERE userlock.id = %(id_1)s
    #  LIMIT %(param_1)s FOR UPDATE
    user = (
        session.query(UserLock)
        .filter(UserLock.id == user_1.id)
        .with_for_update()
        .first()
    )

    # 开启 mycli 执行，堵塞
    # select * from userlock where id -> = 6 for update;

    sleep(100)
    assert user
    assert user.name == user_1.name
