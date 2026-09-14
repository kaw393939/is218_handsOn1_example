#!/usr/bin/env python3
"""Start the calculator with ``python calculator.py`` from the project root.

The shebang above selects python3 through PATH when an executable script is
launched directly on Unix. It is a comment when using ``python calculator.py``.
Keep this entry point small: reusable behavior lives in the app package.
"""

from app.cli import main


# A directly executed file has __name__ == '__main__'. An imported module has
# its module name instead. This guard lets tools/tests import calculator safely
# without asking for keyboard input as an unintended import side effect.
if __name__ == '__main__':
    main()
