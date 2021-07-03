import requests
import base64
import os


def get_bearer_token():
    resp = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        headers={
            "Authorization": "Basic "
            + base64.b64encode(
                (
                    os.getenv("SPOTIFY_CLIENT_ID")
                    + ":"
                    + os.getenv("SPOTIFY_CLIENT_SECRET")
                ).encode("utf-8")
            ).decode("utf-8")
        },
    ).json()
    return "Bearer " + resp["access_token"]
