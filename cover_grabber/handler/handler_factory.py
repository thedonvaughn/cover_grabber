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
from cover_grabber.handler.mp3_handler import MP3Handler
from cover_grabber.handler.ogg_handler import OGGHandler
from cover_grabber.handler.flac_handler import FLACHandler

class HandlerFactory(object):
    @staticmethod
    def get_handler(dirname, filenames):
        """ Factory method to return proper Handler subclass """
        for file in filenames:
            if ".mp3" in file:
                return MP3Handler(dirname, filenames) # Set the File Handler to be MP3

            if ".ogg" in file:
                return OGGHandler(dirname, filenames) # Set the File Handler to be OGG

            if ".flac" in file:
                return FLACHandler(dirname, filenames) # Set the File Handler to be FLAC

        return False
