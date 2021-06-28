import authzed.api.v0.core_pb2 as core_proto


class Zookie(object):
    """Represents a revision cookie that can be used to pass dependency information to Arrakis."""

    def __init__(self, zookie: core_proto.Zookie):
        self._zookie_proto = zookie

    @property
    def token(self) -> str:
        return self._zookie_proto.token

    @property
    def zookie_proto(self) -> core_proto.Zookie:
        return self._zookie_proto

    @classmethod
    def from_token(cls, token: str) -> "Zookie":
        return cls(core_proto.Zookie(token=token))

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, Zookie):
            return False

        return self.token == other.token
