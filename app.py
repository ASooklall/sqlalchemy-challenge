import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Station API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


# Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precip():

    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    prc_1 = list(np.ravel(results))
#   * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
    all_prc = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prc.append(prcp_dict)

#   * Return the JSON representation of your dictionary.
    return jsonify(all_prc)

@app.route("/api/v1.0/stations")
def stations():
    return("fred")
#   * Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/tobs")
def tobs_obs():
        return("fred")
#   * query for the dates and temperature observations from a year from the last data point.
#   * Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/<start>")
def start_only():
    return("fred")
#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>/<end>")
def start_end():
        return("fred")
#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


if __name__ == "__main__":
    app.run(debug=True)


# ## Hints

# * You will need to join the station and measurement tables for some of the analysis queries.

# * Use Flask `jsonify` to convert your API data into a valid JSON response object.