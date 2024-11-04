import sys
from lark import Lark
import traceback

class PdftParser:
    def __init__(self, pdft_grammar: str):
        self.parser: Lark = Lark(pdft_grammar, parser='lalr')

    def parse(self, pdft_model):
        tree = None
        try:
            tree = self.parser.parse(pdft_model)
        except Exception:
            print(traceback.format_exc())
            sys.exit()
        return tree