import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date = input("what year you would like to travel to? (YYYY-MM-DD)")
#
# year = date.split("-")[0]
# month = date.split("-")[1]
# day = date.split("-")[2]

link = f'https://www.billboard.com/charts/hot-100/2007-08-04'
client_ID = '1c450551523348389bf88cca8ca7f115'
client_secret = '307472b2f0f34414a08c53e6b3424f56'
scope = "playlist-modify-private"
redirect_uri = "http://example.com"

response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')
titles = soup.select("li h3#title-of-a-story")
songs = [title.text.replace("\n", "").replace("\t", "") for title in titles]
print(songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_ID,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='22obn4noqi5gbohbdic4edjti',
    )
)

user_id = sp.current_user()["id"]
song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:2000", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
playlist = sp.user_playlist_create(
    user=user_id,
    name="2007-04-08 Billboard 100",
    public=False,
    collaborative=False,
    description='Made by Eugenio Gonzalez Morales'
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist["id"])
