import sys

from src.pdft.errors import PdftError
from src.pdft.parsers import PdftParser
from src.pdft.validators import PdftValidator
from src.utils import get_content

if __name__ == '__main__':
    if len(sys.argv) > 2:
        grammar_filename = sys.argv[1]
        model_filename = sys.argv[2]
        grammar: str = get_content(grammar_filename)
        parser: PdftParser = PdftParser(grammar)
        example = get_content(model_filename)
        tree = parser.parse(example)
        validator: PdftValidator = PdftValidator()
        validator.visit(tree)
        validator.pprint()
        error: PdftError = validator.validate()
        print(error)