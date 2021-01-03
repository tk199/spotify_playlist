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


user_input = input('Enter the song:')
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    #print(json.dumps(result,sort_keys=4,indent=4))
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input('Enter the song: ')

#find playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#add songs

spotifyObject.playlist_add_items(playlist_id=playlist, items=list_of_songs)

