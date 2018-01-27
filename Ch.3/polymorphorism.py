class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename


class MP3File(AudioFile):

    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):

    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):

    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


"""
different behaviors happen depending on what subclass is being used,
without the explicitly know what the subclass is

each class inherits AudioFile, running a check to make sure it's a valid
audio file type. But depending on which subclass (mp3, wav, ogg) the method
"play" can have different implementations for each compression algorithm

Duck typing = how python lets any object be used in any context, up until
it is used in a way that it does not support
"""
