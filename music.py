from PyQt5.QtCore import QThread
from playsound import playsound


class MusicThread(QThread):
    def __init__(self, music, repeat=None):
        if repeat is None:
            self.repeat = [False, 1]
        else:
            self.repeat = repeat
        self.filename = music
        super(MusicThread, self).__init__()

    def run(self):
        if self.repeat[0]:
            playsound(self.filename)
        else:
            try:
                for i in range(self.repeat[1]):
                    playsound(self.filename)
            except Exception:
                while True:
                    playsound(self.filename)


def getPlayBgMusicThread():
    return MusicThread("bg.mp3", [True])
