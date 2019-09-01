"""
author : xzshi19
aims: learning exceptions
date: 2019.08.31
"""

# raise new_exc from original_exc

# execption BaseException  --base class for all built-in exceptions
# args --the tuple of arguments given to the exception constructor
# with_traceback(tb) --This method sets tb as the new traceback for the exception and returns the exception object
try:
    ...
except SomeException:
    tb = sys.exc_info()[2]
    raise OtherException(...).with_traceback(tb)

# exception Exception --All built-in, non-system-exiting exceptions are derived from this class
# All user-defined exceptions should also be derived from this class.

# exception ArithmeticError --The base class for those built-in exceptions that are raised for various arithmetic errors:
# OverflowError, ZeroDivisionError, FloatingPointError.

# exception BufferError --Raised when a buffer related operation cannot be performed.

# exception LookupError --The base class for the exceptions that are raised when a key or index used on a mapping
# or sequence is invalid: IndexError, KeyError. This can be raised directly by codecs.lookup().

# concrete exceptions
# exception AssertionError --Raised when an assert statement fails.

# exception AttributeError --Raised when an attribute reference (see Attribute references) or assignment fails

# exception EOFError --Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
# (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)

# exception FloatingPointError

# exception GeneratorExit --Raised when a generator or coroutine is closed; see generator.close() and coroutine.close().
# It directly inherits from BaseException instead of Exception since it is technically not an error.

# exception ImportError --Raised when the import statement has troubles trying to load a module.

# exception ModuleNotFoundError --A subclass of ImportError which is raised by import when a module could not be located

# exception IndexError --Raised when a sequence subscript is out of range.

# exception KeyError --Raised when a mapping (dictionary) key is not found in the set of existing keys.

# exception KeyboardInterrupt --Raised when the user hits the interrupt key (normally Control-C or Delete).

# exception MemoryError --Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects)

# exception NameError --Raised when a local or global name is not found

# exception NotImplementedError --This exception is derived from RuntimeError
#  In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method,
#  or while the class is being developed to indicate that the real implementation still needs to be added.

# exception OSError

# exception OverflowError --Raised when the result of an arithmetic operation is too large to be represented

# exception RecursionError --This exception is derived from RuntimeError

# exception ReferenceError --This exception is raised when a weak reference proxy, created by the weakref.proxy() function,
# is used to access an attribute of the referent after it has been garbage collected.

# exception RuntimeError --Raised when an error is detected that doesn’t fall in any of the other categories

# exception StopIteration --Raised by built-in function next() and an iterator’s __next__() method to signal that there are no further items produced by the iterator.

# exception StopAsyncIteration

# exception SyntaxError

# exception IndentationError --Base class for syntax errors related to incorrect indentation

# exception TabError --Raised when indentation contains an inconsistent use of tabs and spaces

# exception SystemError --Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope

# exception SystemExit --This exception is raised by the sys.exit() function.

# exception TypeError --Raised when an operation or function is applied to an object of inappropriate type.

# exception UnboundLocalError --Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.

# exception UnicodeError --Raised when a Unicode-related encoding or decoding error occurs.

# exception UnicodeEncodeError

# exception UnicodeDecodeError

# exception UnicodeTranslateError

# exception ValueError --Raised when an operation or function receives an argument that has the right type but an inappropriate value,
# and the situation is not described by a more precise exception such as IndexError

# exception ZeroDivisionError --Raised when the second argument of a division or modulo operation is zero.

# OS Exception
# exception EnvironmentError
# exception IOError
# exception WindowsError

# exception BlockingIOError

# exception ChildProcessError

# exception ConnectionError

# exception BrokenPipeError

# exception ConnectionAbortedError

# exception ConnectionRefusedError

# exception ConnectionReseError

# exception FileExistsError

# exception FileNotFoundError

# exception InterruptedError

# exception NotADirectoryError

# exception IsADirectoryError

# exception PermissionError

# exception ProcessLookupError

# exception TimeoutError

# Warnings
# exception Warning
# exception UserWarning
# exception DeprecationWarning
# exception PendingDeprecationWarning
# exception SyntaxWarning
# exception RuntimeWarning
# exception FutureWarning
# exception ImportWarning
# exception BytesWarning
# exception ResourceWarning
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
