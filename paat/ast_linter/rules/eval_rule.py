import ast
from paat.ast_linter.rules.base import Rule, Finding

class EvalRule(Rule):
    def check(self, tree, filename):
        findings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'eval':
                findings.append(Finding(filename, node.lineno, 'EvalUsage', 'Use of eval()', code=None))
        return findings
