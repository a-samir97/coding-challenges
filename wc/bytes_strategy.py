from wc_interface import WCCommandStrategy


class ByteCountStrategy(WCCommandStrategy):
    def __init__(self, file):
        self.file = file

    def count(self) -> int:
        self.file.seek(0, 2)
        return self.file.tell()
