from calculator import calculator


class TestCalculator:
    def test_basic_add(self):
        # Given
        summand = 1
        
        # When
        result = calculator.add(summand, summand)
        
        # Then
        assert result == 2
