from pytube import YouTube, Search
from download_location import get_download_path
import json
from os import getlogin


#make a python dict from the songs.json file

def open_json_file() -> dict:
    file = open("songs.json", "r")
    json_data = json.load(file)
    file.close()
    return json_data

# Search the song on youtube

def get_song_url(i):
    song = open_json_file()[f'{i}']["song"]
    s = Search(song)
    url = s.results[0].watch_url
    return url

# Download the song from youtube and convert it to mp3, also save it in the download location
def download_song(url):
    download_path = get_download_path(getlogin())
    yt = YouTube(url)
    yt.streams.get_audio_only().download(download_path)

# Loop through the json file and download each song
def download_songs_from_playlist():
    json_data = open_json_file()
    for i in range(len(json_data)):
        url = get_song_url(i)
        download_song(url)
        print(f"{json_data[f'{i}']['song']} finished downloading, {len(json_data) - i - 1} left to go!")


    



