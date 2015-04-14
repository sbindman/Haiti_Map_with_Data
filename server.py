from flask import Flask, render_template, redirect, request, session, flash, url_for, jsonify
import model
import os
from sqlalchemy import and_


app = Flask(__name__)

PORT=int(os.environ.get("PORT" ,5000))


@app.route("/")
def index():
    ''' generates geojson data from the db '''

    coordinates = model.getPOIs()

    return render_template("name.html", coordinates=coordinates)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0" ,port=PORT)
