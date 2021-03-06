"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class L16ChargerCommand(object):
    __slots__ = ["targetState"]

    def __init__(self):
        self.targetState = ""

    def encode(self):
        buf = BytesIO()
        buf.write(L16ChargerCommand._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __targetState_encoded = self.targetState.encode('utf-8')
        buf.write(struct.pack('>I', len(__targetState_encoded)+1))
        buf.write(__targetState_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != L16ChargerCommand._get_packed_fingerprint():
            raise ValueError("Decode error")
        return L16ChargerCommand._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = L16ChargerCommand()
        __targetState_len = struct.unpack('>I', buf.read(4))[0]
        self.targetState = buf.read(__targetState_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if L16ChargerCommand in parents: return 0
        tmphash = (0xe22a31f980d9d595) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if L16ChargerCommand._packed_fingerprint is None:
            L16ChargerCommand._packed_fingerprint = struct.pack(">Q", L16ChargerCommand._get_hash_recursive([]))
        return L16ChargerCommand._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

