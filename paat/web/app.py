from flask import Flask, request, jsonify
from paat.ast_linter.parser import ASTRuleRunner

app = Flask(__name__)
runner = ASTRuleRunner()

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    path = data.get('path')
    findings = runner.run(path)
    return jsonify([f.to_dict() for f in findings])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
