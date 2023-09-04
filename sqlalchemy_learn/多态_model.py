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
from urllib.parse import quote_plus as urlquote

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session, backref, relationship
from sqlalchemy.schema import CreateTable


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
    """Refers to the type of parent."""

    __table_args__ = {"extend_existing": True}
    __tablename__ = "address"

    __mapper_args__ = {"polymorphic_on": "discriminator"}

    discriminator = Column(String(100))
    street = Column(String(100))
    city = Column(String(100))



class Address_A(AddressAssociation):
    __mapper_args__ = {
        "polymorphic_identity": "address_a",
    }


class Address_B(AddressAssociation):
    __mapper_args__ = {
        "polymorphic_identity": "address_b",
    }


# session.add_all(
#     [
#         Address_B(
#             city="customer 1",
#             street="Ace Hammers",
#         ),
#         Address(
#             city="customer 1",
#             street="Ace Hammers",
#         ),
#     ]
# )

info = {
    "discriminator": "address_b",
}
addr = AddressAssociation(**info)
print(addr.discriminator)
