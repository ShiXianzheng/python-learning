"""
author: xzshi19
date: 2019.08.28
Aim: learn python's built-in functions
"""

# abs(x) --return the absolute value of a number; a complex number --> it's magnitude

# all(iterable) --return true if all elements of the iterable are true(or empty)
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# any(iterable) --return true if any element of the iterable is true(empty --> false)
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# ascii(object) --return a string containing a printable representation of an object

# bin(x) --convert an integer number to a binary string prefixed with '0b'

# class bool([x]) --return a boolean value

# breakpoint(*args, **kws) --drop you into the debugger at the call site(sys.breakpointhook(), ignore args and kws)

# class bytearray([source[, encoding[, errors]]]) --return a new array of bytes

# class bytes([source[, encoding[, errors]]]) --return a new 'bytes' object(an immutable sequence)

# callable(object) --return true if the object argument appears callable; Note that classes are callable
# (calling a class returns a new instance); instances are callable if their class has a __call__() method.

# chr(i) --return the string representing a character

# @classmethod --transform a method into a class method
# A class method receives the class as implicit first argument, just like an instance method receives the instance.
# To declare a class method, use this idiom:
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...

# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) --compile the source into a code or AST object

# class complex([real[, imag]]) --return a complex number with the value real+ imag*1j or
# convert a string or number to a complex number
# When converting from a string, the string must not contain whitespace around the central + or - operator.
# For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.

# delattr(object, name) --delete the named attribute(--> del object.name)

# class dice(**kwarg) --create a new dictionary

# dir([object]) --Without arguments, return the list of names in the current local scope.
# With an argument, attempt to return a list of valid attributes for that object
"""
>>> import struct
>>> dir()   # show the names in the module namespace  # doctest: +SKIP
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module # doctest: +SKIP
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']
"""

# divmod(a, b) --Take two (non complex) numbers as arguments and
# return a pair of numbers consisting of their quotient and remainder when using integer division.
# With mixed operand types, the rules for binary arithmetic operators apply.
# For integers, the result is the same as (a // b, a % b).
# For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that.
# In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

# enumerate(iterable, start=0) --return a enumerate object(start, value)...
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

# eval(expression, globals=None, locals=None) --The expression argument is parsed and evaluated as a Python expression
# (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace.

# exec(object[, globals[, locals]]) -- supports dynamic execution of Python code

# filter(function, iterable) --(item for item in iterable if function(item))

# class float([x]) --return a floating point number constructed from a number of string x
# sign           ::=  "+" | "-"
# infinity       ::=  "Infinity" | "inf"
# nan            ::=  "nan"
# numeric_value  ::=  floatnumber | infinity | nan
# numeric_string ::=  [sign] numeric_value
"""
>>> float('+1.23')
1.23
>>> float('   -12345\n')
-12345.0
>>> float('1e-003')
0.001
>>> float('+1E6')
1000000.0
>>> float('-Infinity')
-inf
"""

# format(value[, format_spec]) --Convert a value to a “formatted” representation, as controlled by format_spec

# class frozenset([iterable]) --return a new frozenset object, elements taken from iterable.

# getattr(object, name[, default]) --return the value of the named attribute of object(--> object.name)

# globals() --return a dictionary representing the current global symbol table

# hasattr(object, name) --the result is true if the string is the name of one of the object's attributes

# hash(object) --return the hash value of the object.hash values are integers.

# help([object])

# hex(x) --convert an integer number to a lowercase hexadecimal string prefixed with '0x'
"""
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
"""

# id(object) --return the 'identity' of an object

# input([prompt]) --If the prompt argument is present, it is written to standard output without a trailing newline.
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# When EOF is read, EOFError is raised
"""
>>> s = input('--> ')  
--> Monty Python's Flying Circus
>>> s  
"Monty Python's Flying Circus"
"""

# class int([x]) --Return an integer object constructed from a number or string x, or return 0 if no arguments are given

# isinstance(object, classinfo) --Return true if the object argument is an instance of the classinfo argument,
# or of a (direct, indirect or virtual) subclass thereof

# issubclass(class, classinfo) --Return true if class is a subclass (direct, indirect or virtual) of classinfo.

# iter(object[, sentinel]) --return an iterator object
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)

# len(s) --return the length (the number of items) of an object.

# class list([iterable])

# locals() --update and return a dictionary representing the current local symbol table

# map(function, iterable, ...) --return an iterator that applies function to every item of iterable, yielding the results

# max(iterable, *[, key, default]) max(arg1, arg2, *arg[, key]) --Return the largest item in an iterable or the largest of two or more arguments.

# memoryview(obj) --Return a “memory view” object created from the given argument

# min(iterable, *[, key, default])

# next(iterator[, default]) --Retrieve the next item from the iterator by calling its __next__() method

# class object --Return a new featureless object
# object does not have a __dict__, so you can’t assign arbitrary attributes to an instance of the object class.

# oct(x) --convert an integer number to an octal string prefixed with '0o'

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closed=True, opener=None)
# Open file and return a corresponding file object
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)
"""
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor
"""

# ord(c) --Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
# inverse of chr()

# pow(x, y[, z]) --return x to the power of y, modulo z(pow(x, y) % z)

# print(*object, sep='', end='\n', file=sys.stdout, flush=False) --Print objects to the text stream file

# class property(fget=None, fset=None, fdel=None, doc=None) --return a property attribute
"""
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")



    class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        "Get the current voltage."
        return self._voltage
        
        
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        "I'm the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
"""

# range(start, stop[, step]) --an immutable sequence type

# repr(object) --Return a string containing a printable representation of an object

# reversed(seq) --return a reverse iterator

# round(number[, ndigits]) --Return number rounded to ndigits precision after the decimal point

# class set([iterable]) --return a new set object, optionally with elements taken from iterable.

# setattr(object, name, value) --setattr(x, 'foobar', 123) is equivalent to x.foobar = 123

# class slice(start, stop[, step]) --Return a slice object representing the set of indices specified by range(start, stop, step)

# sorted(iterable, *, key=None, reverse=False) --Return a new sorted list from the items in iterable.

# staticmethod --Transform a method into a static method.
"""
A static method does not receive an implicit first argument.
class C:
    @staticmethod
    def f(arg1, arg2, ...): ...


class C:
    builtin_open = staticmethod(open)
"""

# class str(object=b'', encoding='utf-8', errors='strict') --Return a str version of object

# sum(iterable[, start]) --Sums start and the items of an iterable from left to right and returns the total

# super([type[, object-or-type]]) --Return a proxy object that delegates method calls to a parent or sibling class of type

# tuple([iterable]) -- tuple is actually an immutable sequence type

# class type(object) type(name, bases, dict) -- return the type of an object

# vars([object]) --Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

# zip(*iterables) --Make an iterator that aggregates elements from each of the iterables.
"""
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

zip() in conjunction with the * operator can be used to unzip a list:
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True
"""

# __import__(name, globals=None, locals=None, fromlist=(), level=0)



