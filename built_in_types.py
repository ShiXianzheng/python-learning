""""
some useful methods
"""

# boolean operation
x or y
x and y
not x

# comparisons
is
is not

# numeric types
abs(x)
int()
float()
complex(re, im)
c.conjugate()
divmod(a, b)
pow(x, y)
x ** y

math.trunc()
round(x, n)
math.floor()
math.ceil()

# additional methods on integer types
int.bit_length()
def bit_length(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)

int.to_bytes(length, byteorder, *, signed=False)

classmethod int.from_bytes(bytes, byteorder, *, signed=False)

# additional methods on float
float.as_integer_ratio()

float.is_integer()

float.hex()

classmethod float.fromhex()

# iterator types
container.__iter__()
iterator.__iter__()
iterator.__next__()

# sequence types
list()
tuple()

# ranges types
range()

# text sequence type
str()

# str methods
str.capitalize()
str.casefold()
str.center(width)
str.count(sub)
str.encode(encoding='utf-8', errors='strict')
str.endswith()
str.expandtabs(tabsize=8)
str.find(sub)
str.format()
str.format_map()
str.index(sub)
str.alnum()
str.isalpha()
str.isascii()
str.isdecimal()
str.isdigit()
str.isindentifier()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()
str.join()
str.ljust(width)
str.lower()
str.lstrip([shar])
static str.maketrans(x)
str.partition(sep)
str.replace(old, new)
str.rfind(sub)
str.rindex()
str.rjust(width)
str.rpartition(sep)
str.rstrip([chars])
str.rsplit()
str.split()
str.splitlines()
str.startswith()
str.strip([char])
str.swapcase()
str.title()
"""
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
"""
str.translate(table)
str.upper()
str.zfill(width)


# printf-style string formatting

# binary sequence types

# printf-style bytes formatting

# memory views

# set types

# mapping types
class dict()

len(d)
d[key]
d[key] = value
del d[key]
key in dict
key not in dict
iter(d)
clear()
copy()
classmethod fromkeys(iterable[, value])
get(key[, default])
items()
keys()
pop(key[, default])
popitem()
setdefault(key[, default])
update([other])
values()


# dictionary view objects
len(dictview)
iter(dictview)
x in dictview


# context manager types


