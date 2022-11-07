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
        'Return a string of attributes separated by comma'
        return f"{self.track},{self.artist},{self.genre},{self.bpm},{self.energy},{self.danceability},{self.length}"

    def change_speed(self, relative_bpm: int) -> None:
        'Modify the beat per minute of the Song instance and update attributes'
        self.bpm += relative_bpm
        self.energy += 2 * relative_bpm
        self.danceability += 3 * relative_bpm
        self.length -= relative_bpm
        
    @staticmethod
    def load_songs(path: str) -> list:
        'Return a list of Song instances created for each line of the file'
        f = open(path)
        songs = []
        for line in f:
            song = line.split(',')
            [song.append(int(element)) for element in song[3::]] # convert int
            song = song[0:3] + song[7::]
            songs.append(Song(*song)) # create Song instance
        return songs

    @staticmethod
    def save_songs(songs: list, path: str) -> None:
        'Create a datafile of Song instances at path'
        f = open(path, 'w')
        for song in songs:
            f.write(Song.str(song) + '\n')
