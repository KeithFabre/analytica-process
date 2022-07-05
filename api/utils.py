import requests
import json
from datetime import date


today = date.today()
def ageCalc(birthday, date=today):   
    
     # to extract from str
    str_birth = str(birthday)
    str_date = str(date)

    # slicing to get fraction and turing to int to calc
    y = int(str_birth[0:4])
    m = int(str_birth[5:7])
    d = int(str_birth[8:10])

    Y = int(str_date[0:4])
    M = int(str_date[5:7])
    D = int(str_date[8:10])
    
    # diff with corrections
    days = (31 + (D - d)) if (D < d) else (D - d)

    months = (12 + (M - m)) if (M < m) else (M - m)
    if (D < d):
        months-=1

    years = (Y - y) if ((M - m) == 0) else ((Y - y) - 1)
    
    return years

def getArtistId(artist_name):
    
    APIKEY = 2 # API KEY for tests 

    url = 'https://theaudiodb.com/api/v1/json/{}/search.php?s={}'.format(APIKEY, artist_name)

    response = requests.get(url)

    id = response.json()['artists'][0]['idArtist']

    return id

def getArtistLatestAlbum(artist_id):

    APIKEY = 2 # API KEY for tests 

    # returns all albums    
    url = "https://theaudiodb.com/api/v1/json/{}/album.php?i={}".format(APIKEY, artist_id)

    response = requests.get(url)

    albums = response.json()['album']

    album_info = []

    for album in albums:
        
        idAlbum = album['idAlbum']
        yearAlbum = album['intYearReleased']
        nameAlbum = album['strAlbum']

        # associates album id with album year
        info = { 'id': idAlbum, 'year': yearAlbum, 'name': nameAlbum }

        album_info.append(info)

    # get highest year value
    album_year = max(d['year'] for d in album_info)

    # get id for highest year value
    id_latest = [d['id'] for d in album_info if d['year'] == album_year ]

    album_latest = [{ 'id': d['id'], 'name': d['name'] } for d in album_info if d['year'] == album_year ]


    return album_year, album_latest

def getAlbumTracks(album_latest):

    APIKEY = 2 # API KEY for tests 

    ids = [a['id'] for a in album_latest]

    # if more than one id for one year check if there are singles
    if len(ids) > 1:
        for id in ids:
            url = "https://theaudiodb.com/api/v1/json/{}/track.php?m={}".format(APIKEY, id)

            response = requests.get(url)

            tracks = response.json()['track']

            # check if its a single
            if len(tracks) == 1:
                full_album = None
            
            # if not a single then store the latest album
            elif len(tracks) > 1:
                full_album = tracks # not a single, full album

    # only one id -- no further if-statement necessary
    else:
        id = ids[0]
        url = "https://theaudiodb.com/api/v1/json/{}/track.php?m={}".format(APIKEY, id)

        response = requests.get(url)

        tracks = response.json()['track']
    
    # create dict with number and name of every track

    return tracks


artist_name = "coldplay"

art_id  = getArtistId(artist_name)

album_year = getArtistLatestAlbum(art_id)[0]
album_latest = getArtistLatestAlbum(art_id)[1]

album_tracks = getAlbumTracks(album_latest)
print(album_tracks)

