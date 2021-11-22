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
    from writers.console_writer import ConsoleWriter
    from writers.file_writer import FileWriter

    # writer = FileWriter('fizzbuzz_results')
    writer = ConsoleWriter()

    FizzBuzz(
        writer=writer
    ).run(
        start=1,
        length=100,
    )
