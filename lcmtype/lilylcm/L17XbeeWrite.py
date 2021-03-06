"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class L17XbeeWrite(object):
    __slots__ = ["writeout"]

    def __init__(self):
        self.writeout = ""

    def encode(self):
        buf = BytesIO()
        buf.write(L17XbeeWrite._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __writeout_encoded = self.writeout.encode('utf-8')
        buf.write(struct.pack('>I', len(__writeout_encoded)+1))
        buf.write(__writeout_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != L17XbeeWrite._get_packed_fingerprint():
            raise ValueError("Decode error")
        return L17XbeeWrite._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = L17XbeeWrite()
        __writeout_len = struct.unpack('>I', buf.read(4))[0]
        self.writeout = buf.read(__writeout_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if L17XbeeWrite in parents: return 0
        tmphash = (0xaa7b8a3cbc9cd09) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if L17XbeeWrite._packed_fingerprint is None:
            L17XbeeWrite._packed_fingerprint = struct.pack(">Q", L17XbeeWrite._get_hash_recursive([]))
        return L17XbeeWrite._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

