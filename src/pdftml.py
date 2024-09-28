import sys

from lark import Lark
import traceback

def just_parse(grammar_content, text_to_parse):
    retval = False
    try:
        parser = Lark(grammar_content, parser='lalr')
        tree = parser.parse(text_to_parse)
        retval = bool(tree)
    except Exception:
        print(traceback.format_exc())
        sys.exit()
    return retval

