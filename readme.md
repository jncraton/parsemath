
parsemath
=========

Parses a mathematical expression and returns a Python object

Eventually, this should use a proper parser, but for now it is just a series of hacks that convert formal mathematical notation into Python code and then evaluate it.

Example usage:

>>> parsemath("[1,2,...,5]")
range(1, 6)
>>> parsemath("[0,2,...,6]")
range(0, 7, 2)
>>> parsemath("Σ[0,2,...,6]")
12

