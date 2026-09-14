"""Six examples using Arrange, Act, Assert (AAA)."""

from app.operations import add, subtract


def test_add_positive_numbers():
    # Arrange: choose inputs and an independently known answer.
    first, second = 2, 3
    expected = 5

    # Act: call the function under test.
    result = add(first, second)

    # Assert: check the observed result.
    assert result == expected


def test_add_negative_numbers():
    # Arrange
    first, second = -2, -3
    expected = -5

    # Act
    result = add(first, second)

    # Assert
    assert result == expected


def test_add_zero():
    # Arrange
    first, second = 5, 0
    expected = 5

    # Act
    result = add(first, second)

    # Assert
    assert result == expected


def test_subtract_positive_numbers():
    # Arrange
    first, second = 5, 3
    expected = 2

    # Act
    result = subtract(first, second)

    # Assert
    assert result == expected


def test_subtract_negative_numbers():
    # Arrange
    first, second = -5, -3
    expected = -2

    # Act
    result = subtract(first, second)

    # Assert
    assert result == expected


def test_subtract_zero():
    # Arrange
    first, second = 0, 5
    expected = -5

    # Act
    result = subtract(first, second)

    # Assert
    assert result == expected
