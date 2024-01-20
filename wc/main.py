from sys import argv
from bytes_strategy import ByteCountStrategy
from chars_strategy import CharacterCountStrategy
from lines_strategy import LinesCountStrategy
from word_strategy import WordCountStrategy

# -c bytes
# -l lines
# -w words
# -m chars
# filename

if len(argv[1:]) == 2:
    f = open(argv[2], 'r')
    if argv[1] == '-c':
        print(ByteCountStrategy(file=f).count())
    elif argv[1] == '-l':
        print(LinesCountStrategy(file=f).count())
    elif argv[1] == '-w':
        print(WordCountStrategy(file=f).count())
    elif argv[1] == '-m':
        print(CharacterCountStrategy(file=f).count())

# return all counts
if len(argv[1:]) == 1:
    f = open(argv[1], 'r')
    print(ByteCountStrategy(file=f).count())
    print(WordCountStrategy(file=f).count())
    print(CharacterCountStrategy(file=f).count())
    print(LinesCountStrategy(file=f).count())
