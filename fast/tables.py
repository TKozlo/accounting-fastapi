from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()



class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(6, 2))
    description = Column(String, nullable=True)

    user = relationship('User', backref='operations')
 

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


   