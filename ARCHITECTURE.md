# PAAT (Python AI Analysis Tool) Architecture & Project Structure

This document outlines the recommended directory layout, module responsibilities, and key components for the PAAT project.

## Project Phases & Mapping to Modules

1. **Phase 1: Foundational Static Analysis**

   - Module: `paat/ast_linter`  
     AST parsing and rule-based vulnerability detectors using Python's `ast` module.

2. **Phase 2: AI-Enhanced Analysis**

   - Module: `paat/ai_analysis`  
     AI models (scikit-learn pipelines) for false-positive reduction and severity scoring.

3. **Phase 3: Reporting & User Interface**
   - Module: `paat/report`  
     Report generators (JSON/HTML/CLI output).
   - Module: `paat/cli`  
     Command-line interface powered by `argparse`.
   - Module: `paat/web` (optional)  
     Lightweight web UI (Flask or FastAPI).

## Top-Level Directory Layout

```
Python-AI-Analysis-Tool/
├── paat/                   # Main package
│   ├── __init__.py
│   ├── ast_linter/         # Phase 1
│   │   ├── __init__.py
│   │   ├── parser.py       # AST parsing utilities
│   │   └── rules/          # Individual rule definitions
│   ├── ai_analysis/        # Phase 2
│   │   ├── __init__.py
│   │   ├── features.py     # Feature extraction for ML
│   │   └── models.py       # Model training & prediction
│   ├── report/             # Phase 3 reporting
│   │   ├── __init__.py
│   │   ├── formatter.py    # Output formatting logic
│   │   └── templates/      # HTML templates (if any)
│   ├── cli/                # CLI entrypoints
│   │   ├── __init__.py
│   │   └── main.py         # `argparse` commands and entrypoint
│   └── web/                # Optional Web UI
│       ├── __init__.py
│       ├── app.py          # Flask/FastAPI setup
│       └── static/         # JS/CSS assets
├── tests/                  # Unit and integration tests
│   ├── ast_linter/         # Tests for rules and parser
│   └── ai_analysis/        # Tests for ML model workflows
├── docs/                   # Design documents, tutorials
│   └── architecture.md
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation script
├── README.md               # Project overview and quickstart
└── plan.txt                # Original planning document
```

## Detailed Module Responsibilities

- **paat/ast_linter/parser.py**

  - Load and parse Python source files into ASTs.
  - Provide utilities for traversing and querying AST nodes.

- **paat/ast_linter/rules/**

  - Each rule in its own file (e.g., `sql_injection.py`, `hardcoded_secrets.py`).
  - Implement a common interface (e.g., `Rule.check(node) -> List[Finding]`).

- **paat/ai_analysis/features.py**

  - Convert AST findings and code metrics into numerical features.
  - Handle data serialization for ML workflows.

- ** models.py**

  - Train and store classifiers/regressors using `scikit-learn`.
  - Provide prediction APIs with confidence/severity scores.

- **paat/report/formatter.py**

  - Take a list of Findings and format to JSON, plain text, or HTML.
  - Plug-in architecture for adding new output formats.

- **paat/cli/main.py**

  - Parse command-line arguments.
  - Wire together AST linter, AI models, and reporting.

- **paat/web/app.py**
  - Expose a RESTful API and interactive dashboard.
  - Handle file uploads and display scan results.

## Additional Considerations

- **Testing**: Use `pytest` alongside fixtures of both vulnerable and safe code snippets.
- **CI/CD**: Integrate linting and test runs on GitHub Actions.
- **Packaging**: Distribute on PyPI with versioned releases.
- **Documentation**: Expand `docs/` with user guides, rule catalogs, and AI model descriptions.

---

With this structure, you can incrementally build each phase, add new rules or models, and ensure clear separation of concerns across the project.
