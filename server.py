import os
from flask import Flask, send_file, Response
from gevent.pywsgi import WSGIServer

import trips_service
from db import TripisDb
from configurations_service import ConfigurationsService

app = Flask(__name__)
configs = ConfigurationsService()
db = TripisDb(configs)

@app.route('/tripisapi/trips/')
def get_trips():
    trips = trips_service.get_trips(db)
    return { 'trips': list(map(lambda d: d.__dict__(), trips)) }


@app.route('/tripisapi/trip/<string:trip_id>/')
def get_trip(trip_id: str):
    trip = trips_service.get_trip(db, trip_id)
    if trip is not None:
        return trip.__dict__()
    else:
        return {}


if __name__== '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5001")

    # Production
    print("Started on 5001")
    http_server = WSGIServer(('', 5001), app)
    http_server.serve_forever()
