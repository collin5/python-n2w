#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from n2w.n2w import N2w


class N2wTestCase(TestCase):

    def setUp(self):
        self.n2w = N2w()

    def test_convert_numbers_successfully(self):
        result = self.n2w.convert(123)
        self.assertEqual("one hundred twenty three", result.lower())

    def test_convert_numbers_less_than_ten_successfully(self):
        result = self.n2w.convert(2)
        self.assertEqual("two", result.lower())

    def test_convert_numbers_less_than_100_successfully(self):
        result = self.n2w.convert(49)
        self.assertEqual("forty nine", result.lower())

    def test_convert_hundreds_successfully(self):
        result = self.n2w.convert(134)
        self.assertEqual("one hundred thirty four", result.lower())

    def test_convert_thousands_successfully(self):
        result = self.n2w.convert(2222)
        self.assertEqual("two thousand two hundred twenty two", result.lower())

    def test_convert_millions_succussfully(self):
        result = self.n2w.convert(2000001)
        self.assertEqual("two million one", result.lower())

    def test_convert_billions_successfully(self):
        result = self.n2w.convert(1000000000)
        self.assertEqual("one billion", result.lower())

    def test_convert_quadrillions_successfully(self):
        result = self.n2w.convert(3000000000000)
        self.assertEqual("three quadrillion", result.lower())

    def test_convert_quintillions_successfully(self):
        result = self.n2w.convert(10000000000000000)
        self.assertEqual("ten quintillion", result.lower())

    def test_number_greatter_than_quintillion(self):
        result = self.n2w.convert(1000000000000000000)
        self.assertEqual("number too big", result.lower())

    def test_convert_invalid_value(self):
        result = self.n2w.convert("this should not work")
        self.assertTrue("not a valid number" in result.lower())

