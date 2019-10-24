# import Flask
from flask import Flask

# Create an app, being sure to pass __name__
app = Flask(__name__)


# Define what to do when a user hits the index route
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
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/stations")
def stations():
    print("Requesting aid from defenders..")
    return "Help me!! Aliens are attacking!!"

@app.route("/api/v1.0/tobs")
def tobs_obs():
    print("Requesting aid from defenders..")
    return "Help me!! Aliens are attacking!!"

@app.route("/api/v1.0/<start>")
def start_only():
    return "Help me!! Aliens are attacking!!"

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return "Help me!! Aliens are attacking!!"

if __name__ == "__main__":
    app.run(debug=True)




* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Hints

* You will need to join the station and measurement tables for some of the analysis queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.