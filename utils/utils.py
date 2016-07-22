import os
import re

from typing import List

NUMBER = re.compile(r'.*(s\d{3})')


def get_files(path: str) -> List:
    """Returns list of files inside the path directory"""
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    # Reversed to prevent collision upon renaming
    return sorted(files, reverse=True)


def update_number(number: str) -> str:
    """Updates exercise number"""
    number = int(number[1:])
    number = (number - 100 if number >= 100 else number) + 1
    return 's' + str(number).zfill(3)


def get_number_from_name(filename: str) -> str:
    return re.match(NUMBER, filename).groups()[0]


def refactor(path: str, files: List):
    """Refactor exercise number in files data and names"""
    for filename in files:
        number = get_number_from_name(filename)
        new_number = update_number(number)

        file_path = os.path.join(path, filename)
        new_file_path = file_path.replace(number, new_number)

        with open(file_path, 'r') as file:
            data = file.read()
        data = data.replace(number, new_number)
        with open(file_path, 'w') as file:
            file.write(data)

        os.rename(file_path, new_file_path)
