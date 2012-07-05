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

class Handler(object):
    def __init__(self, dirname, filenames):
        """ Initialize Handler """

        self.dirname = dirname #Name of directory
        self.filenames = filenames #List of filenames found in directory
        self.audio_files = [os.path.join(dirname, file) for file in filenames]


    def get_album_and_artist(self):
        """ Return tags for album and artist"""
        pass 
