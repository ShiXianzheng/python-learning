"""
learning
"""

# string constants
# string.ascii_letters
# string.ascii_lowercase
# string.ascii_uppercase
# string.digits
# string.hexdigits
# string.octdigits
# string.punctuation
# string.printable
# string.whitespace


# custom string formatting
# class string.Formatter (following public methods)
# format(format_string, *args, **kwargs) --The primary API method.
# vformat(format_string, args, kwargs) --vformat() does the work of breaking up the format string into character data and replacement fields
# parse(format_string) --Loop over the format_string and return an iterable of tuples (literal_text, field_name, format_spec, conversion)
# get_field(field_name, args, kwargs) --Given field_name as returned by parse() (see above), convert it to an object to be formatted. Returns a tuple (obj, used_key).
# get_value(key, args, kwargs) --Retrieve a given field value.
# check_unused_args(used_args, args, kwargs) --Implement checking for unused arguments if desired
# format_field(value, format_spec) --The method is provided so that subclasses can override it.
# convert_field(value, conversion) --Converts the value (returned by get_field()) given a conversion type (as in the tuple returned by the parse() method)

# format string syntax
# replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
# field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
# arg_name          ::=  [identifier | digit+]
# attribute_name    ::=  identifier
# element_index     ::=  digit+ | index_string
# index_string      ::=  <any source character except "]"> +
# conversion        ::=  "r" | "s" | "a"
# format_spec       ::=  <described in the next section>

# "First, thou shalt count to {0}"  # References first positional argument
# "Bring me a {}"                   # Implicitly references the first positional argument
# "From {} to {}"                   # Same as "From {0} to {1}"
# "My quest is {name}"              # References keyword argument 'name'
# "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

# "Harold's a clever {0!s}"        # Calls str() on the argument first
# "Bring out the holy {name!r}"    # Calls repr() on the argument first
# "More {!a}"                      # Calls ascii() on the argument first

# format specification mini-language
# The general form of a standard format specifier is:
# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# '<'
# Forces the field to be left-aligned within the available space (this is the default for most objects).
# '>'
# Forces the field to be right-aligned within the available space (this is the default for numbers).
# '='
# Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types. It becomes the default when ‘0’ immediately precedes the field width.
# '^'
# Forces the field to be centered within the available space.

# '+'
#
# indicates that a sign should be used for both positive as well as negative numbers.
#
# '-'
#
# indicates that a sign should be used only for negative numbers (this is the default behavior).
#
# space
#
# indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.

# The '#' option causes the “alternate form” to be used for the conversion.

# The ',' option signals the use of a comma for a thousands separator. For a locale aware separator, use the 'n' integer presentation type instead.

# The '_' option signals the use of an underscore for a thousands separator for floating point presentation types and for integer presentation type 'd'

# When no explicit alignment is given, preceding the width field by a zero ('0') character enables sign-aware zero-padding for numeric types. This is equivalent to a fill character of '0' with an alignment type of '='.

# The precision is a decimal number indicating how many digits should be displayed after the decimal point for a floating point value formatted with 'f' and 'F', or before and after the decimal point for a floating point value formatted with 'g' or 'G'

# 's'
# String format. This is the default type for strings and may be omitted.
# None
# The same as 's'.

# 'b'
# Binary format. Outputs the number in base 2.
# 'c'
# Character. Converts the integer to the corresponding unicode character before printing.
# 'd'
# Decimal Integer. Outputs the number in base 10.
# 'o'
# Octal format. Outputs the number in base 8.
# 'x'
# Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9.
# 'X'
# Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9.
# 'n'
# Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.
# None
# The same as 'd'.

# 'e'
# Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. The default precision is 6.
# 'E'
# Exponent notation. Same as 'e' except it uses an upper case ‘E’ as the separator character.
# 'f'
# Fixed-point notation. Displays the number as a fixed-point number. The default precision is 6.
# 'F'
# Fixed-point notation. Same as 'f', but converts nan to NAN and inf to INF.
# 'g'
# General format. For a given precision p >= 1, this rounds the number to p significant digits and then formats the result in either fixed-point format or in scientific notation, depending on its magnitude.
# The precise rules are as follows: suppose that the result formatted with presentation type 'e' and precision p-1 would have exponent exp. Then if -4 <= exp < p, the number is formatted with presentation type 'f' and precision p-1-exp. Otherwise, the number is formatted with presentation type 'e' and precision p-1. In both cases insignificant trailing zeros are removed from the significand, and the decimal point is also removed if there are no remaining digits following it.
# Positive and negative infinity, positive and negative zero, and nans, are formatted as inf, -inf, 0, -0 and nan respectively, regardless of the precision.
# A precision of 0 is treated as equivalent to a precision of 1. The default precision is 6.
# 'G'
# General format. Same as 'g' except switches to 'E' if the number gets too large. The representations of infinity and NaN are uppercased, too.
# 'n'
# Number. This is the same as 'g', except that it uses the current locale setting to insert the appropriate number separator characters.
# '%'
# Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.
# None
# Similar to 'g', except that fixed-point notation, when used, has at least one digit past the decimal point. The default precision is as high as needed to represent the particular value. The overall effect is to match the output of str() as altered by the other format modifiers.

# : format_spec language
# ! format conversion field

>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
>>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'
>>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'

>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'

>>> c = 3-5j
>>> ('The complex number {0} is formed from the real part {0.real} '
...  'and the imaginary part {0.imag}.').format(c)
'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
>>> class Point:
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...     def __str__(self):
...         return 'Point({self.x}, {self.y})'.format(self=self)
...
>>> str(Point(4, 2))
'Point(4, 2)'

>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"

>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'

>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
'+3.140000; -3.140000'
>>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
>>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000'

>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

>>> '{:,}'.format(1234567890)
'1,234,567,890'

>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'

>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'

>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> int(_, 16)
3232235521
>>>
>>> width = 5
>>> for num in range(5,12):
...     for base in 'dXob':
...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011

# Template strings support $-based substitutions, using the following rules:
# $$ is an escape; it is replaced with a single $.
# $identifier names a substitution placeholder matching a mapping key of "identifier". By default, "identifier" is restricted to any case-insensitive ASCII alphanumeric string (including underscores) that starts with an underscore or ASCII letter. The first non-identifier character after the $ character terminates this placeholder specification.
# ${identifier} is equivalent to $identifier. It is required when valid identifier characters follow the placeholder but are not part of the placeholder, such as "${noun}ification".

# template strings
