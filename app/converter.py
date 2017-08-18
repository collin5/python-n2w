#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta


class safelist(list):
    def get(self, index, default=""):
        try:
            return default if index < 0 else self.__getitem__(int(index))
        except IndexError:
            return default


class Convert():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.greater_names = safelist([
            "thousand", "million", "billion", "quadrillion", "quintillion"
        ])
        self.tens = safelist([
            "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
            "ninety"
        ])
        self.numbers = safelist([
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "forteen", "sixteen", "seventeen",
            "eighteen", "nineteen"
        ])

    def less_than_athousand(self, number):
        result = ""
        if number % 100 < 20:
            result = self.numbers.get((number % 100) - 1)
            number /= 100
        else:
            result = self.numbers.get((number % 10) - 1)
            number /= 10
            result = "{} {}".format(self.tens.get((number % 10) - 1), result)
            number /= 10
        return result if int(number) == 0 else "{} hundred {}".format(self.numbers.get(number - 1), result)
