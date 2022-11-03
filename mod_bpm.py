import sys
from os.path import exists
from spotify import Song


'''
This program modifies the beat per minute (bpm) of songs in <input_file>:

Call to program
python3 mod_bpm.py <relative_bpm>
    
Input
    <relative_bpm>: integer
    top50.csv: datafile
    
Output
    top50_mod.csv: datafile

Information about headers in datafile
0: track name
1: artist name
2: genre
3: beats per minute
4: energy
5: danceability
6: length

Details are described at https://aprendepython.es/miniprojects/spotify/.
Designed by Sergio Delgado Quintero.

Developed by:
Elise Louma Bouarouk
Maryam Barra Bouchemla
'''

if __name__ == '__main__':
    # check top50.csv exists
    if exists('top50.csv'):
        input_file = 'top50.csv'
    else:
        print('The input file top50.csv does not exist in the current folder')
    output_file = 'top50_mod.csv'
    
    # read keyboard input
    try:
        relative_bpm = int(sys.argv[1])
    except Exception:
        print('Error: Integer expected as argument...')
        
    # load songs (from input_file)
    songs = Song.load_songs(input_file)
    
    # change speed of all songs
    for song in songs:
        Song.change_speed(song, relative_bpm)
   
    # save songs (to output_file)
    try:
        Song.save_songs(songs, output_file)
        print(f'Modified songs have been successfully stored in {output_file}')
    except Exception:
        print('Ups. Something went wrong.')
