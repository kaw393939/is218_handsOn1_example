"""
Core calculator operations module.

Provides addition, subtraction, multiplication, division, modulo, powers, and
square roots. These functions contain the business logic, independent of the
terminal interface: no input(), print(), or shared mutable history lives here.

For ordinary numeric inputs, these are pure functions: they compute a result
without changing external state. That makes focused, repeatable unit tests easy.
Validation failures raise exceptions; the CLI decides how to display them.

Annotations such as ``a: float`` and ``-> float`` describe intended numeric
inputs/results but do not convert or validate them. The CLI explicitly converts
input with float(). Direct callers can pass integers, which may produce integer
results. Python power can even produce complex results (see power's docstring).
Docstrings describe the contract; comments explain design decisions.
"""


def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    # Return a value, not a printed message: presentation belongs to the caller.
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract second number from first.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Returns:
        The difference (a - b)
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide first number by second.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The quotient (a / b)

    Raises:
        ValueError: If b is zero (division by zero)
    """
    # A guard clause rejects invalid input before the normal calculation.
    # ValueError is this application's chosen contract, rather than letting
    # Python's built-in ZeroDivisionError leak through for this operation.
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a: float, b: float) -> float:
    """Calculate remainder of a divided by b.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The remainder (a % b)

    Raises:
        ValueError: If b is zero
    """
    # Use the same explicit validation policy as divide(). Tests check both
    # the exception type and its message so callers can rely on the contract.
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero divisor")
    # Python's nonzero remainder has the divisor's sign: -10 % 3 is 2.
    return a % b


def power(a: float, b: float) -> float:
    """Raise first number to power of second.

    Args:
        a: Base
        b: Exponent

    Returns:
        The result of a raised to power b

    This thin wrapper follows Python's ** behavior. For example, a negative
    base with a fractional exponent can return complex despite the float hint;
    zero to a negative power raises ZeroDivisionError. A stricter real-number
    calculator would need an explicit domain policy and corresponding tests.
    """
    return a ** b


def square_root(a: float) -> float:
    """Calculate square root of a number.

    Args:
        a: Number to find square root of

    Returns:
        The square root of a

    Raises:
        ValueError: If a is negative
    """
    # This operation deliberately supports real square roots only. Zero is a
    # valid boundary case, so use < 0, not <= 0. Test both zero and negatives.
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    # Raising to one-half computes the square root. For inexact floating-point
    # results, tests should compare with pytest.approx instead of exact equality.
    return a ** 0.5
