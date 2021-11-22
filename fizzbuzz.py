from get_fizzbuzz_value.get_fizzbuzz_value import get_fizzbuzz_value


class IWriter:
    def write(self, message: str) -> None:
        pass


class FizzBuzz:
    def __init__(
        self,
        *,
        writer: IWriter
    ) -> None:
        self.writer = writer

    def run(self, *, start: int, length: int):
        for i in range(start, start + length):
            self.writer.write(get_fizzbuzz_value(i))


if __name__ == '__main__':
    import sys
    from writers.console_writer import ConsoleWriter
    from writers.file_writer import FileWriter

    args = sys.argv[1:]

    if args[0] == 'file':
        writer = FileWriter('fizzbuzz_results')
    else:
        writer = ConsoleWriter()

    start = int(args[1])
    length = int(args[2])

    FizzBuzz(
        writer=writer
    ).run(
        start=start,
        length=length,
    )
