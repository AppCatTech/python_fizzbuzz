import unittest
from fizzbuzz import FizzBuzz

from parameterized import parameterized

class FizzBuzzTests(unittest.TestCase):
    def setUp(self):
        self.writer = TestWriter()
        self.fizzbuzz = FizzBuzz(
            writer=self.writer,
        )

    @parameterized.expand([
        [1, 5, '1 2 Fizz 4 Buzz'],
        [6, 5, 'Fizz 7 8 Fizz Buzz'],
        [11, 6, '11 Fizz 13 14 FizzBuzz 16'],
    ])
    def test_it_writes_expected_messages(self, start, length, expected):
        self.fizzbuzz.run(
            start=start,
            length=length
        )

        self.assertMessagesWritten(expected)

    def assertMessagesWritten(self, expected: str):
        self.assertEqual(expected, ' '.join(self.writer.messages))


class TestWriter:
    def __init__(self):
        self.messages = []

    def write(self, message):
        self.messages.append(message)


