from flask import Flask, request, jsonify
import model
import json
<<<<<<< HEAD
=======

>>>>>>> tR-4

app = Flask(__name__)

dbs = [
    model.DB("tourism.csv", "score.csv"),
    model.DB("restaurant.csv", "score.csv"),
    model.DB("bar.csv", "score.csv"),
]


@app.route("/", methods=["POST"])
def index():
    content = request.json
<<<<<<< HEAD
    model.getCourse(content)
    data={"type":1, "first":"윗새오름", "second": "제주시청", "third": "넥슨컴퓨터박물관","restaurant1":"레스토랑 이름1","restaurant2":"레스토랑 이름2","restaurant3":"레스토랑 이름3","alchol1":"술집 이름1","alchol2":"술집 이름2","alchol3":"술집 이름3"}
    jsonData=json.dumps(data,ensure_ascii=False,indent="\t")
    print(jsonData)
    
    return jsonData
=======

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
>>>>>>> tR-4


app.run(host="0.0.0.0", port=8081)
