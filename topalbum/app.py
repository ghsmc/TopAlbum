from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests
import spotify_auth

load_dotenv()

SPOTIFY_AUTHORIZATION = spotify_auth.get_bearer_token()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/album")
def getalbum():
    album_information = requests.get(
        "https://api.spotify.com/v1/albums",
        params={
            "ids": "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc",
        },
        headers={"Authorization": SPOTIFY_AUTHORIZATION},
    ).json()
    print(album_information)
    albums = album_information["albums"]

    response = ""

    for album in albums:
        artistname = album["artists"][0]["name"]
        albumname = album["name"]
        albumcover = album["images"][0]["url"]
        albumpopularity = album["popularity"]
        response = (
            response
            + "<p>"
            + albumname
            + " "
            + "("
            + str(albumpopularity)
            + ")"
            + "</p>"
            + '<img src="'
            + albumcover
            + '">'
        )

    return response


app.run(debug=True)
