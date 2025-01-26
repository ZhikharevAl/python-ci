[![Python Code Quality](https://github.com/ZhikharevAl/python-ci/actions/workflows/code-quality.yaml/badge.svg)](https://github.com/ZhikharevAl/python-ci/actions/workflows/code-quality.yaml)

# Python CI Template

A modern Python project template with comprehensive CI/CD setup using GitHub Actions and state-of-the-art development tools.

## Features

- **Python 3.13+** support
- **Modern dependency management** with [uv](https://github.com/astral-sh/uv)
- **Comprehensive code quality checks**:
  - Linting with [Ruff](https://github.com/astral-sh/ruff)
  - Type checking with [Pyright](https://github.com/microsoft/pyright)
  - Test coverage reporting with [pytest-cov](https://github.com/pytest-dev/pytest-cov)
  - Code coverage tracking with [Codecov](https://codecov.io)
- **Allure Reports**: Detailed test reports with [Allure Framework](https://docs.qameta.io/allure/)
- **Pre-commit hooks** for consistent code quality
- **Automated CI/CD** with GitHub Actions

## Project Setup

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ZhikharevAl/python-ci.git
cd python-ci
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -e ".[dev]"
```

4. Install pre-commit hooks:

```bash
pre-commit install
```

## Development

### Code Quality Tools

This project uses several tools to ensure code quality:

- **Ruff**: A fast Python linter and formatter
  - Configured with strict rules (see `pyproject.toml`)
  - Line length set to 100 characters
  - Google docstring convention

- **Pyright**: Static type checker
  - Strict type checking enabled
  - Compatible with Python 3.13

- **pytest**: Testing framework
  - Coverage reporting enabled
  - Test files should be placed in the `tests` directory

- **Allure Framework**: Generates detailed test reports
  - Reports are automatically published to GitHub Pages
  - Allure results are stored in the `allure-results` directory

### GitHub Actions Workflow

The CI pipeline includes the following steps:

1. **Lock file verification**
2. **Code linting**
3. **Code formatting check**
4. **Type consistency check**
5. **Unit tests with coverage reporting**
6. **Allure Report generation**:
   - Test results are saved as artifacts
   - Allure reports are generated and published to GitHub Pages
7. **Project build**

### Pre-commit Hooks

The following pre-commit hooks are configured:

- `uv-lock`: Ensures dependency lock file is up to date
- `ruff`: Lints and formats code
- `pyright`: Checks type consistency
- `trailing-whitespace`: Removes trailing whitespace
- `end-of-file-fixer`: Ensures files end with a newline
- `check-yaml`: Validates YAML files

## Allure Reports

This project uses [Allure Framework](https://docs.qameta.io/allure/) to generate detailed test reports. Reports are automatically published to GitHub Pages after each CI run.

### Viewing Reports

1. After a CI run, navigate to the **Actions** tab in your GitHub repository.
2. Find the latest workflow run and click on it.
3. Scroll down to the **Artifacts** section and download the `allure-results` artifact (if needed).
4. The Allure report is automatically published to GitHub Pages. You can view it at:

```
https://zhikhareval.github.io/python-ci/
```

### Local Report Generation

To generate Allure reports locally:

1. Run tests with Allure results:

```bash
uv run pytest --alluredir=allure-results
```

2. Generate and serve the report:

```bash
allure serve allure-results
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Open a pull request with a detailed description of your changes.
