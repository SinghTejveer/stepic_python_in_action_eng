# pylint: disable=redefined-outer-name, no-self-use, invalid-name

import os

import pytest

from utils.utils import get_files, update_number, get_number_from_name, refactor


@pytest.fixture
def files():
    return ['s102', 's101', 's100']


def create_files(path, files):
    for filename in files:
        with open(os.path.join(path, filename), 'w') as file:
            file.write(filename)


def create_dirs(path, dirs):
    for directory in dirs:
        os.mkdir(os.path.join(path, directory))


class TestGetFiles:

    def test_returns_correct_result(self, tmpdir, files):
        create_files(str(tmpdir), files)
        assert get_files(str(tmpdir)) == files

    def test_ignore_subdirectories(self, tmpdir, files):
        create_files(str(tmpdir), files)
        create_dirs(str(tmpdir), ['dir1', 'dir2'])
        assert get_files(str(tmpdir)) == files


class TestReplace:

    def test_divisible_by_100(self):
        assert update_number('s100') == 's001'
        assert update_number('s200') == 's101'

    def test_not_divisible_by_100(self):
        assert update_number('s101') == 's002'
        assert update_number('s198') == 's099'
        assert update_number('s199') == 's100'
        assert update_number('s210') == 's111'


class TestGetNumberFromName:

    def test_solution_filename(self):
        assert get_number_from_name('s101') == 's101'

    def test_test_filename(self):
        assert get_number_from_name('test_s101') == 's101'

    def test_raises_value_error_if_can_not_parse(self):
        with pytest.raises(AttributeError):
            get_number_from_name('__init__.py')


class TestRefactor:

    def test_returns_correct_result(self, tmpdir, files):
        create_files(str(tmpdir), files)
        refactor(str(tmpdir), files)
        expected = ['s003', 's002', 's001']
        assert get_files(str(tmpdir)) == expected
        for filename in expected:
            with open(os.path.join(str(tmpdir), filename)) as file:
                assert file.read() == filename

    def test_multiple_inclusions(self, tmpdir):
        with open(os.path.join(str(tmpdir), 's101'), 'w') as file:
            file.write('s101 hello world\ns101 s102')
        refactor(str(tmpdir), ['s101'])
        with open(os.path.join(str(tmpdir), 's002'), 'r') as file:
            assert file.read() == 's002 hello world\ns002 s102'

    def test_skipped_files(self, tmpdir):
        file_path = os.path.join(str(tmpdir), '__init__.py')
        with open(file_path, 'w') as file:
            file.write('# Do not touch me')
        skipped_files = refactor(str(tmpdir), ['__init__.py'])
        assert skipped_files == [file_path]
