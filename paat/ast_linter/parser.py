import ast
import os
import pkgutil
import importlib
from paat.ast_linter.rules.base import Rule, Finding

class ASTRuleRunner:
    def __init__(self):
        self.rules = self.load_rules()

    def load_rules(self):
        rules = []
        rules_pkg = importlib.import_module('paat.ast_linter.rules')
        for _, modname, _ in pkgutil.iter_modules(rules_pkg.__path__):
            module = importlib.import_module(f'paat.ast_linter.rules.{modname}')
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Rule) and obj is not Rule:
                    rules.append(obj())
        return rules

    def run_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            tree = ast.parse(source, filename=filepath)
        except SyntaxError:
            return []

        findings = []
        for rule in self.rules:
            findings.extend(rule.check(tree, filepath))
        return findings

    def run(self, path):
        all_findings = []
        if os.path.isfile(path):
            all_findings.extend(self.run_file(path))
        else:
            for root, _, files in os.walk(path):
                for name in files:
                    if name.endswith('.py'):
                        fp = os.path.join(root, name)
                        all_findings.extend(self.run_file(fp))
        return all_findings
