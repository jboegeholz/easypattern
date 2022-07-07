

ANY_CHAR = '.'
DIGIT = r'\d'
NON_DIGIT = r'\D'
WHITESPACE = r'\s'
NON_WHITESPACE = r'\S'
ALPHA = '[a-zA-Z]'
ALPHANUM = r'\w'
NON_ALPHANUM = r'\W'


def zero_or_more(string):
    return string + '*'


def zero_or_one(string):
    return string + '?'


def one_or_more(string):
    return string + '+'


def exactly(number, string):
    return string + '{' + str(number) + '}'


def at_least(number, string):
    return string + '{' + str(number) + ',}'


def between(start, end, string):
    return string + '{' + str(start) + ',' + str(end) + '}'


class Pattern:

    def __init__(self):
        self.pattern = ''

    def starts_with(self, start_str):
        self.pattern += start_str
        return self

    def followed_by(self, next_string):
        self.pattern += next_string
        return self

    def not_followed_by(self, next_string):
        self.pattern += "[^" + next_string + "]"

    def __str__(self):
        return self.pattern

    def __repr__(self):
        return self.pattern



