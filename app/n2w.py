#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .converter import Convert


class N2w(Convert):

    def __init__(self):
        super(N2w, self).__init__()

    def convert(self, input=0):
        if input == 0:
            return "zero"
        else:
            # check if number bigger than quintillion
            if (len(str(input)) > len(self.greater_names) * 1000):
                return "Number too big"

            input, prefix = int(input), ""
            if input < 0:
                prefix, input = "negative", -input

            result, pointer = "", 0
            while True:
                if int(input) % 1000 != 0:
                    result = "{} {} {}".format(self.less_than_athousand(
                        input % 1000), self.greater_names.get(pointer - 1), result)
                pointer += 1
                input /= 1000

                if int(input) < 1:
                    break
            return "{} {}".format(prefix, result).strip()
