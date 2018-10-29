* no braces, indentation instead

* no explicit type declarations ( name = 'milos')

* **data types:** `Number, String, List, Tuple, Dictionary`

* **Numbers** build-in classes: int, float...

* **Strings**
  `name = "Milos"`

* **List**  
  like arrays in JS; ```array = ("Milos", 10, {})```
  
* **Tuple** - like list, but immutable

* **Dictionary**  
  similar to JS, like associative arrays.
  ```python
  dict = {}
  dict['one'] = 'two'
  dict[123] = 'milos'
  ```
  Dictionaries: Keys must be immutable. Which means you can use strings, numbers or tuples 
* Initializing variables:  
  `a = b = c = 1` (all three are initialized with 1)
  `a, b, c = 1, 2, "john"` (a = 1, b = 2, c = "john")

* else - can be used with loops :)

* **???** comma - print 'Current fruit :', fruit

* **Functions:**  
  **Arguments:** Required arguments, Keyword arguments (related when calling function - passing 
  arguments in different order than formal params) , Default arguments (at the end), Variable-length arguments 
  (def printinfo( arg1, *vartuple ) )
  
  `lambda [arg1 [,arg2,.....argn]]:expression` (only single expression, They cannot contain commands or multiple expressions. E.g. 
  can’t use print inside lambda expr)
  
  It is possible to define function inside function. Recursion is allowed.
  
  The globals() and locals() functions can be used to return the names in the global and local namespaces 
  depending on the location from where they are called.
  
* **pass** statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code 
will eventually go, but has not been written yet (e.g., in stubs for example)

* **list comprehension** Four parts: 1) output expression, 2) variable member, 3) input sequence, 4) predicate  
  Example:
  ```python
  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]  #squares of odd numbers
  ```

* **ternary operator** a if condition else b

* **classes**  
  Basic syntax:
  ```python
  class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
  ```
  **NOTE** What this basically means is that class definition defines namespace (like functions do), and it's body
  can contain statements - usually those are function definitions but there could be other constructs like if-else
  etc. See classes.py file for more details
  
* Name mangling:  
  ```python
  class A:
      def __gettext(self):
          return 'class A'
  
  obj = A()
  # obj.__gettext()  - AttributeError: 'A' object has no attribute '__gettext'
  
  print(obj._A__gettext())
  # >>> class A
  ```

* TODO