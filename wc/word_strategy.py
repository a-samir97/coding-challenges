from wc_interface import WCCommandStrategy


class WordCountStrategy(WCCommandStrategy):

    def __init__(self, file):
        self.file = file

    def count(self) -> int:
        self.file.seek(0)
        words_count = 0
        for line in self.file:
            words_count += len(line.split())
        return words_count
