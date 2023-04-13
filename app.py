

from flask import Flask,jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
import numpy as np
import datetime as dt
import sqlite3

engine = create_engine("weekday_airbnb_EU.db")

Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)