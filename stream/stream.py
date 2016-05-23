import os

START_STREAM_PATH = '/stream/start_stream.sh'
STOP_STREAM_PATH = '/stream/stop_stream.sh'


class Stream():
    def __init__(self, command):
        self.command = command

    def startStream(self,key):
        try:
            os.system('sudo sh ' + START_STREAM_PATH + ' ' + key)
            return True
        except Exception as e:
            return False

    def stopstream(self,key):
        try:
            os.system('sudo sh ' + STOP_STREAM_PATH + ' ' + key)
            return True
        except Exception as e:
            return False
