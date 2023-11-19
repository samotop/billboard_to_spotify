import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#User info
SHOPIFY_CLIENT_ID = "PUT YOUR CLIENT ID HERE"
SHOPIFY_CLIENT_SECRET = "PUT YOUR CLIENT SECRET HERE"
REDIRECT_URI = "http://example.com"

#Scraping Billboard 100
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{travel_date}/")
content = response.text
soup = BeautifulSoup(content, "html.parser")
billboard_songs = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in billboard_songs]

#Spotify Authentication
scope = "playlist-modify-private"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SHOPIFY_CLIENT_ID,
                                                    client_secret=SHOPIFY_CLIENT_SECRET,
                                                    redirect_uri=REDIRECT_URI))
user_id = spotify.current_user()["id"]

#Creating a new private playlist in Spotify
playlist = spotify.user_playlist_create(user_id, f"{travel_date} Billboard 100", public=False)

#Searching Spotify for songs by title
YYYY = travel_date.split("-")[0]
spotify_uris = []
for name in song_names:
    try:
        search_result = spotify.search(q=f"(track:{name}year:{YYYY})", type="track", limit=1)
        spotify_uris.append(search_result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

#Adding songs found into the new playlist
spotify.user_playlist_add_tracks(user=user_id, tracks=spotify_uris, playlist_id=playlist["id"])
