import ipaddress

RESULT_PACKT = [0,None,0,0,0,0,0,0]

class SocksClientPacket:

    def __init__(self):
        self.version = None
        self.command = None
        self.remote_port = None
        self.remote_address = None
        self.name = None

    def resolve_data(self, data):
        self.version = data[0]
        self.command = data[1]
        self.remote_port = int(data[2:4].hex(), 16)
        self.remote_address = str(ipaddress.IPv4Address(data[4:8]))
        self.name = data[8]

    def create_result_packet(self, result_code):
        data = RESULT_PACKT
        data[1] = result_code
        data = bytes(''.join([chr(val) for val in data]), 'utf-8')
        return data



