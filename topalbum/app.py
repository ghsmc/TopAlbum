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
        params={"ids": "4aawyAB9vmqN3uQ7FjRGTy,0sNOF9WDwhWunNAHPD3Baj"},
        headers={"Authorization": SPOTIFY_AUTHORIZATION},
    ).json()
    print(album_information)
    albums = album_information["albums"]

    #   artistname = album["artists"][0]["name"]
    #     albumname = album["name"]
    #     albumcover = album["images"][0]["url"]
    #     albumpopularity = album["popularity"]
        
    # move code from getalbum here, reference them
    #pass an array of dictionaries

    n = random.randint(0,22)
    

    return render_template("index.html", albums=albums)



app.run(debug=True)
