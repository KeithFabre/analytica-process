from flask import Flask, request, jsonify
from utils import ageCalc

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # prevents jsonify from sorting

@app.route("/age", methods=["POST"])
def age():
    
    request_data = request.get_json(force=True)

    name = None
    birthdate = None
    date = None

    if request_data:
        if "name" in request_data:
            name = request_data["name"]

        if "birthdate" in request_data:
            birthdate = request_data["birthdate"]

        if "date" in request_data:
            date = request_data["date"]
    
    ageNow = ageCalc(birthdate)
    ageThen = ageCalc(birthdate, date)

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    formatted_date = day + '/' + month + '/' + year
    
    quote = 'Olá, {}! Você tem {} anos e em {} você terá {} anos.'.format(name, ageNow, formatted_date, ageThen)

    data = {
            "quote": quote, 
            "ageNow": ageNow,
            "ageThen": ageThen
            }
    
    return jsonify(data)

@app.route("/album-info", methods=["GET"])
def album_info():
    
    artist = str(request.args.get('artist'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")