"""
management objects are more like office managers, they don't
do the actual "visible" work out on the floor, but
 without them, there would be no communication

The attributes on a management class tend to refer to other
objects that tend to do the "visible" work
"""

import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace(object):
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(
            filename
        ))

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def find_replace(self):
        for filename in self.temp_directoyr.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
