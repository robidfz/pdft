from pprint import pprint

from lark import Token
from lark.visitors import Visitor_Recursive


class PdftValidator(Visitor_Recursive):

    def __init__(self):
        self.functions = {
            'dynamic_name': self.collect
        }
        self.dynamics = list()

    def pprint(self):
        print(f'Dynamics -> {self.dynamics}')


    def _call_userfunc(self, tree):
        payload: Token = tree.data
        kind = payload.value
        if kind in self.functions.keys():
            function = self.functions[kind]
            child = tree.children[0]
            function(child.value)
        return None

    def collect(self, value):
        self.dynamics.append(value)

