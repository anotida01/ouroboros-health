import bluetooth
from bluetooth.btcommon import BluetoothError

class BL_CLIENT():

    def __init__(self, server_name):
        print("Bluetooth client started")
        self.server_name = server_name
        self.server_address = None
        self.client_socket = None

    def connect_to_server(self):
        print('Bluetooth: Looking for server "%s"' % self.server_name)
        nearby_devices = bluetooth.discover_devices(duration=5 ,lookup_names=True, lookup_class=True)

        for addr, name, device_class in nearby_devices:
            print("[DEVICE FOUND]")
            print("Device Name: %s" % (name))
            print("Device MAC Address: %s" % (addr))

            if (name == self.server_name):
                self.server_address = addr
                break

        if self.server_address is not None:
            print("Found server with address: %s" % self.server_address)
        else:
            print ("Could not find target bluetooth server nearby")
            return -1
        
        # connect to server
        port = 1
        self.client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        try:
            self.client_socket.connect((self.server_address, port))
        except BluetoothError as err:
            print(err)
            return -1

        # connection successful!
        return 0

    def send_bl_data(self, data):
        try:
            if (self.client_socket != None): self.client_socket.send(data)
        except BluetoothError as err:
            print(err)
            print("Failed to send data")
            return -1

        # data was sent
        return 0
    
    def close(self):
        if (self.client_socket != None): self.client_socket.close()
        return 0


if __name__ == '__main__':
    exit(1)
