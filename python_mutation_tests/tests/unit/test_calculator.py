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

    def test_divide_should_return_always_an_integer_as_a_result_of_the_division(  # noqa: E501 <-this is just to allow this long line when linting
        self,
    ):
        # Given
        dividend = 105
        divisor = 10

        # When
        result = calculator.divide(dividend, divisor)

        # Then
        assert result == 10

    def test_summation_should_return_zero_when_starting_at_zero(self):
        # Given
        start = 0

        # When
        result = calculator.summation(start)

        # Then
        assert result == 0

    def test_summation_should_return_one_when_starting_at_one(self):
        # Given
        start = 1

        # When
        result = calculator.summation(start)

        # Then
        assert result == 1

    def test_summation_should_return_the_sum_of_all_integers_from_start_downward_to_zero(  # noqa: E501 <-this is just to allow this long line when linting
        self,
    ):
        # Given
        start = 2

        # When
        result = calculator.summation(start)

        # Then
        assert result == 3

    def test_positive_should_true_if_the_term_is_a_positive_number(self):
        # Given
        term = 2

        # When
        result = calculator.is_positive(term)

        # Then
        assert result

    def test_positive_should_false_if_the_term_is_a_negative_number(self):
        # Given
        term = -2

        # When
        result = calculator.is_positive(term)

        # Then
        assert not result
