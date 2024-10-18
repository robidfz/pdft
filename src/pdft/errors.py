from enum import Enum

class PdfErrorKind(Enum):
    DuplicatedDynamic = 1
    DuplicatedComponent = 2
    DuplicatedPort = 3


class PdftError(Exception):
    def __init__(self, kind: PdfErrorKind):
        self.kind = kind
