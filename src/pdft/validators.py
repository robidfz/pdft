from pprint import pprint

from lark import Token
from lark.visitors import Visitor_Recursive

from src.pdft.errors import PdfErrorKind, PdftError
from src.pdft.visitors import PdftVisitor


class PdftValidator(PdftVisitor):

    def __init__(self):
        super().__init__()
        self.checks = [(self.check_dynamics,PdfErrorKind.DuplicatedDynamic)]

    def validate(self) -> PdftError:
        error: PdftError = None
        counter: int = 0
        while not error and (counter < len(self.checks)):
            check, candidate_error = self.checks[counter]
            error = check()
            counter += 1
        return error

    def check_dynamics(self) -> bool:
        temporary_set = set(self.dynamics)
        error = None
        if len(temporary_set) != len(self.dynamics):
            error = PdfErrorKind.DuplicatedDynamic
        return error
