import os
import shutil
from nose.tools import *
from cover_grabber.handler.mp3_handler import MP3Handler

data_path = os.path.join('tests', 'data')
tmp_dir = os.path.join(data_path, 'tmp')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')
mp3_filename = 'silence-44-s-v1.mp3'
mp3_file = os.path.join(mp3_path, mp3_filename)

mp3_handler = MP3Handler(mp3_path, [mp3_filename])

def test_mp3_handler_init():
    assert(mp3_handler)

def test_mp3_can_get_album_and_artist_tag():
    tags = mp3_handler.get_album_and_artist()
    assert(tags == (u'Quod Libet Test Data', u'piman'))


