class Song:
    def __init__(self, track: str, artist: str, genre: str, bpm: int,
                 energy: int, danceability: int, length: int):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self):
        # __str__
'''El formato de salida debe ser una línea con los campos separados por comas, 
tal y como está definido en el fichero de entrada.'''

    def change_speed(self, relative_bpm: int) -> None:
        # your code here

    @staticmethod
    def load_songs(path: str) -> list['Song']:
        # your code here
        return songs

    @staticmethod
    def save_songs(songs: list['Song'], path: str) -> None:
        # your code here