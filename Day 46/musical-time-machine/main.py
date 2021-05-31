from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")

response = requests.get(URL + date_input)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

print(song_names)

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope=scope,
    cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_uris = []
for song_name in song_names:
    search_result = sp.search(q=f"track:{song_name} year:{date_input.split('-')[0]}", type="track")
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} not found in Spotify. Skipped.")

playlist_name = f"{date_input} Billboard 100"
playlist_creation = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Created from Python code with song scrapped from Billboard website for the week of {date_input}")

playlist_id = playlist_creation["id"]
print("---")
print(f"Playlist {playlist_name} created")
print(f"Adding tracks to {playlist_name} playlist...")
add_tracks_to_playlist = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

if add_tracks_to_playlist["snapshot_id"] is not None:
    print(f"Tracks added to {playlist_name} playlist successfully!")
