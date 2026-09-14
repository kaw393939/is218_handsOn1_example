# Assessment Checklist

[Study guide](TEST_GUIDE.md) · [Contents](README.md)

Create your own GitHub repository with a README, clone it, and build this small
addition/subtraction project. Follow the instructor's naming, visibility,
reference-use, time, and assistance rules.

| Requirement | Points | Demonstrate |
| --- | ---: | --- |
| GitHub and clone | 15 | Create with README, clone, verify folder and origin |
| `.gitignore` | 15 | Exclude .venv and caches, verify rules, commit the ignore file |
| Python environment | 15 | Create, activate, and verify the selected interpreter |
| pytest setup | 15 | Install from requirements.txt and explain pytest.ini discovery |
| Functions and AAA tests | 25 | Addition/subtraction, positive/negative/zero examples, passing tests |
| Understand a failure | 5 | Explain and repair a wrong expectation or implementation |
| README and Git handoff | 10 | Document setup, review changes, stage, commit, push, verify GitHub |

The six reference tests are practice examples, not a large test-count target.
Be ready to explain Arrange, Act, and Assert and use different input values.
No classes, REPL, fixtures, mocking, division, or GitHub Actions are required.

## Before submitting

- [ ] Tests pass using `python -m pytest -v` from the project root.
- [ ] `.gitignore` is committed; `.venv`, bytecode, and pytest caches are not.
- [ ] README explains environment setup, dependency installation, and testing.
- [ ] Source, tests, requirements.txt, and pytest.ini are committed and pushed.
- [ ] GitHub shows the same final commit as the local log.

Submit your repository URL and any command output the instructor requests.
Do not copy passing output from the guide or include credentials.

## Be able to explain

1. How do clone, add, commit, and push differ?
2. Why commit `.gitignore` but exclude `.venv`?
3. How do you know which Python runs pytest?
4. What do requirements.txt and pytest.ini each control?
5. Why must the test's expected answer be independent of the function?
