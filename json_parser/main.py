OPEN_BRACKET = "{"
CLOSED_BRACKET = "}"


def json_parser(f):
    with open(f, 'r') as f:
        read_file = f.read()
        if len(read_file) >= 2:
            if read_file[0] == OPEN_BRACKET and read_file[-1] == CLOSED_BRACKET:
                return True
        return False


print(json_parser('tests/step1/valid.json'))
print(json_parser('tests/step1/invalid.json'))
