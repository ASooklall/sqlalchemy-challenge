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
Passenger = Base.classes.passenger

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
    # Create our session (link) from Python to the DB
    session = Session(engine)

#   * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

#   * Return the JSON representation of your dictionary.
    results = session.query(Measurements.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations():
#   * Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/tobs")
def tobs_obs():
#   * query for the dates and temperature observations from a year from the last data point.
#   * Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/<start>")
def start_only():

#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>/<end>")
def start_end():
#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
if __name__ == "__main__":
    app.run(debug=True)


# ## Hints

# * You will need to join the station and measurement tables for some of the analysis queries.

# * Use Flask `jsonify` to convert your API data into a valid JSON response object.