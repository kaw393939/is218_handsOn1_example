"""Unit tests for the arithmetic contract, organized with AAA.

ARRANGE prepares inputs and an independently known expected answer.
ACT calls the behavior under test once.
ASSERT compares the observed result with the expectation.

Keeping these phases visible helps a failed test tell a clear story. Do not
compute the expected value by calling the function being tested: the same bug
would appear on both sides. Tests use fixed data, no keyboard input, and no
shared state, so they are repeatable and can run in any order.

pytest discovers the Test* classes and test_* methods through pytest.ini.
Classes only group related tests; they do not need unittest.TestCase or __init__.
"""

# pytest is a development dependency; production arithmetic does not import it.
import pytest

# Import the actual production functions rather than copying their algorithms.
from app.operations import (
    add, subtract, multiply, divide, modulo, power, square_root
)


class TestAddition:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 2
        second = 3
        expected = 5

        # Act: exercise the function once.
        result = add(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = -2
        second = -3
        expected = -5

        # Act: exercise the function once.
        result = add(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = -5
        expected = 5

        # Act: exercise the function once.
        result = add(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    # Each row becomes a separate test case with its own failure report.
    @pytest.mark.parametrize(
        "first, second, expected",
        [
            (0, 5, 5),
            (5, 0, 5),
            (0, 0, 0),
        ],
    )
    def test_add_zero(self, first, second, expected):
        """Test adding with zero."""
        # Arrange: pytest supplies the inputs and expected answer from one row.

        # Act: exercise the function once.
        result = add(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_add_decimals(self):
        """Test adding decimal numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 1.5
        second = 2.5
        expected = 4.0

        # Act: exercise the function once.
        result = add(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 5
        second = 3
        expected = 2

        # Act: exercise the function once.
        result = subtract(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = -5
        second = -3
        expected = -2

        # Act: exercise the function once.
        result = subtract(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_subtract_mixed_numbers(self):
        """Test subtracting positive and negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = -5
        expected = 15

        # Act: exercise the function once.
        result = subtract(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    # Each row becomes a separate test case with its own failure report.
    @pytest.mark.parametrize(
        "first, second, expected",
        [
            (5, 0, 5),
            (0, 5, -5),
        ],
    )
    def test_subtract_zero(self, first, second, expected):
        """Test subtracting with zero."""
        # Arrange: pytest supplies the inputs and expected answer from one row.

        # Act: exercise the function once.
        result = subtract(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_subtract_decimals(self):
        """Test subtracting decimal numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 5.5
        second = 2.5
        expected = 3.0

        # Act: exercise the function once.
        result = subtract(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 2
        second = 3
        expected = 6

        # Act: exercise the function once.
        result = multiply(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = -2
        second = -3
        expected = 6

        # Act: exercise the function once.
        result = multiply(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = -5
        expected = -50

        # Act: exercise the function once.
        result = multiply(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    # Each row becomes a separate test case with its own failure report.
    @pytest.mark.parametrize(
        "first, second, expected",
        [
            (0, 5, 0),
            (5, 0, 0),
            (0, 0, 0),
        ],
    )
    def test_multiply_zero(self, first, second, expected):
        """Test multiplying with zero."""
        # Arrange: pytest supplies the inputs and expected answer from one row.

        # Act: exercise the function once.
        result = multiply(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_multiply_decimals(self):
        """Test multiplying decimal numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 1.5
        second = 2.5
        expected = 3.75

        # Act: exercise the function once.
        result = multiply(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)


class TestDivision:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = 2
        expected = 5

        # Act: exercise the function once.
        result = divide(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = -10
        second = -2
        expected = 5

        # Act: exercise the function once.
        result = divide(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = -2
        expected = -5

        # Act: exercise the function once.
        result = divide(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_divide_decimals(self):
        """Test dividing decimal numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 7.5
        second = 2.5
        expected = 3.0

        # Act: exercise the function once.
        result = divide(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        # Arrange: choose an input that the documented contract rejects.
        first = 10
        second = 0

        # Assert + Act: the context manager must surround the failing call.
        # pytest.raises fails if no exception (or the wrong type/message) occurs.
        with pytest.raises(ValueError, match='Cannot divide by zero'):
            divide(first, second)


class TestModulo:
    """Test cases for the modulo function."""

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = 3
        expected = 1

        # Act: exercise the function once.
        result = modulo(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        # Arrange: choose a concrete example and its known answer.
        first = -10
        second = 3
        expected = 2

        # Act: exercise the function once.
        result = modulo(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_modulo_zero_remainder(self):
        """Test modulo with zero remainder."""
        # Arrange: choose a concrete example and its known answer.
        first = 10
        second = 5
        expected = 0

        # Act: exercise the function once.
        result = modulo(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_modulo_by_zero(self):
        """Test that modulo by zero raises ValueError."""
        # Arrange: choose an input that the documented contract rejects.
        first = 10
        second = 0

        # Assert + Act: the context manager must surround the failing call.
        # pytest.raises fails if no exception (or the wrong type/message) occurs.
        with pytest.raises(ValueError, match='Cannot calculate modulo with zero divisor'):
            modulo(first, second)


class TestPower:
    """Test cases for the power function."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        # Arrange: choose a concrete example and its known answer.
        first = 2
        second = 3
        expected = 8

        # Act: exercise the function once.
        result = power(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        # Arrange: choose a concrete example and its known answer.
        first = 5
        second = 0
        expected = 1

        # Act: exercise the function once.
        result = power(first, second)

        # Assert: verify the observable return value.
        assert result == expected

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        # Arrange: choose a concrete example and its known answer.
        first = 2
        second = -1
        expected = 0.5

        # Act: exercise the function once.
        result = power(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        # Arrange: choose a concrete example and its known answer.
        first = 4
        second = 0.5
        expected = 2.0

        # Act: exercise the function once.
        result = power(first, second)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_power_negative_base(self):
        """Test power with negative base."""
        # Arrange: choose a concrete example and its known answer.
        first = -2
        second = 3
        expected = -8

        # Act: exercise the function once.
        result = power(first, second)

        # Assert: verify the observable return value.
        assert result == expected


class TestSquareRoot:
    """Test cases for the square_root function."""

    # Each row becomes a separate test case with its own failure report.
    @pytest.mark.parametrize(
        "number, expected",
        [
            (4, 2.0),
            (9, 3.0),
            (16, 4.0),
        ],
    )
    def test_square_root_perfect_squares(self, number, expected):
        """Test square root of perfect squares."""
        # Arrange: pytest supplies the inputs and expected answer from one row.

        # Act: exercise the function once.
        result = square_root(number)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_square_root_zero(self):
        """Test square root of zero."""
        # Arrange: choose a concrete example and its known answer.
        number = 0
        expected = 0.0

        # Act: exercise the function once.
        result = square_root(number)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_square_root_decimals(self):
        """Test square root of decimal numbers."""
        # Arrange: choose a concrete example and its known answer.
        number = 2.25
        expected = 1.5

        # Act: exercise the function once.
        result = square_root(number)

        # Assert: verify the observable return value.
        assert result == pytest.approx(expected)

    def test_square_root_negative(self):
        """Test that square root of negative raises ValueError."""
        # Arrange: choose an input that the documented contract rejects.
        number = -4

        # Assert + Act: the context manager must surround the failing call.
        # pytest.raises fails if no exception (or the wrong type/message) occurs.
        with pytest.raises(ValueError, match='Cannot calculate square root of negative number'):
            square_root(number)


def test_add_inexact_decimals():
    """Binary floating point needs a tolerance for values such as 0.1 + 0.2."""
    # Arrange: the expected answer comes from the mathematical requirement.
    first = 0.1
    second = 0.2
    expected = 0.3

    # Act
    result = add(first, second)

    # Assert: approx accepts a small numerical difference, not arbitrary errors.
    assert result == pytest.approx(expected)


def test_square_root_irrational_result():
    """Use a known approximate answer for a result with no finite decimal form."""
    # Arrange
    number = 2
    expected = 1.4142135623730951

    # Act
    result = square_root(number)

    # Assert
    assert result == pytest.approx(expected)
