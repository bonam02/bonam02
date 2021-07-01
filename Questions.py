
list vs tuple

dict, defaultDict, OrderedDict

module vs package

lambda

namespaces : Local namespace
             Global namespace
            Built-in namespace

how tuples can be used as keys in dictionaries (why only tuples - Because tuples are hashable and lists are not)

Ref : https://stackoverflow.com/questions/1938614/in-what-case-would-i-use-a-tuple-as-a-dictionary-key/1938638

pickling and unpickling

***Decorators

Difference between generators and iterators

"//" operator - floor division

Switch is implemented in python 3.10

Ex: def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2

Ref : https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

What is GIL : Global Interpreter Lock

new Throwable.printstacktrace() in java = traceback.print_stack() in python

Homogeneous, which means data inside an array must be of the same Datatype

NumPy - Numerical Python - NumPy is easy to use, well-optimized and highly flexible.

NumPy 3D array  : num3=[[[1,2,3],[4,5,6],[7,8,9]]]

num3 = np.array(num3)

shape in numpy is used to get the dimensions (whether it is two dimensions or three or one)

to identify data type we can use dtype

to check size we can use size method
ex: from above example num3.size gives 9 as output

Differnce b/w loc and iloc in pandas : https://towardsdatascience.com/how-to-use-loc-and-iloc-for-selecting-data-in-pandas-bd09cb4c3d79


all() - function returns True if all items in an iterable are true, otherwise it returns False.
Ex : mylist = [0, 1, 1]
x = all(mylist)
o/p : False because 0 is false

__call__ in Python - The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function
Ex :
class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

# Instance created
e = Example()

# __call__ method will be called
e()



QuerySet is a collection of SQL queries. The command print(b.query) shows you the SQL query created from the Django filter call.

