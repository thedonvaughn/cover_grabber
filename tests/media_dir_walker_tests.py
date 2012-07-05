import os
from nose.tools import *
from cover_grabber.os.media_dir_walker import MediaDirWalker

walker = MediaDirWalker(os.path.join('tests', 'data'))

def test_media_dir_walker_init():
    assert(walker)

def test_media_dir_walker_path():
    assert(walker.path == os.path.join('tests', 'data'))

def test_cover_doesnt_exist():
    assert(walker.check_cover_image_existence(os.path.join('tests', 'data', 'mp3')) == False)

def test_cover_exists():
    assert(walker.check_cover_image_existence(os.path.join('tests', 'data', 'ogg')) == True)

#def test_can_get_image_url():
#    assert(walker.get_image_url('Abbey Road', 'The Beatles') == "test")
