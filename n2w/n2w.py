#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .converter import Convert


class N2w(Convert):

    def __init__(self):
        super(N2w, self).__init__()

    def convert(self, number=0):
        if number == 0:
            return "zero"
        else:
            # check for invalid int
            try:
                int(number)
            except ValueError:
                return "Input not a valid number"

            # check if number bigger than quintillion
            if (len(str(number)) >= (len(self.greater_names) * 4) - 1):
                return "Number too big"

            number, prefix = int(number), ""
            if number < 0:
                prefix, number = "negative", -number

            result, pointer = "", 0
            while True:
                if int(number) % 1000 != 0:
                    result = "{} {} {}".format(self.less_than_athousand(
                        number % 1000), self.greater_names.get(pointer - 1), result)
                pointer += 1
                number /= 1000

                if int(number) < 1:
                    break
            return "{} {}".format(prefix, result).strip()
