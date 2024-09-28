from src.pdftml import just_parse
from src.utils import get_content

grammar_filename = 'grammars/pdft.lark'

examples = {
    'dynamics': 'examples/dynamics.pdftml',
    'component': 'examples/components.pdftml',
    'full': 'examples/full.pdftml'
}

if __name__ == '__main__':
    grammar = get_content(grammar_filename)
    for example_name in examples.keys():
        example = get_content(examples[example_name])
        result = just_parse(grammar,example)
        print(example_name + ' -> ' + str(result) + '\n')