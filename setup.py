#!/usr/bin/env python
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

from setuptools import setup
import cover_grabber

setup(name='cover_grabber',
      version=cover_grabber.COVER_GRABBER_VERSION,
      description='Recursively traverse media directory and download album art',
      author='Jayson Vaughn',
      author_email='vaughn.jayson@gmail.com',
      url='https://sourceforge.net/projects/covergrabber/',
      scripts = ['covergrabber'],
      packages = ['cover_grabber'],
      package_dir = {'Cover Grabber':'cover_grabber'},
      install_requires = ['mutagen'],
      license = "GNU GPL v3"
)
