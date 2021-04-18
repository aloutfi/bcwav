#!/usr/bin/env python3

import os
import music_tag
import sys

def bcwav(directory):
    for _filename in os.listdir(directory):
        if _filename.endswith("wav"):
            file = music_tag.load_file(f'{directory}{_filename}')
            filename = _filename.split(' - ')

            file['artist'] = filename[0]
            file['album'] = filename[1]
            file['tracknumber'] = filename[-1][0:2]
            file['discnumber'] = filename[-1][0:2]
            file['tracktitle'] = filename[-1][3:-4]
            file.save()
            track_name = filename[-1][3:]
            os.rename(f'{directory}{_filename}', f'{directory}{track_name}')


if __name__ == "__main__":
    directory = sys.argv[1:][0]
    if os.path.exists(directory):
        bcwav(directory)
