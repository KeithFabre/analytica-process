from flask    import Flask, request, jsonify
from utils    import ageCalc, getArtistInfo, getArtistLatestAlbum, getAlbumTracks
from datetime import date

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # prevents jsonify from sorting

@app.route("/age", methods=["POST"])
def age():
    
    request_data = request.get_json(force=True)
    today = str(date.today())

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
            if str(date) == str(today):
                return 'Forneça uma data futura'
    
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

    if artist == None:
        return "No artist name provided"
    else:
        art_id  = getArtistInfo(artist)[0]             # artist id        
        artist_name = getArtistInfo(artist)[1]         # artist name
        
        album_year = getArtistLatestAlbum(art_id)[0]   # year of latest albums        
        album_latest = getArtistLatestAlbum(art_id)[1] # album id and name from year of latest release

        album_tracks = getAlbumTracks(album_latest)[0] # tracks from lastest album        
        album_id = getAlbumTracks(album_latest)[1]     # album id of latest album with described tracks

        # album name of latest album with described tracks
        album_name = [a['name'] for a in album_latest if a['id'] == album_id][0]

    data = {
            "artist":       artist_name, 
            "latest-album": album_name,
            "album-year":   int(album_year),
            "album-tracks": album_tracks
            }
    
    return jsonify(data)





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")