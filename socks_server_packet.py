import ipaddress

class SocksClientPacket:

    def __init__(self):
        self.data = None
        self.version = 
        self.results = None
        self.remote_port = None
        self.remote_address = None

    def resolve_data(self):
        self.version = self.data[0]
        self.command = self.data[1]
        self.remote_port = int(self.data[2:4].hex(), 16)
        self.remote_address = ipaddress.IPv4Address(self.data[4:8])
        self.name = self.data[8]
        print(self.version, self.command, self.remote_port, self.remote_address, self.name)