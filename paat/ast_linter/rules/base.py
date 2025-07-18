"""
Base classes for linter rules and findings.
"""

class Finding:
    def __init__(self, filename, lineno, type, message, code=None):
        self.filename = filename
        self.lineno = lineno
        self.type = type
        self.message = message
        self.code = code

    def to_dict(self):
        return {
            "filename": self.filename,
            "lineno": self.lineno,
            "type": self.type,
            "message": self.message,
            "code": self.code,
        }

class Rule:
    def check(self, tree, filename):
        """Return a list of Finding objects for this AST tree and file."""
        raise NotImplementedError()
