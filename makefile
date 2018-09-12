all: test readme.md

test:
	python3 -m doctest parsemath/parsemath.py

readme.md: parsemath/parsemath.py
	python3 -c "from parsemath import parsemath; print(parsemath.__doc__)" > readme.md