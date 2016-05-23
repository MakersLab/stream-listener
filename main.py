from stream.stream import Stream
import threading
import socket
import json

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 4000
adress = '0.0.0.0'


def connectionThread(conn):
    # production only
    control = Stream()

    msg_recv = conn.recv(1024)
    msg_recv = msg_recv.decode('utf8')
    msgEncoded = json.loads(msg_recv)
    stream_key = msgEncoded['key']
    success = False
    message='unknown error'
    if stream_key != '':
        if (msgEncoded['control'] == 'start'):
            success = control.startStream(stream_key)
            if success:
                message = 'stream should be started'
            else:
                message = 'something went wrong.'
        elif (msgEncoded['control'] == 'stop'):

            success = control.stopstream(stream_key)
            if success:
                message = 'stream should be stopped'
            else:
                message = 'something went wrong.'
    else:
        message = 'stream key was not set'
        success = False
    print(msg_recv)

    data = {
        'successful': success,
        'message': message,
    }

    msgSend = json.dumps(data)
    conn.send(msgSend.encode())
    conn.close()


if __name__ == '__main__':
    connection.bind((adress, port))

    connection.listen(10)
    print('Server listening on', adress + ':' + str(port))
    while True:
        conn, addr = connection.accept()
        print('Got connection')
        t = threading.Thread(target=connectionThread, args=[conn, ])
        t.start()
