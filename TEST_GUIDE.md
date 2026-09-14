# Hands-On Study Guide

[Contents](README.md) · [Submission checklist](ASSESSMENT.md)

**Goal:** create a README-only GitHub repository, clone it, set up Python and
pytest, write addition/subtraction tests, and push the finished project.
Work in your own repository. The instructor decides which references are allowed
during the test. You do not need to build an interactive calculator.

Commands go in a terminal; code goes in the named files. Run commands one line
at a time and save files before testing. The **project root** is your cloned
folder containing README.md. If you see `>>>`, enter `exit()` to leave Python
before running shell commands.

## 1. Create and clone your repository

Check `git --version` and your Python version: `python3 --version` on macOS/Linux
or `py -3 --version` in Windows PowerShell. Use the course's Python installation.
Resolve missing software and GitHub sign-in with course setup support.

On GitHub, create a repository named `addition-subtraction-practice` with a README.
Use the instructor's visibility setting. Leave the gitignore template unselected
so you can create it yourself. Copy its HTTPS URL from **Code**.

Replace YOUR-USERNAME below, or paste the copied URL:

```bash
git clone https://github.com/YOUR-USERNAME/addition-subtraction-practice.git
cd addition-subtraction-practice
git status
git remote -v
```

**Check:** README.md exists locally, the working tree is clean, and origin points
to your repository. Open this folder in your editor. Cloning already sets up Git
and origin; do not run `git init` or add a second origin.

## 2. Create `.gitignore` before generating files

Create `.gitignore` at the project root, including the leading dot:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

These rules exclude the local environment, Python bytecode, and pytest caches.
**Commit `.gitignore` itself.** Keep source, tests, and configuration tracked.
Ignore rules do not remove files already tracked by Git.

## 3. Create and verify the environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

A virtual environment keeps this project's installed packages separate. Verify it:

```bash
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip --version
```

**Check:** paths include `.venv`, and the Boolean is True. Select this interpreter
in your editor too. Reactivate the existing environment when returning later.
If activation is unavailable, use `.venv/bin/python` on macOS/Linux or
`.\.venv\Scripts\python.exe` on Windows in place of `python`.

## 4. Install pytest and configure discovery

Create `requirements.txt`:

```text
pytest==8.4.2
```

Install through your selected interpreter:

```bash
python -m pip install -r requirements.txt
python -m pytest --version
python -m pip check
```

`==` requests the recorded pytest version; pip installs its dependencies too.
The file describes the test dependency, not your entire computer. `pip freeze`
can list all installed packages, but you do not need to memorize that list.

Create `pytest.ini`:

```ini
[pytest]
pythonpath = .
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

`pythonpath = .` adds the project root to Python's import path during testing,
so both `pytest` and `python -m pytest` can import `app`.
pytest searches `tests/` by default and collects files/functions beginning with
`test_`. These settings configure discovery; they do not install pytest or
activate Python. **Check:** pytest reports 8.4.2 and pip reports no broken requirements.

## 5. Write the arithmetic functions

Create `app/`, put a short package docstring in `app/__init__.py`, and create
`app/operations.py`:

```python
"""Arithmetic functions that return results for callers and tests."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the first number minus the second."""
    return a - b
```

`__init__.py` makes app a regular package. The functions return answers instead
of printing them, so tests can check the values. Type hints describe intended
numeric inputs/results; Python does not enforce or convert them automatically.

## 6. Write tests using Arrange–Act–Assert

Create `tests/test_operations.py`. Begin with:

```python
from app.operations import add, subtract


def test_add_positive_numbers():
    # Arrange: inputs and an independently known answer.
    first, second = 2, 3
    expected = 5

    # Act: exercise the function.
    result = add(first, second)

    # Assert: verify the result.
    assert result == expected
```

Using that pattern, write the remaining tests:

| Function | Inputs | Expected | Suggested test name |
| --- | --- | --- | --- |
| add | -2, -3 | -5 | test_add_negative_numbers |
| add | 5, 0 | 5 | test_add_zero |
| subtract | 5, 3 | 2 | test_subtract_positive_numbers |
| subtract | -5, -3 | -2 | test_subtract_negative_numbers |
| subtract | 0, 5 | -5 | test_subtract_zero |

Each test should have its own Arrange, Act, and Assert sections. `=` assigns a
value; `==` compares values. Do not calculate expected by calling the function
under test: that could compare the same bug with itself. No fixtures, test classes,
or `import pytest` are needed here. See the [six reference tests](tests/test_operations.py)
after attempting your own.

## 7. Run, understand a failure, and repair it

Run from the project root:

```bash
python -m pytest --collect-only -q
python -m pytest -v
python -m pytest tests/test_operations.py::test_add_positive_numbers -v
```

**Check:** six tests are collected and pass; the final command runs one selected
test. pytest automatically discovers and calls the tests. No GitHub workflow is
required for this automation.

Practice changing the first expected value from 5 to 6. Save and rerun that test.
Explain the failure, then restore 5. Here the expectation was wrong. Next, change
addition's implementation to `a - b`, run the suite, and identify the failing
examples. Restore `a + b`. Here the implementation was wrong. Finish with six passes.

## 8. Verify `.gitignore` and update README

```bash
git status --short
git check-ignore -v .venv/ __pycache__/ .pytest_cache/
```

**Check:** generated files are absent from ordinary status, and check-ignore
shows the matching rules. Source/tests/configuration should still appear as new
files. `??` means untracked. Ignored files stay on disk; they are normally excluded
from staging as untracked content. Do not force-add them.

Update README with the project purpose, Python version, environment creation and
activation commands, `python -m pip install -r requirements.txt`, and
`python -m pytest -v`. Explain AAA and why generated files are ignored.

## 9. Review, commit, and push

```bash
git status
git diff
git add README.md .gitignore requirements.txt pytest.ini app/__init__.py app/operations.py tests/test_operations.py
git diff --cached
git commit -m "Add addition and subtraction with AAA tests"
git push
git status
git log --oneline
```

`diff` shows edits to tracked files, not new untracked file contents. `add` stages
the intended files; `diff --cached` reviews that selection. A commit records them
locally; push sends the commit to GitHub. If Git requests an author identity,
configure your own name/email for this repository and retry the commit:

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR GIT EMAIL"
```

Replace the placeholders. Author settings do not authenticate you to GitHub.
Use the course-supported sign-in method if push requests authentication; do not
store tokens or passwords in project files.

**Final check:** refresh GitHub. Verify the final commit, README, `.gitignore`,
requirements, configuration, app, and tests are present. The environment/caches
must be absent. Your local working tree should be clean. Run `deactivate` when done.

## If you get stuck

| Symptom | First check |
| --- | --- |
| No module named pytest | Active interpreter and installation |
| No module named app | Current folder, saved files, exact package name |
| No tests collected | tests folder, test_ naming, pytest.ini |
| Environment appears in status | Exact .gitignore name/location and whether files were already tracked |
| Push fails | Read the message; resolve sign-in or remote changes with help, not force-push |

For help, provide the command, expected result, and actual error as text.
Review the [assessment checklist](ASSESSMENT.md) before submitting.
