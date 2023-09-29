import greet
from downloader import download_songs_from_playlist
from spotify_logic import save_playlist_data

playlist_id = greet.greeting()

save_playlist_data(playlist_id)

download_songs_from_playlist()
