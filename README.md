Cover Grabber
=============


Simple utility to recurisvely traverse directory of media files (MP3, OGG, FLAC) and download album cover art.
Very helpful if you have hundreds of thoursands of sub-directories of media files.

---------------

## Home Page

https://sourceforge.net/projects/covergrabber/

## Source Code

https://github.com/thedonvaughn/cover_grabber

## Requirements
* Python
* Mutagen python module


## Install

 1.) Install python-mutagen

* Debian/Ubuntu: apt-get install python-mutagen
* Fedora: yum install python-mutagen
* Arch: pacman -Sy mutagen

 2.) Install covergrabber:

    $ python setup.py install

## Howto Use

    $ covergrabber <Media directory> [options]

For example:

    $ covergrabber "/home/jvaughn/Music"

## For Help

    $ covergrabber -h

------

(c) 2011 - Jayson Vaughn (vaughn.jayson@gmail.com)
