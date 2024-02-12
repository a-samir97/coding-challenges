OPEN_BRACKET = "{"
CLOSED_BRACKET = "}"
DOUBLE_QUOTES = "\""
COLON = ":"
COMMA = ","


def lexical_part(s: str) -> list:
    """
        Lexical part method is responsible for dividing a sequence of chars
        into meanging tokens
    """
    tokens = []
    if len(s) >= 2 and s[0] == OPEN_BRACKET and s[-1] == CLOSED_BRACKET:
        double_quotes_open = False
        temp_string = ""
        for i in range(1, len(s)):
            if s[i] == DOUBLE_QUOTES:
                double_quotes_open = not double_quotes_open
                if double_quotes_open is False:
                    tokens.append(temp_string)
                    temp_string = ""
                continue

            if double_quotes_open:
                temp_string += s[i]
                continue

            if s[i] == COLON:
                tokens.append(s[i])
                continue

            if s[i] == COMMA:
                tokens.append(s[i])
                continue
        return tokens
    return []


def json_parser(f):
    with open(f, 'r') as f:
        read_file = f.read()
        if len(read_file) >= 2:
            if read_file[0] == OPEN_BRACKET and read_file[-1] == CLOSED_BRACKET:
                return True
        return False
