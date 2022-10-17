from sqlalchemy.orm import Session
from fastapi import Depends
from src import schemas, models
from datetime import datetime


def create_room(db: Session, room: schemas.RoomBase):
    db_room = models.Room(number=room.number, detail=room.detail)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()


def get_a_room(db: Session, id: int):
    return db.query(models.Room).filter(models.Room.id == id).first()


def RoomId_to_RoomNumber(db: Session, id: int):
    room = db.query(models.Room).filter(models.Room.id == id).first()
    return room.number


def RoomNumber_to_RoomId(db: Session, room_number: int):
    room = db.query(models.Room).filter(models.Room.number == room_number).first()
    return room.id


def get_one_room(db: Session, number: str):
    return db.query(models.Room).filter(models.Room.number == number).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == int(user_id)).first()


def is_user_is_admin(db: Session, user: str):
    role_a = db.query(models.User).filter(models.User.username == user).first()
    if role_a.admin == True:
        return True
    else:
        return False


def promote_user(db: Session, user: schemas.UserBase):
    target_user = db.query(models.User).filter(models.User.username == user).first()
    if target_user:
        target_user.admin = True
        db.commit()
        db.refresh(target_user)


def is_room_available(f_dates: schemas.BookingBase, db: Session):
    f_in = datetime.strptime(f_dates.date_in, '%Y-%m-%d').date()
    f_out = datetime.strptime(f_dates.date_out, '%Y-%m-%d').date()
    r_id = f_dates.room_id
    booked = db.query(models.Booking).filter(models.Booking.room_id == r_id).all()
    for b in booked:
        b_in = datetime.strptime(b.date_in, '%Y-%m-%d').date()
        b_out = datetime.strptime(b.date_out, '%Y-%m-%d').date()
        if b_in < f_in and b_out < f_out:
            return True
        else:
            return False


def make_booking(db: Session, booking_detail: schemas.MakeABooking):
    db_booking = models.Booking(room_status=1, date_in=booking_detail.date_in, date_out=booking_detail.date_out, room_id=booking_detail.room_id, user_id=1)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)


def update_expire_room(db: Session):
    expire_booking = db.query(models.Booking).filter(models.Booking.room_status.endswith('2')).all()
    for eb in expire_booking:
        d_out = datetime.strptime(eb.date_out, '%Y-%m-%d')
        if datetime.now() > d_out:
            eb.room_status = '0'
            db.commit()
            db.refresh(eb)


def settlement(id, db: Session):
    settle_booking = db.query(models.Booking).filter(models.Booking.id == id).first()
    s_e = settle_booking.room_status
    if s_e == '1':
        s_e = '2'
        db.commit()
        db.refresh(s_e)


def update_failed_booked(id, db: Session):
    failed_booking = db.query(models.Booking).filter(models.Booking.id == id).first()
    f_b = failed_booking.room_status
    if f_b == '1':
        f_b = '0'
        db.commit()
        db.refresh(f_b)


def delete_booking(id: int, db: Session):
    target_booking = db.query(models.Booking).filter(models.Booking.id == id).first()
    db.delete(target_booking)
    db.commit()
    db.refresh(target_booking)


def get_bookings(room_id: int, db: Session):
    return db.query(models.Booking).filter(models.Booking.room_id == room_id).all()


def get_all_bookings(db: Session):
    return db.query(models.Booking).all()