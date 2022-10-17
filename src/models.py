from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey)
from src.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, unique=True, primary_key=True, index=True, nullable=False)
    admin = Column(Boolean, default=False)
    username = Column(String, unique=True, primary_key=False, nullable=False)
    hashed_password = Column(String, primary_key=False, nullable=False)



class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, unique=True, primary_key=True, index=True, nullable=False)
    number = Column(String, nullable=False, unique=True)
    detail = Column(String, nullable=True)


class Booking(Base):
    __tablename__ = "book"
    id = Column(Integer, unique=True, primary_key=True, index=True, nullable=False)
    room_status = Column(Integer, nullable=True)
    date_in = Column(String, nullable=True)
    date_out = Column(String, nullable=True)
    room_id = Column(Integer, ForeignKey('room.id'))
    user_id = Column(Integer, ForeignKey('user.id'))







