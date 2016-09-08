import os
import pytest

from log2graph.log2html import draw_graph, get_files, get_graph, read_log_file

DIR_TEST_FILES = os.getcwd() + os.sep + 'tests' + os.sep + 'test_samples'


@pytest.fixture()
def files():
    return DIR_TEST_FILES


def test_get_files(files):
    list_of_files = []
    list_of_files.extend(get_files(files))
    assert list_of_files is not False


def test_read_log_file(files):
    file_ = DIR_TEST_FILES + os.sep + os.listdir(files)[0]
    numbers = read_log_file(file_)
    assert isinstance(numbers, list) is True
    assert os.path.isfile(file_) is True
    assert isinstance(file_, basestring) is True
    fake_file = os.listdir(files)[0]
    assert os.path.isfile(fake_file) is False


def test_get_graph(files):
    file_ = DIR_TEST_FILES + os.sep + os.listdir(files)[0]
    assert os.path.isfile(file_) is True
    numbers = read_log_file(file_)
    assert numbers is not False
    assert isinstance(get_graph(numbers), dict) is True


def test_draw_graph(files):
    file_ = DIR_TEST_FILES + os.sep + os.listdir(files)[0]
    assert os.path.isfile(file_) is True
    draw_graph(file_, off=True)
    assert os.path.isfile(file_[:-4] + '.html') is True
