# Copyright (C) 2011 Jayson Vaughn (vaughn.jayson@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import urllib
from mp3_handler import MP3Handler
from lastfm_downloader import LastFMDownloader


class MediaDirWalker(object):
    def __init__(self, path, overwrite = False):
        """ Initialize Media directory walker object"""

        self.path = path #Media Path that will be recurisvely traverse
        self.downloader = None #Which Downloader object to use? (LastFM)
        self.filehandler = None #Which File Handler to use? (MP3)
        self.overwrite = overwrite

    def do_walk_path(self):
        """ Walk specified directory recursively.  Call self.process_dir() on each directory """

        os.path.walk(self.path, self.process_dir, None)

    def process_dir(self, args, dirname, filenames):
        """ callback for each directory encourted by os.path.walk.
            If directory contains mp3, search and download it's cover art"""
        
        album_name = ""
        artist_name = ""

        # If we have files in the directory
        if filenames:
            for file in filenames:
                if "mp3" in file:
                    self.filehandler = MP3Handler(dirname, filenames) # Set the File Handler to be MP3
                    break
                    
            # If we have a file handler, then continue
            if self.filehandler:
                # If the directory actually contains MP3s (or whatever media file extension) then continue
                if self.filehandler.audio_files:
                    (album_name, artist_name) = self.filehandler.get_album_and_artist() # Lookup album and artist ID3 tag

                    # If ID3 tag exists and we have an album name
                    if album_name:
                        self.downloader = LastFMDownloader(album_name, artist_name) # Set downloader type to be LastFM
                        image_url = self.downloader.search_for_image() # Search for cover image, return URL to download it
                        # If we found the image URL, then download the image.
                        if image_url:
                            self.download_image(dirname, image_url)


    def download_image(self, dirname, image_url):
        """ Check if overwrite is enabled.  Check if cover.png already exists
        Call method to download album cover art image to specified directory"""

        # Does cover.png already exist?  
        if os.path.exists(os.path.join(dirname, "cover.png")):
            # If overwrite is set to True, then go ahead and re-download cover.png
            if self.overwrite:
                self.do_download(dirname, image_url)
            else:
                print("!! Cover already exists in {0}".format(dirname))
        else:
            # If cover.png doesn't exist, go ahead and download
            self.do_download(dirname, image_url)

    def do_download(self, dirname, image_url):
        """ Download album cover art and save as cover.png"""

        print("Downloading album to {0}".format(dirname))
        image_data = urllib.urlopen(image_url).read()
        f = open(os.path.join(dirname, "cover.png"), 'w')
        f.write(image_data)
        f.close()
