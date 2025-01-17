#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/stats')
def count_objects():
    counts = {"amenities": storage.count("Amenity"),
              "cities": storage.count("City"),
              "places": storage.count("Place"),
              "reviews": storage.count("Review"),
              "states": storage.count("State"),
              "users": storage.count("User")}
    return jsonify(counts)
