# IS 218: Build and Test a Python Calculator

Learn to structure a Python application, build a Read–Evaluate–Print–Loop
(REPL), and write tests using Arrange–Act–Assert (AAA). This repository is a
**model example of professional software engineering** for junior software
engineers in training.

Start with the [step-by-step student lab](part1.md). It explains how to manually
recreate the project in a separate folder, with code exercises, commands,
checkpoints, and troubleshooting. Source files and tests also contain teaching
comments explaining the decisions behind the code.

## 🎯 Project Structure Overview

This is a professional example demonstrating **industry best practices**:

```
is218_handsOn1_example/
├── app/                    # Application package
│   ├── __init__.py        # Package initialization
│   ├── operations.py      # Core arithmetic operations (7 functions)
│   └── cli.py             # Interactive REPL interface
├── tests/                 # Test suite
│   ├── __init__.py
│   └── test_operations.py # 33 comprehensive unit tests (100% coverage)
├── calculator.py          # CLI entry point script
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 📋 Development Workflow for Students

This repository demonstrates **issue-driven development** with structured GitHub Issues and logical Git commits:

### GitHub Issues (Atomic Units of Work)

All development is organized as issues with clear acceptance criteria:

| Issue | Title | Description |
|-------|-------|-------------|
| #1 | Setup: Project Configuration and Dependencies | pytest.ini, requirements.txt, .gitignore |
| #2 | Feature: Implement Core Arithmetic Operations | 7 arithmetic functions with validation |
| #3 | Test: Comprehensive Test Suite | 33 tests across 7 test classes |
| #4 | Feature: CLI REPL Calculator Interface | Interactive calculator with history |
| #5 | Documentation: Entry Point and README | calculator.py entry point and docs |

Each issue includes:
- ✅ Clear acceptance criteria (checkboxes)
- 📚 Learning objectives for students
- 📝 Linked to relevant commits

### Commit History (Logical Progression)

The Git history shows the **ordered construction** of the repository:

```bash
git log --oneline --decorate
```

Output:
```
62b690e (HEAD -> main) feat(entry): create calculator CLI entry point script (#5)
6695388 feat(cli): build interactive REPL calculator interface (#4)
941cfb9 test: create comprehensive test suite for arithmetic operations (#3)
15c7e73 feat(operations): implement core arithmetic operations module (#2)
601d243 feat(setup): configure pytest and project dependencies (#1)
595d9fc initial part 1 added
fcbe627 Initial commit
```

Each commit:
- Uses **conventional commit format** (feat:, test:, fix:)
- References issue number (#N)
- Includes detailed explanation of changes
- Lists key features and learning points

### How to Explore the Development History

```bash
# View commit history in nice format
git log --oneline --graph --decorate

# See detailed commit message (includes learning objectives)
git show 601d243

# View all commits for an issue
git log --grep="#1"

# See what changed in a specific commit
git diff 601d243^..601d243

# View commit by author
git log --author="kwilliams"
```

## 🚀 Run the completed example

Run these commands from this repository's root on macOS/Linux:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies (pytest)
python -m pip install -r requirements.txt

# Run all tests (should show 33 passed)
python -m pytest

# Start interactive calculator
python calculator.py
```

On Windows PowerShell, create the environment with `py -3 -m venv .venv` and
activate it with `.\.venv\Scripts\Activate.ps1`; then use the same `python`
commands. If `.venv` already exists, activate it and continue. The original
classroom environment uses Python 3.9.6 and pytest 8.4.2; the package versions
are retained in [requirements.txt](requirements.txt).

### Using the Calculator

At `calc>` prompt, try these operations:

```
calc> 5 + 3        # Addition
15.0 + 7.0 = 22.0

calc> 20 - 8       # Subtraction
20.0 - 8.0 = 12.0

calc> 6 * 9        # Multiplication
6.0 * 9.0 = 54.0

calc> 100 / 4      # Division
100.0 / 4.0 = 25.0

calc> 23 % 5       # Modulo (remainder)
23.0 % 5.0 = 3.0

calc> 2 ** 8       # Power (exponentiation)
2.0 ** 8.0 = 256.0

calc> sqrt 25      # Square root
sqrt(25.0) = 5.0

calc> history      # Show calculation history
Calculation History:
  1. 5.0 + 3.0 = 8.0
  2. 10.0 - 2.0 = 8.0
  ...

calc> help         # Show help menu
calc> clear        # Clear history
calc> exit         # Exit calculator
```

## 📚 Reading Map

| File | What Students Learn |
| --- | --- |
| [README.md](README.md) | **This guide**: Project structure, workflow, best practices |
| [part1.md](part1.md) | Manual construction, environment setup, AAA, REPL, professional workflow |
| [app/__init__.py](app/__init__.py) | Packages, imports, avoiding import side effects |
| [app/operations.py](app/operations.py) | Function design, contracts, validation, documentation, type hints |
| [app/cli.py](app/cli.py) | REPL patterns, parsing, dispatch, user interaction, state management |
| [calculator.py](calculator.py) | Entry point scripts and the main guard pattern |
| [tests/test_operations.py](tests/test_operations.py) | Unit tests, AAA pattern, edge cases, error testing, pytest best practices |
| [pytest.ini](pytest.ini) | Test discovery configuration |
| [requirements.txt](requirements.txt) | Dependency management |
| [.gitignore](.gitignore) | Git best practices |

## 🎓 Key Learning Objectives

Working through this project, students will learn:

### Python Development
- ✅ Function design with clear contracts
- ✅ Type hints and comprehensive docstrings
- ✅ Error handling and input validation
- ✅ Module organization and packages
- ✅ Professional Python coding standards

### Testing & Quality Assurance
- ✅ Test-driven development (TDD) principles
- ✅ Comprehensive edge case testing
- ✅ Pytest fixtures, assertions, and best practices
- ✅ Testing error conditions and exceptions
- ✅ Achieving 100% code coverage

### Software Engineering Practices
- ✅ **Issue-driven development workflow**
- ✅ **Conventional commit messages**
- ✅ **Logical, atomic commits**
- ✅ **Git workflow and history navigation**
- ✅ Professional documentation standards

### User Interface Development
- ✅ Command-line interface (CLI) design
- ✅ REPL (Read-Eval-Print-Loop) patterns
- ✅ User input handling and validation
- ✅ Error messages and user feedback
- ✅ State management in applications

### Project Organization
- ✅ Professional project structure
- ✅ Virtual environment management
- ✅ Dependency tracking with requirements.txt
- ✅ Git ignore best practices
- ✅ Configuration management

## 🧪 Testing

The test suite includes **33 comprehensive tests** organized into 7 test classes:

```bash
# Run all tests
pytest

# Run with verbose output showing each test
pytest -v

# Run specific test class
pytest tests/test_operations.py::TestAddition -v

# Run with coverage report
pytest --cov=app tests/
```

**Expected output:**
```
============================= 33 passed in 0.01s ==============================
```

### Test Coverage by Operation

- **Addition** (5 tests): positive, negative, mixed, zero, decimals
- **Subtraction** (5 tests): all number types
- **Multiplication** (5 tests): all number types
- **Division** (5 tests): all types + zero-division error
- **Modulo** (4 tests): positive, negative, remainder, zero-divisor error
- **Power** (5 tests): positive exponent, zero, negative, fractional, negative base
- **Square Root** (4 tests): perfect squares, zero, decimals, negative error

## 🚢 Advanced: Contributing

To add new features or fix issues following this workflow:

```bash
# 1. Create a GitHub Issue describing the work
#    (Use gh issue create or github.com/issues/new)

# 2. Create a feature branch
git checkout -b feature/issue-#N

# 3. Make logical commits referencing the issue
git commit -m "feat(module): description (#N)

- Detailed explanation
- Key features
- Learning objectives"

# 4. Ensure all tests pass
pytest

# 5. Submit a pull request with clear description
# (Link to the issue in the PR description)
```

## 🔧 Troubleshooting

### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Import Errors

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Verify pytest is installed
pip list | grep pytest
```

### Calculator Won't Start

```bash
# Try explicit Python path
python3 calculator.py

# Or use module execution
python -m app.cli
```

### Test Failures

```bash
# Run tests with verbose output and full tracebacks
pytest -vv --tb=long

# Run a specific failing test
pytest tests/test_operations.py::TestDivision::test_divide_by_zero -v
```

## 📖 Additional Resources for Students

### Python Resources
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

### Testing Resources
- [Pytest Documentation](https://docs.pytest.org/)
- [Real Python Testing Tutorial](https://realpython.com/python-testing/)
- [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

### Git & Professional Practices
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Documentation](https://git-scm.com/doc)
- [Professional Git Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows)

## 💡 Key Takeaways

This project demonstrates that **professional software engineering** involves:

1. **Clear Organization**: Logical project structure and file organization
2. **Quality Code**: Type hints, docstrings, error handling
3. **Comprehensive Testing**: Edge cases, error conditions, high coverage
4. **Good Documentation**: README, commit messages, code comments
5. **Professional Workflow**: Issues, branches, meaningful commits
6. **User Experience**: Helpful error messages, clear interface

These practices make code:
- ✅ Maintainable
- ✅ Understandable
- ✅ Reliable
- ✅ Professional-grade
- ✅ Educational for junior engineers
