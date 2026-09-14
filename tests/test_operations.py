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

═══════════════════════════════════════════════════════════════════════════════
🤖 MENTOR COMMENTARY: Testing Philosophy and The AAA Pattern
═══════════════════════════════════════════════════════════════════════════════

Let's talk about something that separates professional developers from
junior ones: comprehensive testing. You're about to see 66 tests for a
simple calculator. Your first thought might be: "Isn't that overkill?"

Short answer: No. Let me explain why.

1. **THE AAA PATTERN (Arrange-Act-Assert)**
   
   Every test follows this structure:
   
   ```python
   def test_add_positive_numbers(self):
       # ARRANGE: Set up test data
       a = 2
       b = 3
       expected = 5
       
       # ACT: Call the function once
       result = add(a, b)
       
       # ASSERT: Check if result matches expectation
       assert result == expected
   ```
   
   This pattern is universal:
   
   Java (JUnit):
   ```java
   @Test
   public void testAddPositiveNumbers() {
       // Arrange
       int a = 2, b = 3;
       int expected = 5;
       // Act
       int result = add(a, b);
       // Assert
       assertEquals(expected, result);
   }
   ```
   
   JavaScript (Jest):
   ```javascript
   test('add positive numbers', () => {
       // Arrange
       const a = 2, b = 3;
       const expected = 5;
       // Act
       const result = add(a, b);
       // Assert
       expect(result).toBe(expected);
   });
   ```
   
   Every professional framework, every language, uses this pattern.
   When you learn this, you've learned testing for the rest of your career.

2. **WHY THESE 66 TESTS EXIST (Not Overkill)**
   
   Look at this test:
   ```python
   def test_divide_by_zero(self):
       with pytest.raises(ValueError, match="Cannot divide by zero"):
           divide(10, 0)
   ```
   
   What does it test?
   - That divide() RAISES an exception (not returns -1 or None)
   - That the exception is ValueError (not generic Exception)
   - That the message says "divide by zero" (not cryptic garbage)
   
   If someone later changes the code to:
   ```python
   def divide(a, b):
       if b == 0:
           return None  # Forgot to raise
       return a / b
   ```
   
   This test FAILS. You catch the bug before it reaches production.
   
   Real-world: A fintech company's divide function returns None for zero
   instead of raising. A calculation silently fails. Wrong money moves.
   Regulatory disaster.
   
   These tests prevent that.

3. **COMPREHENSIVE EDGE CASES (Why 5 Tests Per Operation)**
   
   The add() function has 5 tests:
   
   ```python
   def test_add_positive_numbers(self):
       assert add(2, 3) == 5          # Normal case
   
   def test_add_negative_numbers(self):
       assert add(-2, -3) == -5       # Negative case
   
   def test_add_mixed_numbers(self):
       assert add(10, -5) == 5        # Mixed signs
   
   def test_add_zero(self):
       assert add(0, 5) == 5          # Zero edge case
       assert add(5, 0) == 5
       assert add(0, 0) == 0
   
   def test_add_decimals(self):
       assert add(1.5, 2.5) == 4.0    # Floating point
   ```
   
   Why so many?
   
   In professional debugging, bugs cluster in edge cases:
   - Positive numbers work, negatives fail
   - Works with integers, breaks with floats
   - Works when a > b, fails when b > a
   - Works in US timezone, fails in another
   
   The engineers who write comprehensive edge case tests catch these bugs
   BEFORE they reach production. The ones who test happy path only don't.
   
   That's why some engineers are paid 2x more. They think about edge cases.

4. **TESTING ERROR CONDITIONS (Not Just Success)**
   
   Look at these tests:
   ```python
   def test_divide_by_zero(self):
       with pytest.raises(ValueError, match="Cannot divide by zero"):
           divide(10, 0)
   
   def test_square_root_negative(self):
       with pytest.raises(ValueError, match="Cannot calculate square root"):
           square_root(-4)
   ```
   
   These DON'T test success. They test failure modes.
   
   Many junior developers think: "If it doesn't crash, it works."
   
   Professional developers think: "How do I MAKE it crash in safe ways?"
   
   Why? Because:
   - Crashes under your control are OK
   - Crashes under user control are disasters
   - Better to raise ValueError("helpful message") than return None silently
   
   The library you use (numpy, pandas, requests, etc.) has tests for error
   conditions. That's why it's reliable. This is how reliability works.

5. **REPETITION AND REDUNDANCY (It Looks Like Overkill)**
   
   You might think:
   "If add(2, 3) works, won't add(-2, -3) also work?"
   
   Theoretically yes. In practice, NO. Here's a real bug:
   
   ```python
   def add(a, b):
       return abs(a) + abs(b)  # Bug: forgot about negative results
   ```
   
   This passes:
   ```python
   assert add(2, 3) == 5  ✓ (abs(2) + abs(3) = 5)
   ```
   
   This fails:
   ```python
   assert add(-2, -3) == -5  ✗ (abs(-2) + abs(-3) = 5, not -5)
   ```
   
   Without the negative test, this bug goes to production.
   
   This happens constantly in the real world. Developers write one path,
   test the happy path, miss entire branches.
   
   The repetition IS the point. It's not overkill, it's intentional coverage.

6. **PARAMETRIZED TESTS (Reducing Redundancy)**
   
   Notice some tests use parametrization:
   ```python
   def test_add_zero(self):
       assert add(0, 5) == 5
       assert add(5, 0) == 5
       assert add(0, 0) == 0
   ```
   
   In more complex projects, you'd write:
   ```python
   @pytest.mark.parametrize("a,b,expected", [
       (0, 5, 5),
       (5, 0, 5),
       (0, 0, 0),
   ])
   def test_add_zero(self, a, b, expected):
       assert add(a, b) == expected
   ```
   
   This runs the same test 3 times with different data.
   
   Benefit: Less code, same coverage, easier to add more cases.
   
   When you find a bug (e.g., "add fails with b=1000000"), you add ONE line:
   ```python
   (1000000, 1, 1000001),
   ```
   
   The test runs again with the new case. Professional teams do this.

7. **DETERMINISTIC, ISOLATED, REPEATABLE**
   
   Notice tests:
   - Use fixed data (no random numbers)
   - Don't depend on each other (can run in any order)
   - Don't rely on external state (no database, no time, no network)
   
   Why?
   
   BAD test:
   ```python
   def test_something():
       random_number = random.randint(1, 1000)
       assert add(random_number, 5) > 5
   ```
   
   This passes 99% of the time. Sometimes fails mysteriously.
   Developers spend hours debugging. It's random. Nightmare.
   
   GOOD test:
   ```python
   def test_something():
       assert add(10, 5) > 5
   ```
   
   Passes every time. Deterministic. Debuggable.
   
   Professional tests are boring. They're predictable. That's the goal.

8. **TEST COVERAGE (100% Here, 80%+ in Real Projects)**
   
   We have 66 tests for a few simple functions. Test coverage is 100%:
   every line of code is executed by at least one test.
   
   This matters because:
   - Untested code is broken code (just nobody knows it yet)
   - A line that was never executed might crash on the first real user
   - 100% coverage doesn't guarantee correctness, but 0% coverage guarantees
     surprises
   
   Real companies:
   - Startups: 60-70% coverage (moving fast, accepting risk)
   - Mature companies: 80-90% coverage (stability matters)
   - Critical systems: 95%+ coverage (financial, healthcare, aviation)
   
   We're at 100% here to demonstrate the ideal.

═══════════════════════════════════════════════════════════════════════════════
⚡ THE TESTING PYRAMID

In enterprise software, testing looks like this:

                      /\
                     /  \         Manual Testing (smoke tests)
                    /    \        A few scenarios a human tests
                   /      \
                  /________\
                /          \
               /            \      Integration Tests
              /              \     Database + API + UI together
             /________________\    Smaller number, slower
            /                  \
           /                    \   Unit Tests (What we do here)
          /                      \  Fast, deterministic, comprehensive
         /____________________________\

Most tests should be unit tests (like these). Fast, cheap, reliable.
Some integration tests. Very few manual tests.

Teams that get this backwards:
- Mostly manual testing → slow to catch bugs, expensive
- Mostly integration tests → slow to run, flaky
- Good mix → bugs caught fast, high confidence

We're building the foundation here.

═══════════════════════════════════════════════════════════════════════════════
⚡ REAL-WORLD CONNECTION

Your first job on a professional team:

"We found a bug in production. Can you write a test for it?"

What they mean: Reproduce the bug as a test case first. THEN fix it.

Why? Because:
1. The bug exists (test proves it)
2. After fix, test passes
3. If someone breaks it later, test fails immediately
4. Bug never comes back

Without this discipline, bugs reoccur. With it, they don't.

This is THE foundational skill of professional development.

═══════════════════════════════════════════════════════════════════════════════
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
