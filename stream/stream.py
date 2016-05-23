import os

START_STREAM_PATH = 'stream/start_stream.sh'
STOP_STREAM_PATH = 'stream/stop_stream.sh'


class Stream():
    def __init__(self, ):
        pass

    def startStream(self,key):
        try:
            print('Trying Start stream')
            os.system('sudo sh ' + START_STREAM_PATH + ' ' + key)
            print('Done start')
            return True
        except Exception as e:
            return False

    def stopstream(self,key):
        try:
            print('Trying Stoop stream')
            os.system('sudo sh ' + STOP_STREAM_PATH)
            print('Done stop')
            return True
        except Exception as e:
            return False
