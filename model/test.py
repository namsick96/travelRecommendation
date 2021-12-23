from flask import Flask, request, jsonify
import model


app = Flask(__name__)

dbs = [
    model.DB("tourism.csv", "score.csv"),
    model.DB("restaurant.csv", "score.csv"),
    model.DB("bar.csv", "score.csv"),
]


@app.route("/", methods=["POST"])
def index():
    content = request.json
    model.main(content, dbs)
    return jsonify(content)


app.run(host="0.0.0.0", port=8081)
