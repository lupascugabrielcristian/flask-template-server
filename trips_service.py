from db import TripisDb
from trip import Trip

def record_to_trip(trip_record) -> Trip:
    trip = Trip()
    trip.id = trip_record[0]
    trip.city = trip_record[1]
    trip.country = trip_record[2]
    trip.userId = trip_record[3]
    trip.participants = trip_record[4]
    return trip

def get_trips(db: TripisDb):
    sql_records = db.get_trips()

    # Trip[]
    trips = list(map(lambda r: record_to_trip(r), sql_records))
    return trips


def get_trip(db: TripisDb, trip_id: str):
    sql_records = db.get_trip(trip_id)
    if len(sql_records) > 0:
        trip_record = sql_records[0]
        return record_to_trip(trip_record)
    else:
        return None

