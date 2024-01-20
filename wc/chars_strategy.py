from wc_interface import WCCommandStrategy


class CharacterCountStrategy(WCCommandStrategy):
    def __init__(self, file):
        self.file = file

    def count(self) -> int:
        self.file.seek(0)
        chars_count = 0
        for line in self.file:
            chars_count += len(line)
        return chars_count
