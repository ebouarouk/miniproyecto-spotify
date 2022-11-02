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

if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(sys.argv[1])  # read keyboard input

    # load songs (from input_file)

    # change speed of all songs

    # save songs (to output_file)