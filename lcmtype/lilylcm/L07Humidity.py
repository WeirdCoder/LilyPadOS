"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class L07Humidity(object):
    __slots__ = ["humidity"]

    def __init__(self):
        self.humidity = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(L07Humidity._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">f", self.humidity))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != L07Humidity._get_packed_fingerprint():
            raise ValueError("Decode error")
        return L07Humidity._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = L07Humidity()
        self.humidity = struct.unpack(">f", buf.read(4))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if L07Humidity in parents: return 0
        tmphash = (0x89d65147753a47c9) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if L07Humidity._packed_fingerprint is None:
            L07Humidity._packed_fingerprint = struct.pack(">Q", L07Humidity._get_hash_recursive([]))
        return L07Humidity._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
