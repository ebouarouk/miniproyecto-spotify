import sys

from spotify import Song


'''Information about headers in datafile
0: track name
1: artist name
2: genre
3: beats per minute
4: energy
5: danceability
6: length'''

# poner el path hacia la carpeta de Maryam 
folder_path = '/home/ebouarouk/miniproyecto-spotify/'
# quitar esto y llamar al path de la carpeta

if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(sys.argv[1])  # read keyboard input

    # load songs (from input_file)
    songs = Song.load_songs(folder_path + input_file)
    
    # change speed of all songs
    for song in songs:
        Song.change_speed(song, relative_bpm)

    # save songs (to output_file)
    Song.save_songs(songs, folder_path + output_file)
