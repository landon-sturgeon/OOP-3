"""
common need for custom behavior is caching a value that is
difficult to calculate or expensive to look up
The goal is to store the value locally to avoid repeated calls
to the expensive calculation
"""


from urllib.request import urlopen


class WebPage(object):
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content