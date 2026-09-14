# IS 218 — Python Setup and Basic Testing

A focused example for the hands-on assessment: create a GitHub repository with
a README, clone it, configure Git/Python/pytest, and test addition and subtraction.

**Start with the [step-by-step guide](TEST_GUIDE.md).** Use the
[assessment checklist](ASSESSMENT.md) before submitting.

## Project structure

```text
.
├── app/
│   ├── __init__.py       # Makes app a regular Python package
│   └── operations.py     # Addition and subtraction
├── tests/
│   └── test_operations.py # Six Arrange–Act–Assert tests
├── .gitignore           # Excludes the environment and generated files
├── requirements.txt     # pytest dependency
├── pytest.ini           # Test discovery settings
├── README.md
├── TEST_GUIDE.md
└── ASSESSMENT.md
```

## Run this example

From this repository's root on macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

On Windows PowerShell, create with `py -3 -m venv .venv` and activate with
`.\.venv\Scripts\Activate.ps1`, then run the same installation/test commands.
If the environment already exists, activate it instead of recreating it.

Expected result: **6 passed**. Read [the functions](app/operations.py) and
[the tests](tests/test_operations.py) together. Each test arranges inputs, calls
one function, and checks an independently expected result.

Plain `pytest -v` also works: pytest.ini adds the project root to the test import path.

There is no interactive calculator or CI setup to learn for this assessment.
Professional practice here means clear organization, reproducible setup,
meaningful tests, and reviewed Git commits.
