from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


class Parent(db.Model):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class Child(db.Model):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", backref=backref("child"))

    ###  只删除父级，子不影响
    # 1. parent_id = Column(Integer, ForeignKey('parent.id', ondelete="CASCADE"))
    #    parent = relationship("Parent", backref=backref("child", passive_deletes=True))

    ###  子级跟随删除
    # 2. parent = relationship("Parent", backref = backref("child", cascade="all, delete-orphan"))
    # 3. parent = relationship("Parent", backref = backref("child", cascade="all,delete"))

    ##  父级删除，子级不删除，外键更新为 null
    # 4. parent = relationship("Parent", backref = backref("child"))
