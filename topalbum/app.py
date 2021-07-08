from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests
import random
import spotify_auth

load_dotenv()

SPOTIFY_AUTHORIZATION = spotify_auth.get_bearer_token()

app = Flask(__name__)


@app.route("/")
def home():
    album_information = requests.get(
        "https://api.spotify.com/v1/albums",
        params={"ids": "3XLn9BkDkwq4icsUye2Krp,1oNWum7uuaISS4cSgDQhWT,2If8WvHmIANFsGWDf36e2M,2vmjRfAgNyYIiFsHuUU8u9"},
        headers={"Authorization": SPOTIFY_AUTHORIZATION},
    ).json()

    print(album_information)
    albums = album_information["albums"]

    i = random.randint(0, 3)
    j=random.randint(0,3)
    
    while j == i:
        j = random.randint(0, 3)

    album1 = album_information["albums"][i]
    album2 = album_information["albums"][j]

    albumdate1 = album1["release_date"]
    albumdate2 = album2["release_date"]

    name1 = album1["name"]
    name2 = album2["name"]

    popularity1 = album1["popularity"]
    popularity2 = album2["popularity"]

    image1 = album1["images"][0]["url"]
    image2 = album2["images"][0]["url"]

    

    #   artistname = album["artists"][0]["name"]
    #     albumname = album["name"]
    #     albumcover = album["images"][0]["url"]
    #     albumpopularity = album["popularity"]
        
    # move code from getalbum here, reference them
    #pass an array of dictionaries

    n = random.randint(0,22)
    

    return render_template("index.html", album1=album1, album2=album2, image1=image1, image2=image2, name1=name1, name2=name2, popularity1=popularity1, popularity2=popularity2)



app.run(debug=True)
