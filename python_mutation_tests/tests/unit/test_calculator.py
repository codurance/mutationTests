from calculator import calculator


class TestCalculator:
    def test_basic_add(self):
        # Given
        summand = 1

        # When
        result = calculator.add(summand, summand)

        # Then
        assert result == 2

    def test_subtract(self):
        # Given
        minuend = 0
        subtrahend = 0

        # When
        result = calculator.subtract(minuend, subtrahend)

        # Then
        assert result == 0

    def test_multiply(self):
        # Given
        factor = 1

        # When
        result = calculator.multiply(factor, factor)

        # Then
        assert result == 1
