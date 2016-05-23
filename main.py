from stream import Stream
import threading
import socket
import json

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 4000
adress = '0.0.0.0'

def connectionThread(conn):
    #production only
    control=Stream('none')

    msg_recv=conn.recv(1024)
    msg_recv=msg_recv.decode('utf8')
    msgEncoded=json.loads(msg_recv)

    if(msgEncoded['control']=='start'):
        control.startStream()
    elif(msgEncoded['control']=='stop'):
        control.stopstream()

    print(msg_recv)

    data={
        'successful':True,
        'message':'Stream was ...'
    }
    msgSend=json.dumps(data)
    conn.send(msgSend.encode())
    conn.close()


if __name__ == '__main__':
    connection.bind((adress, port))

    connection.listen(10)
    print('Server listening on', adress + ':' + str(port))
    while True:
        conn, addr = connection.accept()
        print('Got connection')
        t = threading.Thread(target=connectionThread, args=[conn,])
        t.start()

