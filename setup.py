#!/usr/bin/env python
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


from setuptools import setup

setup(name='cover_grabber',
      version='1.1.0',
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
