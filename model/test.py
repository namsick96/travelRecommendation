from flask import Flask, request, jsonify
import model
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    content = request.json
    model.getCourse(content)
    data={"type":1, "first":"윗새오름", "second": "제주시청", "third": "넥슨컴퓨터박물관","restaurant1":"레스토랑 이름1","restaurant2":"레스토랑 이름2","restaurant3":"레스토랑 이름3","alchol1":"술집 이름1","alchol2":"술집 이름2","alchol3":"술집 이름3"}
    jsonData=json.dumps(data,ensure_ascii=False,indent="\t")
    print(jsonData)
    
    return jsonData


app.run(host="0.0.0.0", port=8081)
