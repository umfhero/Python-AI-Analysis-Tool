import argparse
import sys
from paat.ast_linter.parser import ASTRuleRunner
from paat.report.formatter import format_json, format_text

def main():
    parser = argparse.ArgumentParser(prog='paat', description='Python AI Analysis Tool')
    parser.add_argument('path', nargs='?', default='.', help='File or directory to scan')
    parser.add_argument('-o', '--output', choices=['json', 'text'], default='text', help='Output format')
    args = parser.parse_args()

    runner = ASTRuleRunner()
    findings = runner.run(args.path)

    if args.output == 'json':
        out = format_json(findings)
    else:
        out = format_text(findings)

    sys.stdout.write(out)

if __name__ == '__main__':
    main()
