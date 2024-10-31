# variables and data types in python
# Variables are used to store values in memory and give them a name so that they can be accessed later in the program. 
# Variables are created when they are first assigned a value. 
# Variables are assigned values using the assignment operator (=). 
# Variables are case sensitive.  Example: x = 5, X = 10 
# Variables can be assigned different data types.  Example: x = 5, y = 'Hello'
# Variables can be reassigned to different data types.  Example: x = 5, x = 'Hello'
# data types in python are: int, float, string, boolean, list, tuple, dictionary, set, None and complex. 

# int: integer, whole number, positive or negative, without decimals, unlimited length. Example: 5, -3, 0
# float: floating point number, positive or negative, with decimals, unlimited length. Example: 3.14, -0.001
# string: sequence of characters, enclosed in single or double quotes, immutable. Example: 'Hello', "World" 
# boolean: True or False, used for conditional statements. Example: x = True, y = False 
# list: ordered collection of items, mutable, enclosed in square brackets. Example: [1, 2, 3] , [1, 2, 3, 3] = [1, 2, 3, 3] 
# tuple: ordered collection of items, immutable, enclosed in parentheses. Example: (1, 2, 3) , (1, 2, 3, 3) = (1, 2, 3, 3) 
# dictionary: unordered collection of items, mutable, key-value pairs, enclosed in curly braces. Example: {'name': 'John', 'age': 25} ,      {'name': 'John', 'age': 25} = {'name': 'John', 'age': 30}
# set: unordered collection of unique items, mutable, enclosed in curly braces. Example: {1, 2, 3}   , {1, 2, 3, 3} = {1, 2, 3} 
# None: null value, represents absence of value. Example: x = None 
# complex: real and imaginary part, enclosed in parentheses. Example: 5 + 3j 
# type() function is used to check the data type of a variable.
# type conversion is the process of converting one data type to another. 
# type casting is the process of converting one data type to another. Example: int(), float(), str(), bool(), list(), tuple(), dict(), set(), complex().
# type coercion is the process of converting one data type to another.  Example: int + float = float
# type inference is the process of automatically determining the data type of a variable.  Example: x = 5 # x is an integer 
# type checking is the process of verifying the data type of a variable. Example: isinstance(x, int)
# type hinting is the process of specifying the data type of a variable. Example: x: int = 5  
# type annotations are used to specify the data type of a variable.  Example: x: int = 5

#  Strings in Python 
# Strings are used to store text data in python. 
# Strings are immutable, which means they cannot be changed after they are created.
# Strings are enclosed in single or double quotes. Example: 'Hello', "World" 
# Strings can be concatenated using the + operator. Example: 'Hello' + 'World' = 'HelloWorld'
# Strings can be repeated using the * operator. Example: 'Hello' * 3 = 'HelloHelloHello'
# Strings can be indexed using square brackets. Example: 'Hello'[0] = 'H'
# Strings can be sliced using square brackets. Example: 'Hello'[0:3] = 'Hel'
# Strings can be formatted using the format() method. Example: 'Hello, {}!'.format('World') = 'Hello, World!'
# Strings can be formatted using f-strings. Example: name = 'World', f'Hello, {name}!' = 'Hello, World!'

#  Lists in Python
# Lists are used to store multiple items in a single variable.
# Lists are ordered, mutable, and can contain items of different data types.
# Lists are enclosed in square brackets. Example: [1, 2, 3]
# Lists can be indexed using square brackets. Example: [1, 2, 3][0] = 1
# Lists can be sliced using square brackets. Example: [1, 2, 3][0:2] = [1, 2]
# Lists can be nested inside other lists. Example: [[1, 2], [3, 4]]
# Lists can be concatenated using the + operator. Example: [1, 2] + [3, 4] = [1, 2, 3, 4]
# Lists can be repeated using the * operator. Example: [1, 2] * 3 = [1, 2, 1, 2, 1, 2]
# Lists can be modified using various methods like append(), insert(), remove(), pop(), clear(), sort(), reverse().
# Lists can be sorted using the sort() method. Example: [3, 1, 2].sort() = [1, 2, 3]
# Lists can be reversed using the reverse() method. Example: [1, 2, 3].reverse() = [3, 2, 1]

#  Tuples in Python
# Tuples are used to store multiple items in a single variable.
# Tuples are ordered, immutable, and can contain items of different data types.
# Tuples are enclosed in parentheses. Example: (1, 2, 3)
# Tuples can be indexed using square brackets. Example: (1, 2, 3)[0] = 1
# Tuples can be sliced using square brackets. Example: (1, 2, 3)[0:2] = (1, 2)
# Tuples can be nested inside other tuples. Example: ((1, 2), (3, 4))
# Tuples can be concatenated using the + operator. Example: (1, 2) + (3, 4) = (1, 2, 3, 4)
# Tuples can be repeated using the * operator. Example: (1, 2) * 3 = (1, 2, 1, 2, 1, 2)

#  Dictionaries in Python
# Dictionaries are used to store key-value pairs in python.
# Dictionaries are unordered, mutable, and can contain items of different data types.
# Dictionaries are enclosed in curly braces. Example: {'name': 'John', 'age': 25}
# Dictionaries can be accessed using keys. Example: {'name': 'John', 'age': 25}['name'] = 'John'
# Dictionaries can be modified using various methods like update(), pop(), clear().
# Dictionaries can be sorted using the sorted() function. Example: sorted({'b': 2, 'a': 1}) = [('a', 1), ('b', 2)]

#  Sets in Python
# Sets are used to store unique items in python.
# Sets are unordered, mutable, and can contain items of different data types.
# Sets are enclosed in curly braces. Example: {1, 2, 3}
# Sets can be modified using various methods like add(), remove(), pop(), clear().
# Sets can be used to perform set operations like union, intersection, difference, symmetric difference.
# Sets can be sorted using the sorted() function. Example: sorted({3, 1, 2}) = [1, 2, 3]

#  None in Python
# None is used to represent the absence of a value in python.
# None is a null value and does not have any data type.
# None is used as a default return value for functions that do not return anything.

#  Complex Numbers in Python
# Complex numbers are used to represent numbers in the form a + bj, where a is the real part and b is the imaginary part.
# Complex numbers are enclosed in parentheses. Example: 5 + 3j
# Complex numbers can be added, subtracted, multiplied, divided, and compared.

#  Boolean in Python
# Boolean values are used to represent truth values in python.
# Boolean values can be True or False.
# Boolean values are used for conditional statements and comparisons.
# Boolean values can be combined using logical operators like and, or, not.

#  Type Conversion in Python
# Type conversion is the process of converting one data type to another.
# Type conversion can be done using built-in functions like int(), float(), str(), bool().
# Type conversion can be done implicitly or explicitly.
# Implicit type conversion is done automatically by the interpreter.
# Explicit type conversion is done manually by the programmer.

#  Type Coercion in Python
# Type coercion is the process of converting one data type to another.
# Type coercion can be done implicitly or explicitly.
# Implicit type coercion is done automatically by the interpreter.
# Explicit type coercion is done manually by the programmer.

#  Type Inference in Python
# Type inference is the process of automatically determining the data type of a variable.
# Type inference is done by the interpreter based on the value assigned to the variable.
# Type inference helps in reducing the amount of code needed to specify data types.
# Type inference is used in dynamically typed languages like python.

#  Type Checking in Python
# Type checking is the process of verifying the data type of a variable.
# Type checking can be done using the isinstance() function.
# Type checking helps in ensuring that the correct data type is used in the program.
# Type checking is used in statically typed languages like python.
# Example: isinstance(x, int) # check if x is an integer  

#  Type Hinting in Python
# Type hinting is the process of specifying the data type of a variable.
# Type hinting is done by adding type annotations to variables.
# Type hinting helps in improving code readability and maintainability.
# Type hinting is used in statically typed languages like python. 
# Example: x: int = 5  # x is an integer  

#  Type Annotations in Python
# Type annotations are used to specify the data type of a variable.
# Type annotations are added to variables using colons.
# Type annotations help in improving code readability and maintainability.
# Type annotations are used in statically typed languages like python.
# Example: x: int = 5  # x is an integer    , y: str = 'Hello'  # y is a string


  

# local variables are variables that are defined inside a function and can only be accessed within that function.
# global variables are variables that are defined outside a function and can be accessed anywhere in the program.
# global keyword is used to access global variables inside a function.
# nonlocal keyword is used to access variables from the outer scope inside a nested function.
# scope is the visibility of variables in a program.
# scope resolution is the process of determining the value of a variable based on its scope.
# scope rules in python are: local scope, enclosing scope, global scope, built-in scope.
# local scope is the innermost scope and contains variables defined inside a function.
# enclosing scope is the scope that contains the local scope and any enclosing scopes.
# global scope is the scope that contains variables defined outside a function.
# built-in scope is the scope that contains built-in functions and modules.
# LEGB rule is used to determine the order in which python searches for variables in different scopes.
# LEGB stands for local, enclosing, global, built-in.
# nested functions are functions defined inside another function.
# nested functions can access variables from the outer scope using the nonlocal keyword.
# nested functions can be used to encapsulate code and reduce redundancy.
# Example: def outer(): def inner(): nonlocal x x = 10



# recursion is the process of a function calling itself.  Example: def factorial(n): if n == 0: return 1 else: return n * factorial(n - 1)  
# recursion is used to solve problems that can be broken down into smaller subproblems. 
# recursion has two main components: base case and recursive case.
# base case is the condition that stops the recursion.
# recursive case is the condition that calls the function recursively. 
# recursion can be used to solve problems like factorial, fibonacci sequence, binary search, tree traversal. 
# recursion can be less efficient than iteration due to the overhead of function calls. 
# recursion can lead to stack overflow if the recursion depth is too large.
# tail recursion is a special form of recursion where the recursive call is the last statement in the function.
# tail recursion can be optimized by the compiler to avoid stack overflow.
# tail recursion can be converted to iteration using a technique called tail call optimization. 
# Example: def factorial(n, result=1): if n == 0: return result else: return factorial(n - 1, result * n) 
# Example: def factorial(n): result = 1 for i in range(1, n + 1): result *= i return result 
# Example: def factorial(n, result=1): while n > 0: result *= n n -= 1 return result 
# Example: def factorial(n): return 1 if n == 0 else n * factorial(n - 1)

# iteration is the process of repeating a set of instructions a specified number of times or until a condition is met.
# iteration can be done using loops like for loop and while loop. 
# for loop is used to iterate over a sequence of items like lists, tuples, dictionaries, strings.  
# for loop uses the range() function to generate a sequence of numbers.
# for loop uses the in keyword to iterate over items in a sequence.
# for loop can be used to iterate over items in a list, tuple, dictionary, string.
# for loop can be used to iterate over items in a range of numbers.
# while loop is used to repeat a set of instructions until a condition is met.
# while loop uses the while keyword followed by a condition.
# while loop continues to execute as long as the condition is true.
# while loop can be used to repeat a set of instructions until a certain condition is met.
# while loop can be used to implement infinite loops.
# break statement is used to exit a loop prematurely.
# break statement is used to exit the innermost loop.
# break statement can be used in for loop and while loop.
# continue statement is used to skip the current iteration of a loop.
# continue statement is used to skip the remaining code in the loop and move to the next iteration.
# continue statement can be used in for loop and while loop.
# pass statement is used as a placeholder when no action is required.
# pass statement is used to avoid syntax errors when no code is needed.
# pass statement can be used in if statements, loops, functions, classes. 
# Example: for i in range(5): if i == 3: break print(i)
# Example: for i in range(5): if i == 3: continue print(i)
# Example: for i in range(5): pass 
# Example: while True: pass 
# Example: def func(): pass
# Example: class MyClass: pass
# Example: if x < 0: pass else: print(x) 

#  Functions in Python
# Functions are blocks of code that perform a specific task.
# Functions are defined using the def keyword followed by the function name and parameters.
# Functions can have zero or more parameters.
# Functions can have a return statement to return a value.
# Functions can have default parameters with default values.
# Functions can have keyword arguments with explicit parameter names.
# Functions can be called with positional arguments or keyword arguments.
# Functions can be called recursively to solve problems.
# Functions can be passed as arguments to other functions.
# Functions can be defined inside other functions. 
# Functions can have docstrings to provide documentation.
# Functions can have annotations to specify parameter and return types.
# Functions can have variable-length arguments using *args and **kwargs.
# Functions can have lambda expressions for anonymous functions.
# Functions can have closures to capture and remember the enclosing scope. 
# Example: def add(x, y): return x + y 
# Example: def greet(name='World'): return f'Hello, {name}!' 
# Example: def multiply(x, y=2): return x * y 
# Example: def divide(x, y): return x / y
# Example: def add(x, y): return x + y


# Lambda Functions in Python
# Lambda functions are anonymous functions that can have any number of arguments but only one expression.
# Lambda functions are defined using the lambda keyword followed by the arguments and expression.
# Lambda functions are used to create small, one-line functions without a name.
# Lambda functions can be used as arguments to higher-order functions like map(), filter(), reduce().
# Lambda functions can be used to create simple functions on the fly.
# Lambda functions can be used to create functions that are not needed elsewhere.
# Example: add = lambda x, y: x + y
# Example: multiply = lambda x, y=2: x * y
# Example: divide = lambda x, y: x / y
# Example: greet = lambda name='World': f'Hello, {name}!'
# Example: lambda x: x ** 2

#  Higher-Order Functions in Python
# Higher-order functions are functions that take other functions as arguments or return functions as results.
# Higher-order functions are used to create abstractions and compose functions.
# Higher-order functions are used to create more flexible and reusable code.
# Higher-order functions can be used to implement function decorators.
# Higher-order functions can be used to implement function currying.
# Higher-order functions can be used to implement function composition.
# Higher-order functions can be used to implement function chaining.
# Higher-order functions can be used to implement function memoization.




#  Classes in Python  (OOP - Object Oriented Programming) 
# Classes are used to create objects in python.
# Classes are defined using the class keyword followed by the class name.
# Classes can have attributes to store data.
# Classes can have methods to perform actions.
# Classes can have a constructor method called __init__ to initialize objects.
# Classes can have instance methods, class methods, and static methods.
# Classes can have properties to access and set attributes.
# Classes can have inheritance to create subclasses.
# Classes can have magic methods to customize behavior. 
# Classes can have decorators to modify behavior.
# Classes can have slots to restrict attribute creation.
# Classes can have metaclasses to customize class creation.
# Classes can have descriptors to customize attribute access.
# Classes can have abstract methods to define interfaces.
# Classes can have mixins to provide additional functionality.
# Classes can have data classes to create data structures. 
# Example: class Person: def __init__(self, name): self.name = name
# Example: class Person: def __init__(self, name): self.name = name def greet(self): return f'Hello, {self.name}!'
# Example: class Person: def __init__(self, name): self.name = name @property def name(self): return self._name @name.setter def name(self, value): self._name = value
# Example: class Person: def __init__(self, name): self.name = name @classmethod def create(cls, name): return cls(name)
# Example: class Person: def __init__(self, name): self.name = name @staticmethod def greet(name): return f'Hello, {name}!'

# Inheritance in Python
# Inheritance is the process of creating a new class from an existing class.
# Inheritance allows the new class to inherit attributes and methods from the existing class.
# Inheritance is used to create a hierarchy of classes with shared functionality.
# Inheritance can be single inheritance, multiple inheritance, or multilevel inheritance.
# Inheritance can be used to reuse code and avoid redundancy.
# Inheritance can be used to create subclasses with specialized behavior.
# Inheritance can be used to override methods and attributes in the superclass.
# Inheritance can be used to call methods from the superclass using super().
# Inheritance can be used to check if an object is an instance of a class using isinstance().
# Inheritance can be used to check if a class is a subclass of another class using issubclass().
# Example: class Person: def __init__(self, name): self.name = name class Student(Person): def __init__(self, name, student_id): super().__init__(name) self.student_id = student_id
# Example: class Person: def greet(self): return 'Hello!' class Student(Person): def greet(self): return 'Hi!'
# Example: class Person: def greet(self): return 'Hello!' class Student(Person): def greet(self): return super().greet() + ' How are you?'
# Example: class Person: pass class Student(Person): pass isinstance(Student(), Person) # True
# Example: class Person: pass class Student(Person): pass issubclass(Student, Person) # True

#  Encapsulation in Python
# Encapsulation is the process of restricting access to the internal state of an object.
# Encapsulation is used to protect the data of an object from being modified directly.
# Encapsulation is achieved by using private attributes and methods. 
# Encapsulation is used to hide the implementation details of an object.
# Encapsulation is used to prevent external code from modifying the internal state of an object.
# Encapsulation is used to ensure that the object is in a valid state at all times.
# Encapsulation is used to improve code maintainability and reusability.
# Encapsulation is one of the four pillars of object-oriented programming.
# Example: class Person: def __init__(self, name): self.__name = name def get_name(self): return self.__name def set_name(self, name): self.__name = name 
# Example: class Person: def __init__(self, name): self._name = name def get_name(self): return self._name def set_name(self, name): self._name = name
# Example: class Person: def __init__(self, name): self.name = name @property def name(self): return self._name @name.setter def name(self, value): self._name = value


#  Polymorphism in Python
# Polymorphism is the process of using a single interface to represent different types of objects. 
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Polymorphism is achieved by using inheritance, method overriding, and method overloading.
# Polymorphism is used to create flexible and reusable code.
# Polymorphism is one of the four pillars of object-oriented programming. 
# Example: class Animal: def speak(self): pass class Dog(Animal): def speak(self): return 'Woof!' class Cat(Animal): def speak(self): return 'Meow!'
# Example: class Animal: def speak(self): pass class Dog(Animal): def speak(self): return 'Woof!' class Cat(Animal): def speak(self): return 'Meow!' def make_sound(animal): return animal.speak()

#  Abstraction in Python
# Abstraction is the process of hiding the implementation details of an object and showing only the essential features.
# Abstraction is used to simplify complex systems by focusing on the essential aspects.
# Abstraction is achieved by using abstract classes and interfaces.
# Abstraction is used to create a blueprint for objects without specifying the details.
# Abstraction is used to define a common interface for a group of related objects.
# Abstraction is used to reduce code duplication and improve code maintainability.
# Abstraction is one of the four pillars of object-oriented programming.
# Example: from abc import ABC, abstractmethod class Animal(ABC): @abstractmethod def speak(self): pass class Dog(Animal): def speak(self): return 'Woof!' class Cat(Animal): def speak(self): return 'Meow!'

#  Decorators in Python
# Decorators are functions that modify the behavior of other functions.
# Decorators are used to add functionality to existing functions without modifying their code.
# Decorators are used to wrap a function with additional functionality.
# Decorators are used to add logging, timing, caching, authentication, and other features to functions.
# Decorators are defined using the @ symbol followed by the decorator function name.
# Decorators can take arguments to customize their behavior.
# Decorators can be used to create class decorators, method decorators, and property decorators.
# Decorators can be used to create function decorators, generator decorators, and context manager decorators.
# Decorators can be used to create custom decorators for specific use cases.
# Example: def logger(func): def wrapper(*args, **kwargs): print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}') return func(*args, **kwargs) return wrapper @logger def add(x, y): return x + y

#  Generators in Python
# Generators are functions that return an iterator object.
# Generators are used to generate a sequence of values lazily.
# Generators are defined using the yield keyword instead of return.
# Generators can be used to create infinite sequences of values.
# Generators can be used to process large datasets efficiently.
# Generators can be used to create pipelines of data processing steps.
# Generators can be used to implement coroutines for asynchronous programming.
# Generators can be used to create custom iterators for specific use cases.
# Example: def count(n): for i in range(n): yield i for i in count(5): print(i)

#  Context Managers in Python
# Context managers are used to manage resources like files, sockets, and database connections.
# Context managers are defined using the with statement.
# Context managers are used to ensure that resources are properly cleaned up after use.
# Context managers are used to handle exceptions and errors in a controlled way.
# Context managers are implemented using the __enter__ and __exit__ methods.
# Context managers can be created using the contextlib module.
# Context managers can be used to create custom context managers for specific use cases.
# Example: with open('file.txt', 'r') as f: data = f.read() print(data)




#  Modules in Python
# Modules are files that contain python code.
# Modules can be imported using the import statement.
# Modules can be used to organize code and reuse functionality.
# Modules can be packages that contain multiple modules.
# Modules can be built-in modules that come with python.
# Modules can be third-party modules that are installed using pip.
# Modules can be used to create libraries and frameworks.
# Modules can be used to create standalone applications.
# Modules can be used to create scripts and utilities.
# Modules can be used to create plugins and extensions.
# Example: import math print(math.pi)
# Example: from math import pi print(pi)
# Example: import os print(os.getcwd())
# Example: import sys print(sys.argv)
# Example: import random print(random.randint(1, 10))
# Example: import requests response = requests.get('https://www.google.com') print(response.status_code)
# Example: import mymodule print(mymodule.add(1, 2)) 
# Example: from mymodule import add print(add(1, 2))
# Example: import mypackage.mymodule print(mypackage.mymodule.add(1, 2)) 

#  Packages in Python
# Packages are directories that contain modules.
# Packages can be created by adding an __init__.py file to the directory.
# Packages can be nested to create subpackages.
# Packages can be imported using the import statement.
# Packages can be used to organize code into logical units.
# Packages can be used to distribute code as libraries.
# Packages can be used to create reusable components.
# Packages can be used to create plugins and extensions.
# Example: import mypackage.mymodule print(mypackage.mymodule.add(1, 2))
# Example: from mypackage import mymodule print(mymodule.add(1, 2))


#  Errors in Python
# Errors are exceptions that occur during the execution of a program.
# Errors can be syntax errors, runtime errors, or logical errors.
# Errors can be handled using try-except blocks.
# Errors can be raised using the raise statement.
# Errors can be caught using the except clause.
# Errors can be re-raised using the raise statement.
# Errors can be suppressed using the pass statement.
# Errors can be logged using the logging module.
# Errors can be debugged using the pdb module.
# Errors can be handled using custom exception classes.
# Example: try: x = 1 / 0 except ZeroDivisionError as e: print('Error:', e)
# Example: try: raise ValueError('Invalid value') except ValueError as e: print('Error:', e)
# Example: try: x = 1 / 0 except ZeroDivisionError as e: pass
# Example: import logging logging.basicConfig(level=logging.DEBUG) try: x = 1 / 0 except ZeroDivisionError as e: logging.error('Error: %s', e)

#  Testing in Python
# Testing is the process of verifying that a program works as expected.
# Testing can be done manually or automatically using test frameworks.
# Testing can be done at different levels like unit testing, integration testing, system testing.
# Testing can be done using test cases that cover different scenarios.
# Testing can be done using assertions to check the correctness of the program.
# Testing can be done using test runners to automate the testing process.
# Testing can be done using mock objects to simulate dependencies.
# Testing can be done using code coverage tools to measure test coverage.
# Testing can be done using continuous integration tools to automate testing.
# Testing can be done using performance testing tools to measure performance.   
# Example: assert add(1, 2) == 3 
# Example: assert add(1, 2) == 3, 'Test failed'
# Example: pytest test_mymodule.py 
# Example: unittest discover 
# Example: coverage run test_mymodule.py
# Example: coverage report
# Example: tox
# Example: locust -f load_test.py
# Example: jenkins 




