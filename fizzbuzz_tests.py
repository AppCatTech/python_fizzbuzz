import unittest
from parameterized import parameterized
from get_fizzbuzz_value.get_fizzbuzz_value import get_fizzbuzz_value


class GetFizzBuzzValueTests(unittest.TestCase):
    @parameterized.expand([
        [1, '1'],
        [2, '2'],
        [4, '4']
    ])
    def test_it_returns_string_version_of_integer_when_not_divisible_by_3_or_5(self, input_value, expected_result):
        result = get_fizzbuzz_value(input_value)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        [3],
        [6],
        [9],
    ])
    def test_it_returns_Fizz_when_given_multiples_of_3(self, input_value):
        result = get_fizzbuzz_value(input_value)
        self.assertEqual('Fizz', result)

    @parameterized.expand([
        [5],
        [10],
        [20],
    ])
    def test_it_returns_Buzz_when_given_multiples_of_5(self, input_value):
        result = get_fizzbuzz_value(input_value)
        self.assertEqual('Buzz', result)

    @parameterized.expand([
        [15],
        [30],
    ])
    def test_it_returns_FizzBuzz_when_given_multiples_of_3_and_5(self, input_value):
        result = get_fizzbuzz_value(input_value)
        self.assertEqual('FizzBuzz', result)

    def test_it_raises_a_TypeError_when_not_given_integer_input(self):
        with self.assertRaisesRegex(TypeError, 'get_fizzbuzz_value did not receive integer input'):
            get_fizzbuzz_value(None)

"""
Todo:
    - get_fizzbuzz_value(value: int) -> str
        - it returns string version of integer when not divisible by 3 or 5 - x
        - it returns "Fizz" for multiples of 3 - x
        - it returns 'Buzz' for mults of 5 - x
        - it should raise a TypeError when not given a valid input type - x
        - it returns 'FizzBuzz' for multiples of 3 and 5 - x
"""
