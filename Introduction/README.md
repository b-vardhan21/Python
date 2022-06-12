## Introduction
#Python is a general purpose high level programming language</br>
#Developed by Guido van Rossam </br>
#published in 1991</br>
#uses -> Desktop Applications, web Applications, Database Applications</br>

## Reserved Words
>>> import keyword</br>
>>> keyword.kwlist</br>
 ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

## Inbulit data types
1) Int
2) Float
3) Complex
4) Bool
5) Str
6) Bytes
7) Bytearray
8) Range
9) List
10) Tuple
11) Set
12) Frozenset 
13) Dict
14) None


## Fundamental Data Types
1. int
2. float
3. complex
4. bool
5. str
   
## Int Data Type
We can use int data type to represent whole numbers </br>
Eg: a = 10</br>
type(a) //int</br>
Note:</br>
 But in Python3 there is no long type explicitly and we can represent long values also by
 using int type only.

## Float Data Type
 We can use float data type to represent floating point values (decimal values)</br>
 Eg: f = 1.234</br>
 type(f) float</br>

## Complex Data Type
Form >> a+bj</br>
a is a Real Part</br>
b is a Imaginary Part</br>

## bool Data Type
 We can use this data type to represent boolean values.</br>
 The only allowed values for this data type are:</br>
 True and False</br>
 Internally Python represents True as 1 and False as 0</br>

## str Data Type
str represents String data type.</br>
A String is a sequence of characters enclosed within single quotes or double quotes.</br>

### Type Casting
The following are various inbuilt functions for type casting
1. int()
2. float() 
3. complex()
4. bool()
5. str()

## Fundamental Data Types vs Immutability:
 1. All Fundamental Data types are immutable. i.e once we creates an object,we cannot perform any changes in that object. If we are trying to change then with those changes a new object will be created. This non-chageable behaviour is called immutability.
 2. In Python if a new object is required, then PVM won’t create object immediately. First it will check is any object available with the required content or not. If available then existing object will be reused. If it is not available then only a new object will be created. The advantage of this approach is memory utilization and performance will be improved.
 3. But the problem in this approach is, several references pointing to the same object, by using one reference if we are allowed to change the content in the existing object then the remaining references will be effected. To prevent this immutability concept is
required. According to this once creates an object we are not allowed to change content. If we are trying to change with those changes a new object will be created.

## bytes Data Type
 bytes data type represens a group of byte numbers just like an array.
  x = [10,20,30,40]
 b = bytes(x)
 type(b) > bytes
 print(b[0]) > 10
 print(b[-1]) > 40
 Note:
 1. The only allowed values for byte data type are 0 to 256. By mistake if we are trying to provide any other values then we will get value error.
 2.  Once we creates bytes data type value, we cannot change its values,otherwise we will get TypeError.

x=[10,20,30,40]
b=bytes(x)
b[0]=100
TypeError: 'bytes' object does not support item assignment

## bytearray data type
 bytearray is exactly same as bytes data type except that its elements can be modified.

 ## List Data Type
 Insertion Order is preserved</br>
 Heterogeneous Objects are allowed</br>
 Duplicates are allowed</br>
 Growable in nature</br>
 Values should be enclosed within square brackets.</br>

 ## Tuple Data Type
1. tuple data type is exactly same as list data type except that it is immutable.i.e we
cannot chage values.
2. Tuple elements can be represented within parenthesis.

## Range Data Type
 1. range Data Type represents a sequence of numbers.
 2. The elements present in range Data type are not modifiable. i.e range Data type is immutable.

## set Data Type
 Insertion order is not preserved</br>
 Duplicates are not allowed</br>
 Heterogeneous objects are allowed</br>
 Index concept is not applicable</br>
 It is mutable collection</br>
 
 ## frozenset data type
  1. It is exactly same as set except that it is immutable.
  2. Hence we cannot use add or remove functions.

## dict data type
Eg:d={101:'durga',102:'ravi',103:'shiva'} 

If we want to represent a group of values as key-value pairs then we should go for dict data type</br>
1. >>>d={101:'durga',102:'ravi',103:'shiva'}
2. >>>d[101]='sunny'
3. >>>d
4. {101:'sunny',102:'ravi',103:'shiva'}
5. 
6. Wecancreateemptydictionaryasfollows
7. d={}
8. Wecanaddkey-valuepairsasfollows
9. d['a']='apple'
10. d['b']='banana'
11. print(d)

Note: dict is mutable and the order won’t be preserved.</br>

## None data type
 None means nothing or No value associated.</br>
 If the value is not available, then to handle such type of cases None introduced.</br>
It is something like null value in Java.</br>


