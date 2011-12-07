# Copyright (C) 2011 Jayson Vaughn <vaughn.jayson@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import mutagen
from mutagen.oggvorbis import OggVorbis

class OGGHandler(object):
    def __init__(self, dirname, filenames):
        """ Initialize OggVorbis Handler """

        self.dirname = dirname #Name of directory
        self.filenames = filenames #List of filenames found in directory
        # Create audio_files list from the filenames list by filtering for only ogg files 
        self.audio_files = [os.path.join(dirname, file) for file in filenames if ".ogg" in file]

    def get_album_and_artist(self):
        """ Return Ogg tags for album and artist"""

        self.audio_files.sort()

        for file in self.audio_files:
            try:
                tags = OggVorbis(file)
                if tags:
                    if "album" in tags.keys() and "artist" in tags.keys():
                        return (tags["album"][0], tags["artist"][0])
                        break # If we found ID3 tag info from a file, no reason to query the rest in a directory.  
            except mutagen.oggvorbis.OggVorbisHeaderError:
                continue
        return (None, None)
