"""
def exception(x,y):
    return x/y
exception(3,0) #Exception error scenario
"""


#Errors :
"""
A fundamental problem, often a syntax or logic mistake, that prevents the program from running or behaving as intended.
Typically detected during the parsing/compilation phase (e.g., SyntaxError) or due to severe system issues (e.g., OutOfMemoryError).
Generally not recoverable within the program's normal flow; requires code correction or system resource management.
Often due to programmer mistakes in code structure, syntax, or fundamental logic.
SyntaxError, IndentationError, SystemError (e.g., MemoryError).
Requires fixing the underlying code issue or addressing system-level problems.
"""


#Exception : the expected error scenario in python
"""
Error	Exception
	A fundamental problem, often a syntax or logic mistake, that prevents the program from running or behaving as intended.	An event that occurs during the execution of a program that disrupts the normal flow of instructions. It can be handled to prevent program termination.
	Typically detected during the parsing/compilation phase (e.g., SyntaxError) or due to severe system issues (e.g., OutOfMemoryError).	Occurs during runtime when unexpected conditions arise (e.g., ZeroDivisionError, FileNotFoundError, ValueError).
	Generally not recoverable within the program's normal flow; requires code correction or system resource management.	Can be caught and handled using try-except blocks, allowing the program to continue execution or gracefully exit.
	Often due to programmer mistakes in code structure, syntax, or fundamental logic.	Can be caused by external factors (e.g., missing files, network issues) or invalid data input, in addition to logical errors.
	SyntaxError, IndentationError, SystemError (e.g., MemoryError).	TypeError, NameError, ZeroDivisionError, FileNotFoundError, ValueError, IndexError.
	Requires fixing the underlying code issue or addressing system-level problems.	Handled using try, except, else, and finally blocks to manage the program's response to the event.
"""

#4 keywords to handle exceptions :
#try, except, finally, raise
#by using above keywords-we can mention the error reasons to load
#instead of sudden breaking of code/ crash of codes
#also to avoid the dumping of data

#scenario that tries exception - try
#to catch the scenario - except
#try-except is a combo
#in keyword " except" -> the storing of issue given by try , is saved

"""
def exception(x,y):
    try:
        if y == 0:
            raise ZeroDivisionError("division by zero not possible")
    except ZeroDivisionError as e:
        print(e)
    return x/y
exception(3,0)
exception(0,0)
"""


#keyword "finally" is used to saved even if exception comes/not comes
#the input of finally - always loads

"""
def exception(x,y):
    try:
        if y == 0:
            raise ZeroDivisionError("division by zero not possible")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally block executed")
    return x/y
exception(3,1)
exception(0,0)
"""

#else block
#if exception is not quoted - the input of else not always loads

def exception(x,y):
    try:
        if y == 0:
            raise ZeroDivisionError("division by zero not possible")
    except ZeroDivisionError as e:
        print(e)
    else:
        print("else block executed")
    finally:
        print("finally block executed")
    return x/y
exception(3,1)
print(exception(3,1))
exception(0,0)
