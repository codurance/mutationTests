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

    def test_dividing_zero_should_return_zero(self):
        # Given
        dividend = 0
        divisor = 100

        # When
        result = calculator.divide(dividend, divisor)

        # Then
        assert result == 0

    def test_divide_should_return_always_an_integer_as_a_result_of_the_division(
        self,
    ):
        # Given
        dividend = 105
        divisor = 10

        # When
        result = calculator.divide(dividend, divisor)

        # Then
        assert result == 10
