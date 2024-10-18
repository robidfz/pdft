from pprint import pprint

from lark import Token
from lark.visitors import Visitor_Recursive

class PdftVisitor(Visitor_Recursive):

    def __init__(self):
        self.functions = {
            'dynamic_name_def': self.dynamic_name_def,
            'dynamic_name_use': self.dynamic_name_use,
            'component_name_def': self.component_name_def,
            'component_name_use': self.component_name_use,
            'instance_name_def': self.instance_name_def,
            'instance_name_use': self.instance_name_use
        }
        self.lists = {
            'dynamic': {
                'def': list(),
                'use': list()
            },
            'component': {
                'def': list(),
                'use': list()
            },
            'instance': {
                'def': list(),
                'use': list()
            }
        }
        self.dynamics = list()

    def pprint(self):
        pprint(self.lists)

    def _call_userfunc(self, tree):
        payload: Token = tree.data
        kind = payload.value
        if kind in self.functions.keys():
            function = self.functions[kind]
            child = tree.children[0]
            function(child.value)
        return None

    def dynamic_name_def(self, value):
        self.lists['dynamic']['def'].append(value)

    def dynamic_name_use(self, value):
        self.lists['dynamic']['use'].append(value)

    def component_name_def(self, value):
        self.lists['component']['def'].append(value)

    def component_name_use(self, value):
        self.lists['component']['use'].append(value)

    def instance_name_def(self, value):
        self.lists['instance']['def'].append(value)

    def instance_name_use(self, value):
        self.lists['instance']['use'].append(value)