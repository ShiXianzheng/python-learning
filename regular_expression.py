"""
author: xzshi19
arms: learning character string and regular expression
date: 2019.09.01
"""

# regular expression syntax
# Regular expressions can be concatenated to form new regular expressions; if A and B are both regular expressions, then AB is also a regular expression

# special characters
# . matches any character except a newline
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the end of the string
# * match 0 or more repetitions of the preceding RE --ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s
# + match 1 or more repetitions of the preceding RE --ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
# ? match 0 or 1 repetitions of the preceding RE --ab? will match either ‘a’ or ‘ab’

# *?, +?, ?? --The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible.
# Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', it will match the entire string,
# and not just '<a>'. Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion;
# as few characters as possible will be matched. Using the RE <.*?> will match only '<a>'.

# {m} specifies that the exactly m copies of the previous RE should be matched;
# For example, a{6} will match exactly six 'a' characters, but not five.

# {m, n} match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible.
# For example, a{3,5} will match from 3 to 5 'a' characters

# {m, n}?  match from m to n repetitions of the preceding RE, attempting to match as few as repetitions as possible.
# For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? will only match 3 characters.

# \ Either escapes special characters (permitting you to match characters like '*', '?', and so forth),
# or signals a special sequence; special sequences are discussed below.
#  This is complicated and hard to understand, so it’s highly recommended that you use raw strings for all but the simplest expressions.

# [] used to indicate a set of characters.
# Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'
# Ranges of characters can be indicated by giving two characters and separating them by a '-',
# for example [a-z] will match any lowercase ASCII letter, [0-5][0-9] will match all the two-digits numbers from 00 to 59,
# and [0-9A-Fa-f] will match any hexadecimal digit.
# If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [-a] or [a-]), it will match a literal '-'.

# For example, [(+*)] will match any of the literal characters '(', '+', '*', or ')'.

# For example, [^5] will match any character except '5', and [^^] will match any character except '^'.
# ^ has no special meaning if it’s not the first character in the set.

# To match a literal ']' inside a set, precede it with a backslash, or place it at the beginning of the set.
# For example, both [()[\]{}] and []()[{}] will both match a parenthesis.

# | match either of it. In other words, the '|' operator is never greedy. To match a literal '|', use \|, or enclose it inside a character class, as in [|].

# (...) Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group;

# (?...)

# (?aiLmsux) --(One or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x'.) The group matches the empty string;
# the letters set the corresponding flags: re.A (ASCII-only matching), re.I (ignore case), re.L (locale dependent),
# re.M (multi-line), re.S (dot matches all), re.U (Unicode matching), and re.X (verbose), for the entire regular expression.
# (The flags are described in Module Contents.) This is useful if you wish to include the flags as part of the regular expression,
# instead of passing a flag argument to the re.compile() function. Flags should be used first in the expression string.

# (?:...)
# (?aiLmsux-imsx:...)
# (?P<name>...)
# (?P=name)
# (?#...)
# (?=...)
# (?<=...)
# (?<!...)

# \number --Matches the contents of the group of the same number.
# \A --Matches only at the start of the string.
# \b --Matches the empty string, but only at the beginning or end of a word
# \B --Matches the empty string, but only when it is not at the beginning or end of a word.
# \d --For Unicode (str) patterns:
# Matches any Unicode decimal digit (that is, any character in Unicode character category [Nd]).
# This includes [0-9], and also many other digit characters. If the ASCII flag is used only [0-9] is matched.
# For 8-bit (bytes) patterns:
# Matches any decimal digit; this is equivalent to [0-9].
# \D --Matches any character which is not a decimal digit
# \s --For Unicode (str) patterns:
# Matches Unicode whitespace characters (which includes [ \t\n\r\f\v], and also many other characters,
# for example the non-breaking spaces mandated by typography rules in many languages). If the ASCII flag is used, only [ \t\n\r\f\v] is matched.
# For 8-bit (bytes) patterns:
# Matches characters considered whitespace in the ASCII character set; this is equivalent to [ \t\n\r\f\v].
# \S --Matches any character which is not a whitespace character
# \w --For Unicode (str) patterns:
# Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore. If the ASCII flag is used, only [a-zA-Z0-9_] is matched.
# For 8-bit (bytes) patterns:
# Matches characters considered alphanumeric in the ASCII character set; this is equivalent to [a-zA-Z0-9_].
# If the LOCALE flag is used, matches characters considered alphanumeric in the current locale and the underscore.
# \W --Matches any character which is not a word character.
# \Z --Matches only at the end of the string.

# module contents
# re.compile(pattern, flags=0) --Compile a regular expression pattern into a regular expression object,
# which can be used for matching using its match(), search() and other methods,
# re.A/re.ASCII
# re.DEBUG
# re.I/re.IGNORECASE
# re.I/re.LOCALE
# re.M/re.MULTILINE
# re.S/re.DOTALL
# re.X/re.VERBOSE
# re.search(pattern, string, flags=0)
# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)
# re.finditer(pattern, string, flags=0)
# re.sub(pattern, repl, string, count=0, flags=0)
# re.subn(pattern, repl, string, count=0, flags=0)
# re.escape(pattern)
# re.purge()
# exception re.error(msg, pattern=None, pos=None)

# regular expression objects
...

# match objects
...

# regular expression examples
# def displaymatch(match):
#     if match is None:
#         return None
#     return '<Match: %r, groups=%r>' % (match.group(), match.groups())

# >>> valid = re.compile(r"^[a2-9tjqk]{5}$")
# >>> displaymatch(valid.match("akt5q"))  # Valid.
# "<Match: 'akt5q', groups=()>"
# >>> displaymatch(valid.match("akt5e"))  # Invalid.
# >>> displaymatch(valid.match("akt"))    # Invalid.
# >>> displaymatch(valid.match("727ak"))  # Valid.
# "<Match: '727ak', groups=()>"

# >>> pair = re.compile(r".*(.).*\1")
# >>> displaymatch(pair.match("717ak"))     # Pair of 7s.
# "<Match: '717', groups=('7',)>"
# >>> displaymatch(pair.match("718ak"))     # No pairs.
# >>> displaymatch(pair.match("354aa"))     # Pair of aces.
# "<Match: '354aa', groups=('a',)>"# >>> pair.match("717ak").group(1)
# '7'
#
# # Error because re.match() returns None, which doesn't have a group() method:
# >>> pair.match("718ak").group(1)
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     re.match(r".*(.).*\1", "718ak").group(1)
# AttributeError: 'NoneType' object has no attribute 'group'
#
# >>> pair.match("354aa").group(1)
# 'a'

# simulating scanf()
...

# making a phonebook
...

