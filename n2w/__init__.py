#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .n2w import N2w

app = N2w()


def convert(number):
    return app.convert(number)
