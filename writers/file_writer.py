class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        open(self.filename, 'w').close()

    def write(self, message: str) -> None:
        with open(self.filename, 'a') as f:
            f.write(message + '\n')
