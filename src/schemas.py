from pydantic import BaseModel
from typing import Optional


class RoomBase(BaseModel):
    number: str
    detail: str


class Room(RoomBase):
    id: int


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserCreate):
    id: int
    admin: bool


class BookingBase(BaseModel):
    date_in: str
    date_out: str
    room_id: int


class MakeABooking(BookingBase):
    room_status: int
    user_id: int


class Booking(MakeABooking):
    id: int


class UpdateBooking(BaseModel):
    date_in: str
    date_out: str
    room_status: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None