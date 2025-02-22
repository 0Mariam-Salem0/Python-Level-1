#Start of 2 meetings (1 and 2)
#Lecture 1
#Python indentation
if 5 > 2:
    print("five is greater than two")
#if 5 > 2:
#print("five is greater than two")
#expected indented (needs space before the line)
#IndentationError: expected an indented block after 'if' statement on line 5
print("----------------------------------------")
if 5 > 2:
    print("five is greater than two")
    print("five is greater than two")
"""
if 5 > 2:
    print("five is greater than two")
          print("five is greater than two")
#unexpected indent (don't need space before the line)          
#IndentationError: unexpected indent
"""
print("----------------------------------------")
#Comments
print("comments started by the hash (#) or between 3 double quotes ")
#("""....""")
#This is a comment 
"""This is a comment"""
print("----------------------------------------")
#Python variables (variables are containers for storing data values)
#Data values (which are stored in the variables)
x = 5
y = 5.3
z = "hello world"
print(x)
print(y)
print(z)
print("----------------------------------------")
#Data type
#print(type()function) (to know the type of the data value which is assigned to the data variable)
print(type(x))
print(type(y))
print(type(z))
print("----------------------------------------")
#Casting (specify the data type of the variable)
x = str(3)
#"3"
y = int(3)
#3
z = float(3)
#3.0
print(x)
print(y)
print(z)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print("----------------------------------------")
#Quotes
print("string can be put between single quotes or double quotes")
print("""(x = 'hello world') is equal to (x = "hello world")""")
print('hello world')
print("hello world")
print("----------------------------------------")
#Lecture 2
#Case-sensitive
A = "python"
a = 4
print(A)
print(a)
"""
a = 4
print(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
# A not equal to a
"""
print("----------------------------------------")
#Multiple variables
#many values to multiple variables
x, y, z = "apple", "orange", "banana"
print(x)
print(y)
print(z)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print("----------------------------------------")
#one value to multiple variables
x = y = z = "WORLD"
print(x)
print(y)
print(z)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print("----------------------------------------")
#Unpack a collection
fruits = ["apple", "orange", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("----------------------------------------")
#Variables
print("variable name can start with a letter or underscore only")
print("variable names don't contain spaces")
print("variable name can not start with a number")
print("variables can contain alphabets (A-Z or a-z) & numbers (0-9) & underscore (_) ")
print("such as (name, Name, Name_python, _python, python_1)")
print("----------------------------------------")
#Outout variables
#Combine text & variable
x = "awesome"
print("python is " + x)
print("----------------------------------------")
#Combine variable & variable
x = "python is "
y = "awesome"
print(x + y)
z = x + y
print(z)
print("----------------------------------------")
#Concatenation
#plus (+) is used to combine texts & variables or as mathematical operator
x = 5
y = 10
print(x + y)
print("----------------------------------------")
#Combine a string with a number
x = str(5)
y = " python"
print(x + y)
"""
x = 5
y = "python"
print(x + y)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
print("----------------------------------------")
#Data Types
#Built-in data types
print("categories:\n"
      "Text type: str\n"
      "Numeric types: int,float\n"
      "Sequences types: list,tuple\n"
      "Boolean type: bool")
print("----------------------------------------")
#Getting data type
#use type() function (get the data type of any object)
x = 5
print(type(x))
print("----------------------------------------")
#Setting the data type
#Specifying the data type by (int, float, string) #This process is called Casting
x = int(5)
y = float(5)
z = str(5)
print(x)
print(y)
print(z)
print("----------------------------------------")
#Data types
print("int is integer: whole number + or - with no decimals")
x = 1
y = 294493497439493
z = -1
print(x)
print(y)
print(z)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print("----------------------------------------")
print("float is floating point number: a number + or - with decimals")
x = 1.10
y = 1.0
z = -33.99
w = 33e4
#e is power of 10 (exponential)
print(x)
print(y)
print(z)
print(w)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print("----------------------------------------")
#Casting int(), float(), str()
x = int(1)
y = int(2.8)
z = int("3")
a = float(1)
b = float(2.8)
c = float("3")
d = float("4.2")
k = str("s1")
l = str(2)
m = str(3.0)
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(k)
print(l)
print(m)
print("----------------------------------------")
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(k))
print(type(l))
print(type(m))
print("----------------------------------------")
#assigning multiline string to a variable by triple quotes
print("multiline string can be put between 3 quotes assigned to any variable")
a = """hello
python
world
"""
print(a)
print("----------------------------------------")
#string are arrays
#Counting starts from 0
#space is counted
a = "Hello, world!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])
print("----------------------------------------")
#Types of operators
print("Arithmetic operators")
print(10 + 5)
x = 10
y = 3
print("+          Addition         ", x + y)
print("-          Subtraction      ", x - y)
print("*          Multiplication   ", x * y)
print("/          Division         ", x / y)
print("%          Modulus          ", x % y)
print("**         Exponentiation   ", x ** y)
print("//         Floor division   ", x // y)
print("----------------------------------------")
print("Assignment operators")
print("=        x = 5      equals to      x = 5")
print("+=       x += 5     equals to      x = x + 5")
print("-=       x -= 5     equals to      x = x - 5")
print("*=       x *= 5     equals to      x = x * 5")
print("/=       x /= 5     equals to      x = x / 5")
print("%=       x %= 5     equals to      x = x % 5")
print("//=      x //= 5    equals to      x = x // 5")
print("**=      x **= 5    equals to      x = x ** 5")
print("----------------------------------------")
print("Comparison operators")
print("==          equal                          x == y")
print("!=          not equal                      x != y")
print(">           greater than                   x > y")
print("<           less than                      x < y")
print(">=          greater than or equal          x >= y")
print("<=          less than or equal             x <= y")
print("----------------------------------------")
print("Logical operators")
print("and       returns true if both statements are true       x < 5 and x < 10")
x = 4
if x < 5 and x < 10:
    print("x is less than 5 and 10")
print("or        returns true if one of the statements is true       x < 5 or x < 10")
x = 9
if x < 5 or x < 10:
    print("x is less than 5 or 10")
print("not       reverse the result & returns false if the result is true     not(x < 5 and x < 10)")
x = 11
if not(x < 5 and x < 10):
    print("x is not less than 5")
print("----------------------------------------")
#Getting user input
value = input("please enter a string:\n")
print("your name is " + value)
print("you entered", value, "and its type is", type(value))
print(f"you entered {value} and its type is {type(value)}")
print(type(value))
#print("you entered " + {value} + "and its type is " + {type(value)})
#TypeError: can only concatenate str (not "set") to str
print("----------------------------------------")
value_1 = input("please enter your first name\n")
value_2 = input("please enter your second name\n")
value_3 = input("please enter birth year\n")
age = 2022 - int(value_3)
print("user's full name is", value_1, value_2)
print("user's age is", str(age))
print(type(value_1))
print(type(value_2))
print(type(value_3))
print("----------------------------------------")
#End of 2 meetings