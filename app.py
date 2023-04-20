import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///abdata.sqlite", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine, reflect=True)

session = Session(engine)
app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"#Paris Airbnb Data#<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"@Available Airbnbs<br/>"
        f"/api/v1.0/paris<br/>"
        f"<br/>"
        f"@Airbnbs Nearby Metro<br/>"
        f"/api/v1.0/nearbymetro<br/>"
        f"<br/>"
        f"@Minimum and Maximum Room rate you are looking for<br/>"
        f"/api/v1.0/start/end<br/>"
        )

Paris = Base.classes.paris
   

@app.route("/api/v1.0/paris")
def ava():
    ava_q = session.query(
    Paris.attr_index,
    Paris.biz, 
    Paris.cleanliness_rating, 
    Paris.host_is_superhost,
    Paris.metro_dist,
    Paris.realSum,
    Paris.bedrooms,
    Paris.guest_satisfaction_overall,
    Paris.person_capacity,
    Paris.lat,
    Paris.lng)\
    .all()

    ava_l = []
    for attr, biz, clean, host, dist, rate, bedrooms, rating, cap, lat, lng in ava_q:
        ava_d = {}
        ava_d["attr_index"] = attr
        ava_d["biz"] = biz
        ava_d["cleanliness_rating"] = clean
        ava_d["host_is_superhost"] = host
        ava_d["metro_dist"] = dist
        ava_d["realSum"] = rate
        ava_d["bedrooms"] = bedrooms
        ava_d["guest_satisfaction_overall"] = rating
        ava_d["person_capacity"] = cap
        ava_d["lat"] = lat
        ava_d["lng"] = lng
        ava_l.append(ava_d)
    return jsonify(ava_l)


@app.route("/api/v1.0/nearbymetro")
def metro():
    dtce = 0.2
    metro_q = session.query(Paris.metro_dist, Paris.realSum, Paris.bedrooms, Paris.guest_satisfaction_overall)\
    .filter(Paris.metro_dist <= dtce)\
    .all()
    metro_l = []
    for dist, rate, bedrooms, rating in metro_q:
        metro_d = {}
        metro_d["metro_dist"] = dist
        metro_d["realSum"] = rate
        metro_d["bedrooms"] = bedrooms
        metro_d["guest_satisfaction_overall"] = rating
        metro_l.append(metro_d)
    return jsonify(metro_l)

@app.route("/api/v1.0/<start>/<end>")
def roomrate(start,end):
    roomrate_q = session.query(Paris.realSum, Paris.bedrooms, Paris.guest_satisfaction_overall)\
        .filter(Paris.realSum >= start).filter(Paris.realSum <= end)\
        .all()
    roomrate_l = []
    for rate, bedrooms, rating in roomrate_q:
        roomrate_d = {}
        roomrate_d["realSum"] = rate
        roomrate_d["bedrooms"] = bedrooms
        roomrate_d["guest_satisfaction_overall"] = rating
        roomrate_l.append(roomrate_d)

    return jsonify(roomrate_l)

if __name__ == '__main__':
    app.run(debug=True)
    
