from enum import Enum

class PdfErrorKind(Enum):
    DuplicatedDynamic = 1
    UndefinedDynamic = 2
    DuplicatedComponent = 3
    UndefinedComponent = 4
    UndefinedInstance = 5


class PdftError(Exception):
    def __init__(self, kind: PdfErrorKind):
        self.kind = kind
