"""Illustrates a mixin which provides a generic association
using a single target table and a single association table,
referred to by all parent tables.  The association table
contains a "discriminator" column which determines what type of
parent object associates to each particular row in the association
table.

SQLAlchemy's single-table-inheritance feature is used
to target different association types.

This configuration attempts to simulate a so-called "generic foreign key"
as closely as possible without actually foregoing the use of real
foreign keys.   Unlike table-per-related and table-per-association,
it uses a fixed number of tables to serve any number of potential parent
objects, but is also slightly more complex.

"""
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Session
from urllib.parse import quote_plus as urlquote


@as_declarative()
class Base:
    """Base class which provides automated table name
    and surrogate primary key column.

    """

    __table_args__ = {"extend_existing": True}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class AddressAssociation(Base):

    __table_args__ = {"extend_existing": True}
    __tablename__ = "address"

    discriminator = Column(String(100))
    """Refers to the type of parent."""

    __mapper_args__ = {"polymorphic_on": discriminator}


class Address(AddressAssociation):
    street = Column(String(100))
    city = Column(String(100))
    discriminator = Column(String(100))

    __mapper_args__ = {
        "polymorphic_identity": "address",
    }


class Address_B(AddressAssociation):
    city = Column(String(100))
    street = Column(String(100))
    discriminator = Column(String(100))

    __mapper_args__ = {
        "polymorphic_identity": "address_b",
    }


# engine = create_engine("sqlite://", echo=True)
engine = create_engine(
    f"mysql+pymysql://root:{urlquote('p@3Sw0rd')}@192.168.78.213:3306/airflow?charset=utf8mb4",
    echo=True,
)

# # Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session(engine)

session.add_all(
    [
        Address_B(
            city="customer 1",
            street="Ace Hammers",
        ),
        Address(
            city="customer 1",
            street="Ace Hammers",
        ),
    ]
)

session.commit()

#print(Address_B.filter())
for addr in session.query(Address_B):
    print(addr)
