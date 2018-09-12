import re

def parsemath(expr):
  """
  Parses a mathematical expression and returns a Python object

  Eventually, this should use a proper parser, but for now it is just a series of hacks that convert formal mathematical notation into Python code and then evaluate it.

  Example usage:

  >>> parsemath("[1,2,...,5]")
  range(1, 6)
  >>> parsemath("[0,2,...,6]")
  range(0, 7, 2)
  """

  for m in re.finditer("\[(\d+),(\d+),...,(\d+)\]", expr):
    new_range = "range(%d,%d,%d)" % (int(m.group(1)), int(m.group(3)) + 1, int(m.group(2)) - int(m.group(1)))
    expr = expr.replace(m.group(0), new_range)
  
  return eval(expr)