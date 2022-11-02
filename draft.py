def load_songs(path: str):
    f = open(path)
    songs = []
    for line in f:
        song = line.split(',')
        print(song)
        # songs.appen(Song(track: str, artist: str, genre: str, bpm: int,
        #         energy: int, danceability: int, length: int))
        [song.insert(index, int(element)) for index, element in song[3::]]    
        song = song[0:3] + song[7::]
        #Song(*song)
        print(song)
        break
    return songs

load_songs('/home/ebouarouk/miniproyecto-spotify/top50.csv')