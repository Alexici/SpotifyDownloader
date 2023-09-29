def greeting():
    print("""
    Hello and welcome to Spotify Scraper! This program requires a spotify playlist ID in order to download a set number of songs from that playlist.\n
    The maximum amount is 100 songs and the download always starts from the first added song in the playlist - This cannot be changed due to the way the Spotify API works (or I am just too dumb to figure it out)\n
    The program will download the songs in the Downloads folder in a folder called Songs. (Plans to make this customizable are not in the works)\n
    What is the playlist ID you might ask, well let me give you an example:\n
    playlist link: https://open.spotify.com/playlist/37i9dQZF1DXa2PvUpywmrr?si=c3fba014a920434f\n
    the playlist ID is the part after playlist/ and before the question mark, so in this case it is 37i9dQZF1DXa2PvUpywmrr\n
          
    Please enter the playlist ID in order to continue with the download
""")
    playlist_id = input("Playlist ID: ")
    return playlist_id