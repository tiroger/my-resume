
from flask import Flask, jsonify, render_template, jsonify, url_for, json
import os

# To Return json of scores
import json

app = Flask(__name__, template_folder='.')


@app.route("/")
def index():
    """Returns the homepage"""
    return render_template("index.html")

@app.route('/skills')
def skills():
    filename = os.path.join(app.static_folder, 'skills.json')
    with open(filename) as skills:
        skills = json.load(skills)

    return skills

@app.route('/timeline')
def timeline():
    filename = os.path.join(app.static_folder, 'timeline.json')
    with open(filename) as timeline:
        timeline = json.load(timeline)

    return jsonify(timeline)


if __name__ == "__main__":
     app.run(debug=True)
