import json
import requests
import pandas as pd
import os
from tqdm import tqdm

api_key = "76129b4755674eabb8122486664765ab"


def addr_to_lat_lon(addr):
    url = "https://dapi.kakao.com/v2/local/search/address.json?query={address}".format(
        address=addr
    )
    headers = {"Authorization": "KakaoAK " + api_key}
    result = json.loads(str(requests.get(url, headers=headers).text))
    try:
        match_first = result["documents"][0]["address"]
    except IndexError:
        print("no")
        return -1, -1
    else:
        return float(match_first["x"]), float(match_first["y"])


folder = "csv_data"
filelist = os.listdir(folder)


for file in filelist:

    print(file)
    res_df = pd.DataFrame([], columns=["name", "x", "y"])
    fName = file[:-4]
    res = []
    if fName[0] == "c":
        readCSV = pd.read_csv(os.path.join(folder, file), encoding="utf-8")
    else:
        continue
        readCSV = pd.read_csv(os.path.join(folder, file), encoding="utf-8")
    df = readCSV[["이름", "주소"]]
    df = df.dropna(axis=0)

    df.index = list(range(df.shape[0]))
    indexes = df.index.tolist()

    for i in tqdm(indexes):
        x, y = addr_to_lat_lon(df.iloc[i]["주소"])
        print(x, y)
        res_df = res_df.append(
            {"name": df.iloc[i]["이름"], "x": x, "y": y}, ignore_index=True
        )

    res_df.to_csv(os.path.join("csv_result", fName + "_result.csv"))
