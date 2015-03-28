"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class L09Voltage(object):
    __slots__ = ["analogValue"]

    def __init__(self):
        self.analogValue = [ 0 for dim0 in range(8) ]

    def encode(self):
        buf = BytesIO()
        buf.write(L09Voltage._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>8b', *self.analogValue[:8]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != L09Voltage._get_packed_fingerprint():
            raise ValueError("Decode error")
        return L09Voltage._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = L09Voltage()
        self.analogValue = struct.unpack('>8b', buf.read(8))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if L09Voltage in parents: return 0
        tmphash = (0x128be18524f70c4) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if L09Voltage._packed_fingerprint is None:
            L09Voltage._packed_fingerprint = struct.pack(">Q", L09Voltage._get_hash_recursive([]))
        return L09Voltage._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

