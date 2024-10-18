from src.pdft.parsers import PdftParser
from src.pdft.validators import PdftValidator
from src.utils import get_content

grammar_filename = 'grammars/pdft.lark'

examples = {
    #'dynamics': 'examples/dynamics.pdftml'
    #'component': 'examples/components.pdftml',
    'full': 'examples/full.pdftml'
}

if __name__ == '__main__':
    grammar: str = get_content(grammar_filename)
    parser: PdftParser = PdftParser(grammar)
    for example_name in examples.keys():
        example = get_content(examples[example_name])
        tree = parser.parse(example)
        validator: PdftValidator = PdftValidator()
        validator.visit(tree)
        validator.pprint()