import re
from easy_pattern import *


regex = RegEx()
regex.starts_with(zero_or_more(DIGIT)).followed_by(one_or_more(ALPHANUM)).followed_by(at_least(3, WHITESPACE))

print(regex)
p = re.compile(regex.regex)
print p.findall('12345abc   ')
assert p.findall('12345abc   ') == ['12345abc   ']

print('All tests passed')
