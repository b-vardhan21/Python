## String
Any sequence of characters within either single quotes or double quotes is considered as a String.</br>
Note:</br>
In most of other languges like C, C++, Java, a single character with in single quotes is treated as char data type value. But in Python we are not having char data type.Hence it is treated as String only.</br>

Eg:</br>
>>>ch='a'</br>
>>> type(ch)</br>
<class 'str'></br>

## slice operator:
Syntax: s[beginindex:endindex:step]</br>
Begin Index: From where we have to consider slice (substring)</br>
End Index: We have to terminate the slice (substring) at endindex-1</br>
step: Incremented Value.</br>

Note:</br>
If we are not specifying bEgin index then it will consider from bEginning of the string.</br>
If we are not specifying end index then it will consider up to end of the string.</br>
The default value for step is 1.</br>
In the backward direction if end value is -1 then result is always empty.</br>
In the forward direction if end value is 0 then result is always empty.</br>

## Mathematical Operators for String:
We can apply the following mathematical operators for Strings.</br>
 1. + operator for concatenation
 2. * operator for repetition

print("durga"+"soft") -> durgasoft</br>
print("durga"*2) -> durgadurga</br>

Note:-</br>
1. To use + operator for Strings, compulsory both arguments should be str type.
2. To use * operator for Strings, compulsory one argument should be str and other argument should be int.

## len() in-built Function:
We can use len() function to find the number of characters present in the string.
Eg:</br>
s = 'durga'</br>
print(len(s)) -> 5</br>


``` python
s = "Learning Python is very easy!!!"
length = len(s)
i = 0
print("Forward Direction")
while i < length:
    print(s[i], end = '')
    i = i+1
print()
print("Backward Direction")
temp = length
while length <= temp & length > 0:
    print(s[length - 1], end = '')
    length = length - 1

```