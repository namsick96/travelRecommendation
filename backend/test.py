from flask import Flask,request,jsonify
import kakaoMapRoute

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    content=request.json
    return jsonify(content)

app.run(host = '127.0.0.1', port=8081)
