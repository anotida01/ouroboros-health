import bluetooth
from bluetooth.btcommon import BluetoothError

class BL_SERVER():
    def __init__(self):
        print("[BL_SERVER] - Server started")
        self.SERVER_SOCKET = None
        self.CLIENT_SOCKET = None

    def setup_server(self):
        # create Bluetooth Server socket on port 1
        print("[BL_SERVER] - Starting Bluetooth socket on Port 1")
        self.SERVER_SOCKET = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port = 1
        self.SERVER_SOCKET.bind(("",port))

        print("[BL_SERVER] - Listening for connection")
        self.SERVER_SOCKET.listen(1) # wait for connection to be established

        self.CLIENT_SOCKET, address = self.SERVER_SOCKET.accept()
        print("[BL_SERVER] - Accepted connection from:", address)
        return

    def receive_bl_data(self):
        data = self.CLIENT_SOCKET.recv(1024)
        print ("[BL_SERVER] - Received: [%s]" % data)
        return data

def bl_server_main():
    
    while True:
        bl = BL_SERVER()
        bl.setup_server()

        while True:
            try:
                data = bl.receive_bl_data()
            except BluetoothError as err:
                    print(err)
                    print("[BL_SERVER] - Connection Lost...")
                    break
            
            outfile = open('data_reading.txt', 'w+')
            data = data.decode('utf-8')
            outfile.write(data)
            outfile.close()

