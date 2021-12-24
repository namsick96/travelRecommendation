from flask import Flask, request, jsonify
import model
import json

app = Flask(__name__)

dbs = [
    model.DB("tourism.csv", "score.csv"),
    model.DB("restaurant.csv", "score.csv"),
    model.DB("bar.csv", "score.csv"),
]


@app.route("/", methods=["POST"])
def index():
    content = request.json

    result_dict = model.main(content, dbs)
    result = {
        "type": content["type"],
        "first": result_dict[0][0],
        "second": result_dict[0][1],
        "third": result_dict[0][2],
        "restaurant1": result_dict[1][0],
        "restaurant2": result_dict[1][1],
        "restaurant3": result_dict[1][2],
        "alcohol1": result_dict[2][0],
        "alcohol2": result_dict[2][1],
        "alcohol3": result_dict[2][2],
    }

    return json.dumps(result)


app.run(host="0.0.0.0", port=8081)
