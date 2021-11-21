def get_fizzbuzz_value(value: int) -> str:
    if type(value) is not int:
        raise TypeError('get_fizzbuzz_value did not receive integer input')

    if value % 5 == 0 and value % 3 == 0:
        return 'FizzBuzz'

    if value % 5 == 0:
        return 'Buzz'

    if value % 3 == 0:
        return 'Fizz'

    return f'{value}'
