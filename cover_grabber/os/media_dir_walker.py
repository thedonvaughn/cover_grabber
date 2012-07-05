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
from cover_grabber.handler.handler_factory import HandlerFactory
from cover_grabber.downloader.lastfm_downloader import LastFMDownloader
from cover_grabber.logging.config import logger

class MediaDirWalker(object):
    def __init__(self, path, overwrite = False):
        """ Initialize Media directory walker object"""

        self.path = path #Media Path that will be recurisvely traverse
        self.overwrite = overwrite

    def do_walk_path(self):
        """ Walk specified directory recursively.  Call self.process_dir() on each directory """

        logger.info(u'Scanning {path}'.format(path=self.path))
        os.path.walk(self.path, self.process_dir, None)

    def process_dir(self, args, dirname, filenames):
        """ callback for each directory encourted by os.path.walk.
            If directory contains audio files, attempt to extract it's metatags, then search and download it's cover art"""
        
        album_name = ""
        artist_name = ""
        filehandler = None
        
        # If we have files in the directory
        if filenames:
            filehandler = HandlerFactory.get_handler(dirname, filenames) # get proper Handler class based on extension of files

            # If we have a file handler, then continue
            if filehandler:
                # If the directory actually contains media files then continue
                if filehandler.audio_files:
                    (album_name, artist_name) = filehandler.get_album_and_artist() # Lookup album and artist ID3 tag

                    # If metadata/tags exists and we have an album name
                    if album_name:
                        cover_exists = self.check_cover_image_existence(dirname) # Does cover image already exist in the current directory?
                        if cover_exists == False:
                            image_url = self.get_image_url(album_name, artist_name)
                        else:
                            logger.warning(u'cover image for "{artist_name} - {album_name}" already exists, moving on to the next one'.format(artist_name=artist_name, album_name=album_name))
                            image_url = None

                        # If we found the image URL, then download the image.
                        if image_url:
                            logger.info(u'Downloading album cover image for "{artist_name} - {album_name}"'.format(artist_name=artist_name, album_name=album_name))
                            self.download_image(dirname, image_url)

    def check_cover_image_existence(self, dirname):
        """ Check if cover image already exists in the specified directory """
        possible_covers = ["cover.png", "cover.jpg", "cover.gif", "cover.tiff", "cover.svg"]
        for cover_name in possible_covers:
            if os.path.exists(os.path.join(dirname, cover_name)):
                return True
        return False  

    def get_image_url(self, album_name, artist_name):
        """ Retrieve URL for cover image """
        image_url = None
        try:
            downloader = LastFMDownloader(album_name, artist_name) # Set downloader type to be LastFM
            image_url = downloader.search_for_image() # Search for cover image, return URL to download it
        except KeyboardInterrupt,e:
            raise
        except Exception,e:
            logger.error(u'SOMETHING VERY BAD HAPPENED during processing of "{artist_name} - {album_name}"'.format(artist_name=artist_name, album_name=album_name))
        return image_url

    def download_image(self, dirname, image_url):
        """ Check if overwrite is enabled.  Check if album cover already exists
        Call method to download album cover art image to specified directory"""

        # Set name of image file based on extension from image URL
        if ".png" in image_url.lower():
            cover_name = "cover.png"
        elif ".jpg" in image_url.lower():
            cover_name = "cover.jpg"
        elif ".jpeg" in image_url.lower():
            cover_name = "cover.jpg"
        elif ".gif" in image_url.lower():
            cover_name = "cover.gif"
        elif ".tif" in image_url.lower():
            cover_name = "cover.tiff"
        elif ".tiff" in image_url.lower():
            cover_name = "cover.tiff"
        elif ".svg" in image_url.lower():
            cover_name = "cover.svg"
        else:
            return

        # Does cover.(png|jpg|gif|tiff|svg) already exist?  
        if os.path.exists(os.path.join(dirname, cover_name)):
            # If overwrite is set to True, then go ahead and re-download album cover
            if self.overwrite:
                self.do_download(dirname, image_url, cover_name)
            else:
                logger.warning(u'Cover ({covername}) already exists in {dir_name}'.format(covername=cover_name, dir_name = dirname))
        else:
            # If cover doesn't exist, go ahead and download
            self.do_download(dirname, image_url, cover_name)

    def do_download(self, dirname, image_url, cover_name):
        """ Download album cover art and save as cover.(png|jpg|gif|tiff|svg)"""

        image_data = urllib.urlopen(image_url).read()
        f = open(os.path.join(dirname, cover_name), 'w')
        f.write(image_data)
        f.close()
