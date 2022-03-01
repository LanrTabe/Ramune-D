import json
import socket
import threading

Host = '127.0.0.1'
Port = 11235
R_Server = socket.socket()
R_Clients = []

def Broadcast(R_Message : str) -> None:
    print('Broadcast', R_Message)
    print('Length', len(R_Clients))
    Eraser = []
    for CurC in R_Clients:
        try:
            CurC.send(R_Message.encode('utf-8'))
        except:
            Eraser.append(CurC)
    for EraC in Eraser:
        R_Clients.remove(EraC)

class Thread_Client(threading.Thread):
    def __init__(self, R_Client, R_Address) -> None:
        super().__init__()
        self.Client = R_Client
        self.Address = R_Address

    def run(self) -> None:
        while True:
            try:
                Content = json.loads(self.Client.recv(1024).decode('utf-8'))
            except:
                return
            if Content['Type'] == 'Sender':
                print('Sender')
                Broadcast(Content['Text'])
            elif Content['Type'] == 'Receiver':
                print('Receiver')
                self.Client.settimeout(0.25)
                R_Clients.append(self.Client)
                return

def main():
    R_Server.bind((Host, Port))
    R_Server.listen(10)
    while True:
        R_Client, R_Address = R_Server.accept()
        print(R_Client, R_Address)
        R_Thread = Thread_Client(R_Client, R_Address)
        R_Thread.start()

if __name__ == '__main__':
    main()