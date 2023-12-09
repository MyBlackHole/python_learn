from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import event

postgresql_engine = create_engine(
    "postgresql+pyscopg2://scott:tiger@hostname/dbname",
    # disable default reset-on-return scheme
    pool_reset_on_return=None,
)


@event.listens_for(postgresql_engine, "reset")
def _reset_postgresql(dbapi_connection, connection_record, reset_state):
    if not reset_state.terminate_only:
        dbapi_connection.execute("CLOSE ALL")
        dbapi_connection.execute("RESET ALL")
        dbapi_connection.execute("DISCARD TEMP")

    # so that the DBAPI itself knows that the connection has been
    # reset
    dbapi_connection.rollback()


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    __mapper_args__ = {
        "polymorphic_identity": "employee",
        "polymorphic_on": type,
    }
