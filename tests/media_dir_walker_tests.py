import os
import shutil
from nose.tools import *
from cover_grabber.os.media_dir_walker import MediaDirWalker

data_path = os.path.join('tests', 'data')
tmp_dir = os.path.join(data_path, 'tmp')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')

walker = MediaDirWalker(data_path)


def setup():
    if os.path.exists(tmp_dir):
        empty_dir(tmp_dir)
        os.rmdir(tmp_dir)

    os.mkdir(tmp_dir)

def empty_dir(path):
    for file_name in os.listdir(tmp_dir):
        os.remove(os.path.join(tmp_dir, file_name))

def teardown():
    empty_dir(tmp_dir)
    os.rmdir(tmp_dir)


def test_media_dir_walker_init():
    assert(walker)

def test_media_dir_walker_path():
    assert(walker.path == os.path.join('tests', 'data'))

def test_cover_doesnt_exist():
    assert(walker.check_cover_image_existence(os.path.join('tests', 'data', 'mp3')) == False)

def test_cover_exists():
    assert(walker.check_cover_image_existence(os.path.join('tests', 'data', 'ogg')) == True)

def test_can_get_image_url():
    assert("http://" in walker.get_image_url('Abbey Road', 'The Beatles'))

def test_can_download_image():
    image_url = walker.get_image_url('Abbey Road', 'The Beatles')
    walker.download_image(os.path.join('tests', 'data', 'tmp'), image_url)
    assert(("cover" in os.listdir(tmp_dir)[0].split('.')[0]) == True)
