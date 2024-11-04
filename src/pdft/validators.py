from src.pdft.errors import PdfErrorKind, PdftError
from src.pdft.visitors import PdftVisitor


class PdftValidator(PdftVisitor):

    def __init__(self):
        super().__init__()
        self.checks = [
            self.duplicated_dynamic, self.undefined_dynamic,
            self.duplicated_component, self.undefined_component,
            self.undefined_instance
        ]

    def validate(self) -> PdftError:
        error: PdftError = None
        counter: int = 0
        while not error and (counter < len(self.checks)):
            check = self.checks[counter]
            error = check()
            counter += 1
        return error

    def duplicated(self, main, kind, candidate_error) -> PdftError:
        temporary_set = set(self.lists[main][kind])
        error = None
        if len(temporary_set) != len(self.lists[main][kind]):
            error = candidate_error
        return error

    def undefined(self, main, candidate_error) -> PdftError:
        definition_set = set(self.lists[main]['def'])
        use_set = set(self.lists[main]['use'])
        error: PdftError = None
        while not error and use_set:
            item = use_set.pop()
            error = None if item in definition_set else candidate_error
        return error

    def duplicated_dynamic(self) -> PdftError:
        return self.duplicated('dynamic','def', PdfErrorKind.DuplicatedDynamic)

    def duplicated_component(self) -> PdftError:
        return self.duplicated('component','def', PdfErrorKind.DuplicatedComponent)

    def undefined_dynamic(self) -> PdftError:
        return self.undefined('dynamic', PdfErrorKind.UndefinedDynamic)

    def undefined_component(self) -> PdftError:
        return self.undefined('component', PdfErrorKind.UndefinedComponent)

    def undefined_instance(self) -> PdftError:
        return self.undefined('instance', PdfErrorKind.UndefinedInstance)
