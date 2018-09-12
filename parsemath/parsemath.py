"""
parsemath
=========

[![Build Status](https://travis-ci.org/jncraton/parsemath.svg?branch=master)](https://travis-ci.org/jncraton/parsemath)

Parses a mathematical expression and returns a Python object

Eventually, this should use a proper parser, but for now it is just a series of hacks that convert formal mathematical notation into Python code and then evaluate it.

Example usage:

```
>>> parsemath("[1,2,...,5]")
range(1, 6)
>>> parsemath("[0,2,...,6]")
range(0, 7, 2)
>>> parsemath("Σ[0,2,...,6]")
12
>>> parsemath("Σ[0,2,...,4²]")
72

```
"""

import re

def parsemath(expr):
  expr = replace_pow(expr)

  for m in re.finditer("\[(.*?),(.*?),...,(.*?)\]", expr):
    new_range = "range(%d,%d,%d)" % (eval(m.group(1)), eval(m.group(3)) + 1, eval(m.group(2)) - eval(m.group(1)))
    expr = expr.replace(m.group(0), new_range)

  expr += ")" * expr.count("Σ")
  expr = expr.replace("Σ", "sum(")
  
  return eval(expr)

def replace_pow(expr):
  """
  >>> replace_pow("4²")
  '4**2'
  """

  replacements = [
    ("²","**2"),
  ]

  for r in replacements:
    expr = expr.replace(r[0], r[1])

  return expr
    