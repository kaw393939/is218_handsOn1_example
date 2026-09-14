"""The calculator's application package.

``__init__.py`` identifies this directory as a regular Python package. Python
executes it on the first import of ``app`` in a process, including imports such
as ``from app.operations import add``. Keep package initialization lightweight:
importing arithmetic for a test must not start an interactive input loop.

The demo below is an introductory import exercise, not part of the calculator's
execution path. Try ``from app import demo`` followed by ``demo()`` in Python.
"""


def demo():
    """Print a package-import demonstration; return None implicitly.

    Defining a function does not execute its body. Printing happens only when
    someone calls ``demo()``. Compare this with operations.add, which returns a
    value for its caller to use instead of printing it.
    """
    print("This is a demo function from the app package.")
