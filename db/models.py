from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, BigInteger

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)
    elixir = Column(BigInteger)
    money = Column(BigInteger)
    gems = Column(BigInteger)
