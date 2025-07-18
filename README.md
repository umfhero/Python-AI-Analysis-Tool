# Python-AI-Analysis-Tool

PAAT, or Python AI Analysis Tool is a Python-based static analysis tool that scans Python source code for common security vulnerabilities, leverages AI to reduce false positives, prioritize findings, and suggest context-aware remediation.

# Goals

Direct Security Impact: Addresses real-world security risks in code.

AI for Practical Problems: Uses AI to solve known pain points in static analysis (false positives, overwhelming alerts).

Technical Depth: Involves parsing code (AST), applying security rules, and integrating ML models.

Scalability & Modularity: Can be built in modules, allowing for expansion.

# Breakdown & AI integration

Phase 1: Foundational Static Analysis (Rule-Based)
Phase 2: AI-Enhanced Analysis
Phase 3: Reporting & User Interface

# Technology Stack

Python: The core language.

ast: For parsing Python code.

scikit-learn: For all your classical machine learning needs (classification, regression, clustering).

pandas: For data handling and preparation (especially for your ML datasets).

nltk or spaCy: If you delve deeper into NLP for understanding code context beyond simple keywords.

numpy: For numerical operations.

joblib or pickle: For saving/loading trained ML models.

Flask / FastAPI: For optional web UI.

tqdm: For progress bars (makes CLI tools nicer).

Dataset Acquisition: This will be your biggest challenge for the AI part.

## Installation

# Create a virtual environment and install dependencies

python -m venv venv

# Activate on PowerShell

venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

# Install the package in editable mode

pip install -e .

## Usage

# Run the CLI scanner (text output)

paat path/to/code

# JSON output

paat path/to/code -o json

# Web API mode (Flask)

# From project root:

export FLASK_APP=paat.web.app
flask run --port 5000
