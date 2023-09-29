from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Get the token from spotify API
def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token =json_result["access_token"]
    return token

# Get the header for the request
def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def get_playlist_items(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=RO&fields=items%28track%28name%2Cid%2Cartists%28name%29%29%29&limit=100"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    print(json_result)
    return json_result

# def get_track_info(token, track_id):
#     url = f"https://api.spotify.com/v1/tracks/{track_id}"
#     headers = get_auth_header(token)
#     result = get(url, headers=headers)
#     json_result = json.loads(result.content)
#     return json_result


def save_playlist_data(playlist_id):
    playlist_items = get_playlist_items(token, playlist_id)
    print("TOTAL LENGTH OF THE PLAYLIST: ", len(playlist_items))
    all_songs = {}
    # Loop through the playlist and get the id of each track
    # The loop is also storing the details of each track in a separate file
    for i in range(len(playlist_items)):
        # print(playlist_items[i]["track"]["artists"][0]["name"])
        # print(playlist_items[i]["track"]["name"])
        # print(playlist_items[i]["track"]["id"])
        # print("-----------------")
        all_songs[i] = {
            "song" : f"{playlist_items[i]['track']['name']} - {playlist_items[i]['track']['artists'][0]['name']}"
    }
    # Make a json file with the artist and song name of each track
    with open("songs.json", "w+") as f:
        json.dump(all_songs, f, indent=4)

token = get_token()