from ctypes import Structures, c_ubyte, c_ushort, c_uint32
import socket


class IP(Structures):
    _field_ = [
        ("ihl",             c_ubyte,    4),     # 4-bit unsingned char
        ("version",         c_ubyte,    4),     # 4-bit unsingned char
        ("tos",             c_ubyte,    8),     # 8-bit char
        ("len",             c_ushort,   16),    # 16-bit unsigned short
        ("id",              c_ushort,   16),    # 16-bit unsigned short
        ("offset",          c_ushort,   16),    # 16-bit unsingned short
        ("ttl",             c_ubyte,    8),     # 8-bit char
        ("protocol_num",    c_ubyte,    8),     # 8-bit char
        ("sum",             c_ushort,   16),    # 16-bit unsigned short
        ("src",             c_uint32,   32),    # 32-bit unsingned int
        ("dst",             c_uint32,   32),    # 32-bit unsingned int
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # human readable IP address
        self.src_address = socket.inet_ntoa(socket.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(socket.pack("<L", self.dst))
