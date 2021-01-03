import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'tahak92'


token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)


#create playlist


playlist_name = input("Enter a playlist title: ")

playlist_description = input("Enter a playlist description: ")


spotifyObject.user_playlist_create(user = username, name=playlist_name,public=True, description=playlist_description)
