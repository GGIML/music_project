import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd

USERNAME = '263a95d0f58b4e289109c4bac025c9b7'
KEY = 'a4797bcca8cd460f81e29815cdbaed7b'

auth_manager = SpotifyClientCredentials(client_id=USERNAME, client_secret=KEY)
sp = spotipy.Spotify(client_credentials_manager=auth_manager)

def getIDfromsearch(track_name, artist):
    if '/' in track_name:
        track_name = track_name.split('/')[0]
    result = sp.search(q=f'track:{track_name} artist:{artist}', type='track', limit=1)
    if result['tracks']['items'] == []:
        idd = None
    idd = result['tracks']['items'][0]['id']
    return idd

def getTrackFeatures(idd):
    meta = sp.tracks(idd)
    features = sp.audio_features(idd)

    tracks_dict = {'name': meta['tracks'][0]['name'],
                  'album': meta['tracks'][0]['album']['name'],
                  'artist': meta['tracks'][0]['album']['artists'][0]['name'],
                  'release_date':meta['tracks'][O]['album']['release_date'],
                  'popularity': meta['tracks'][j]['popularity'],
                  'duration_ms':features[0]['duration_ms'],
                  'key':features[0]['key'],
                  'mode':features[0]['mode'],
                  'time_signature':features[0]['time_signature'],
                  'acousticness':features[0]['acousticness'],
                  'danceability':features[0]['danceability'],
                  'energy':features[0]['energy'],
                  'instrumentalness':features[0]['instrumentalness'],
                  'liveness':features[0]['liveness'],
                  'loudness':features[0]['loudness'],
                  'speechiness':features[0]['speechiness'],
                  'valence':features[0]['valence'],
                  'tempo':features[0]['tempo']}
    
    tracks = pd.DataFrame(tracks_dict)
    return tracks