import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import statistics as s

import matplotlib.pyplot as p
cid = 'dbed050e59224dd6966833101f62e199'
secret = 'd4cf877e4dfb4d58a31f164d16f002e9'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


uris = {'bts':['spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX',(1,0,0),[]],
		'jagjit singh': ['spotify:artist:2ijWbN5KykTYiBoVmhzCTU',(0,1,0),[]],
		'mozart':['spotify:artist:4NJhFmfw43RLBLjQvxDuRS',(0,0,1),[]],
		'metallica': ['spotify:artist:2ye2Wgw4gimLv2eAKyk1NB',(1,0.9,0.5),[],],
		'ed sheeran':['spotify:artist:6eUKZXaKkcviH0Ku9w2n3V',(1,0.5,0.9),[]]}

graph_stuff = {(1,0,0),(0,1,0),(0,0,1),(1,0.9,0.5),(1,0.5,0.9)}



for uri in uris:
	albums = sp.artist_albums(uris[uri][0], album_type=None, country=None, limit=None, offset=0)
	
	for i in range(0,len(albums)):
		t = albums['items'][i]['uri']
		tracks = sp.album_tracks(t, limit=None, offset=0)
		for j in range(0,len(tracks)):
			# print('name:' + tracks['items'][j]['name'])
			# print('uri:' + tracks['items'][j]['uri'])
			track_uri=tracks['items'][j]['uri']
			energy = sp.audio_features(tracks=[track_uri])[0]['danceability ']
			#print('energy:' + str(energy))
			uris[uri][2].append(energy)
	print("Average energy of "+ uri + " songs:"+str(s.mean(uris[uri][2])))
	
for uri in uris:
	p.plot(uris[uri][2], '*',color=uris[uri][1])
p.show()


	

			




    


