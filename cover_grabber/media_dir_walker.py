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
import urllib
from mp3_handler import MP3Handler
from ogg_handler import OGGHandler
from flac_handler import FLACHandler
from lastfm_downloader import LastFMDownloader


class MediaDirWalker(object):
    def __init__(self, path, overwrite = False):
        """ Initialize Media directory walker object"""

        self.path = path #Media Path that will be recurisvely traverse
        self.overwrite = overwrite

    def do_walk_path(self):
        """ Walk specified directory recursively.  Call self.process_dir() on each directory """

        print("Scanning: {path}".format(path=self.path))
        os.path.walk(self.path, self.process_dir, None)

    def process_dir(self, args, dirname, filenames):
        """ callback for each directory encourted by os.path.walk.
            If directory contains mp3, search and download it's cover art"""
        
        album_name = ""
        artist_name = ""
        filehandler = None
        
        # If we have files in the directory
        if filenames:
            for file in filenames:
                if ".mp3" in file:
                    filehandler = MP3Handler(dirname, filenames) # Set the File Handler to be MP3
                    break

                if ".ogg" in file:
                    filehandler = OGGHandler(dirname, filenames) # Set the File Handler to be OGG
                    break
                    
                if ".flac" in file:
                    filehandler = FLACHandler(dirname, filenames) # Set the File Handler to be OGG
                    break

            # If we have a file handler, then continue
            if filehandler:
                # If the directory actually contains media files then continue
                if filehandler.audio_files:
                    (album_name, artist_name) = filehandler.get_album_and_artist() # Lookup album and artist ID3 tag

                    # If metadata/tags exists and we have an album name
                    if album_name:
                        # check if the cover is already there before making api calls
                        possible_covers = ["cover.png", "cover.jpg", "cover.gif"]
                        for cover_name in possible_covers:
                            if os.path.exists(os.path.join(dirname, cover_name)):
                                print(u'cover image for "{artist_name} - {album_name}" already present, move to next one'.format(artist_name=artist_name, album_name=album_name))
                                return
                        try:
                            downloader = LastFMDownloader(album_name, artist_name) # Set downloader type to be LastFM
                            image_url = downloader.search_for_image() # Search for cover image, return URL to download it
                        except KeyboardInterrupt,e:
                            raise
                        except Exception,e:
                            image_url = None
                            print(u'SOMETHING VERY BAD HAPPENED during processing of "{artist_name} - {album_name}"'.format(artist_name=artist_name, album_name=album_name))
                        # If we found the image URL, then download the image.
                        if image_url:
                            print(u'Downloading album cover image for "{artist_name} - {album_name}"'.format(artist_name=artist_name, album_name=album_name))
                            self.download_image(dirname, image_url)


    def download_image(self, dirname, image_url):
        """ Check if overwrite is enabled.  Check if album cover already exists
        Call method to download album cover art image to specified directory"""

        # Set name of image file based on extension from image URL
        if ".png" in image_url:
            cover_name = "cover.png"
        elif ".jpg" in image_url:
            cover_name = "cover.jpg"
        elif ".jpeg" in image_url:
            cover_name = "cover.jpeg"
        elif ".gif" in image_url:
            cover_name = "cover.gif"
        else:
            return

        # Does cover.(png|jpg|jpeg|gif) already exist?  
        if os.path.exists(os.path.join(dirname, cover_name)):
            # If overwrite is set to True, then go ahead and re-download album cover
            if self.overwrite:
                self.do_download(dirname, image_url, cover_name)
            else:
                print("!! Cover already exists in {0}".format(dirname))
        else:
            # If cover doesn't exist, go ahead and download
            self.do_download(dirname, image_url, cover_name)

    def do_download(self, dirname, image_url, cover_name):
        """ Download album cover art and save as cover.(png|jpg|jpeg|gif)"""

        image_data = urllib.urlopen(image_url).read()
        f = open(os.path.join(dirname, cover_name), 'w')
        f.write(image_data)
        f.close()
