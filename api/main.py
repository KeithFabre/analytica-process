from flask import Flask

app = Flask(__name__)
app.run(debug=True)

'''
    POST with json req and res
    in: 
        - name (str)
        - birthdate (date)
        - date (date)
    out: 
        - quote (str)
        - ageNow (int)
        - ageThen (int)
'''
@app.route('/age', methods=['POST'])
def age():
    pass

'''
    GET with query req and json res
    in: 
        - artist
    out:
        - artist (str)
        - latest-album (str)
        - album-year (int)
        - album-tracks (dict)
    
'''
@app.route('/album-info', methods=['GET'])
def album_info():
    pass