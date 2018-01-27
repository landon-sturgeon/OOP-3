"""
always dry your code
you'll be reading and revising code more often than writing fresh
being able to read code is paramount to future efficiency
deduping code always for only one pace needing to be revised
if a change is needed
"""

import sys
import os
from zip_processor import ZipProcessor


class ZipProcesser(object):
    def __init__(self, zipname):
        self.zipname = zipname

        self.temp_directory = Path("unzipped={}".format(
            zipname[:-4]
        ))

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
