import unittest
import re
from easy_pattern import *


class PatternTest(unittest.TestCase):

    def test_digit(self):
        pattern = Pattern()
        pattern.starts_with(DIGIT)
        p = re.compile(pattern.pattern)
        self.assertEqual(p.findall('1'), ['1'])

    def test_non_digit(self):
        regex = Pattern()
        regex.starts_with(NON_DIGIT)
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('a'), ['a'])

    def test_alpha(self):
        regex = Pattern()
        regex.starts_with(ALPHA)
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('a'), ['a'])

    def test_alphanum(self):
        regex = Pattern()
        regex.starts_with(ALPHANUM)
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('a'), ['a'])

    def test_zero_or_more_digits(self):
        regex = Pattern()
        regex.starts_with(zero_or_more(DIGIT))
        print(regex)
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('12345'), ['12345', ''])

    def test_at_least_three_digits(self):
        regex = Pattern()
        regex.starts_with(at_least(3, DIGIT))
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('12345'), ['12345'])

    def test_between_three_and_five_digits(self):
        regex = Pattern()
        regex.starts_with(between(3, 5, DIGIT))
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('12345'), ['12345'])

    def test_digit_followed_by_non_digit(self):
        regex = Pattern()
        regex.starts_with(DIGIT).followed_by(one_or_more(NON_DIGIT))
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('1a'), ['1a'])

    def test_digit_not_followed_by(self):
        regex = Pattern()
        regex.starts_with(DIGIT).not_followed_by(DIGIT)
        p = re.compile(regex.pattern)
        self.assertEqual(p.findall('1a'), ['1a'])


