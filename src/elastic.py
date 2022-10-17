from elasticsearch import Elasticsearch
from sqlalchemy.orm import Session
from src.crud import get_all_bookings


es = Elasticsearch(hosts="localhost", port="9200")


def save_elastic(db: Session):
    bookings = get_all_bookings(db)
    if bookings:
        i = 1
        for booking in bookings:
            b = {"id": f"{booking.id}", "room_status": f"{booking.room_status}", "date_in": f"{booking.date_in}",
                 "date_out": f"{booking.date_out}", "user_id": f"{booking.user_id}", "room_id": f"{booking.room_id}"}
            es.index(index='bookings', body=b, id=i)
            i += 1


def query_on_elastic():
    query = {
        "query": {
            "match_all": {}
        }
    }
    res = es.search(body=query, index='bookings')
    return res


# if __name__ == '__main__':
#     query_on_elastic()