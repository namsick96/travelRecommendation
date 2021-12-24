function csvToJSON(csv_string) {
  const rows = csv_string.split("\r\n");
  const jsonArray = [];
  for (let i = 1; i < rows.length; i++) {
    let row = rows[i].split(",");
    jsonArray.push(row[0]);
  }

  return jsonArray;
}

const fs = require("fs");
const file_csv = fs.readFileSync(
  "/Users/eunddodi/Desktop/conference/travelRecommendation/frontend/src/data/name_place.csv"
);

const string_csv = file_csv.toString();
const arr_json = csvToJSON(string_csv);
const string_json = JSON.stringify(arr_json);
fs.writeFileSync("placeList.json", string_json);
