from wc_interface import WCCommandStrategy


class LinesCountStrategy(WCCommandStrategy):

    def __init__(self, file):
        self.file = file

    def count(self) -> int:
        self.file.seek(0)
        return len(self.file.readlines())
