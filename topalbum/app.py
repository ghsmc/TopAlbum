from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests
import random
import spotify_auth

load_dotenv()

SPOTIFY_AUTHORIZATION = spotify_auth.get_bearer_token()

app = Flask(__name__)

album_information = requests.get(
    "https://api.spotify.com/v1/albums",
    params={
        "ids": "2vmjRfAgNyYIiFsHuUU8u9,1ATL5GLyefJaxhQzSPVrLX,0S0KGZnfBGSIssfF54WSJh,5zi7WsKlIiUXv09tbGLKsE,3arNdjotCvtiiLFfjKngMc,392p3shh2jkxUxY2VHvlH8,0ptlfJfwGTy0Yvrk14JK1I,6pwuKxMUkNg673KETsXPUV,41GuZcammIkupMPKH2OJ6I"
    },
    headers={"Authorization": SPOTIFY_AUTHORIZATION},
).json()


@app.route("/")
def home():
    albums = album_information["albums"]

    album1 = random.choice(albums)
    album2 = random.choice(albums)
    while album1 == album2:
        album2 = random.choice(albums)

    name1 = album1["name"]
    name2 = album2["name"]

    popularity1 = album1["popularity"]
    popularity2 = album2["popularity"]

    artist1 = album1["artists"]
    aritst2 = album2["artists"]

    image1 = album1["images"][0]["url"]
    image2 = album2["images"][0]["url"]

    return render_template(
        "index.html",
        album1=album1,
        album2=album2,
        image1=image1,
        image2=image2,
        name1=name1,
        name2=name2,
        popularity1=popularity1,
        popularity2=popularity2,
    )


app.run(debug=True)
