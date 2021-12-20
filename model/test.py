from flask import Flask, request, jsonify
import model

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    content = request.json
    model.getCourse(content)
    return jsonify(content)


app.run(host="0.0.0.0", port=8081)
