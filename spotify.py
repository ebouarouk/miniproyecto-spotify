class Song:
    def __init__(self, track: str, artist: str, genre: str, bpm: int,
                 energy: int, danceability: int, length: int) -> None:
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self) -> str:
        return f"{self.track},{self.artist},{self.genre},{self.bpm},{self.energy},{self.danceability},{self.length}"
        # need to shorten string without breaking format

    def change_speed(self, relative_bpm: int) -> None:
        self.bpm += relative_bpm
        self.energy += 2 * relative_bpm
        self.danceability += 3 * relative_bpm
        self.length -= relative_bpm
        # necesita comprobar resultado con relative_bpm negativo
        
    @staticmethod
    def load_songs(path: str) -> list:
        f = open(path)
        songs = []
        for line in f:
            song = line.split(',') # convert string line to list of str
            [song.append(int(element)) for element in song[3::]] # convert to int and append  
            song = song[0:3] + song[7::] # remove str duplicates
            songs.append(Song(*song)) # create instances and append to list
        return songs

    @staticmethod
    def save_songs(songs: list, path: str) -> None:
        # if folder exists
        f = open(path, 'w')
        for song in songs:
            f.write(Song.__str__(song) + '\n')


### testing
'''
path = '/home/ebouarouk/miniproyecto-spotify/top50.csv'
songs = Song.load_songs(path)
for object in songs:
    print(Song.__str__(object))

'''
