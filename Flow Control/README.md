## What is the difference between for loop and while loop in Python?
We can use loops to repeat code execution</br>
Repeat code for every item in sequence -> for loop</br>
Repeat code as long as condition is true -> while loop</br>

# How to exit from the loop?
By using break statement
# How to skip some iterations inside loop?
By using continue statement.
# When else part will be executed wrt loops?
If loop executed without break

## pass statement:
pass is a keyword in Python.</br>
In our programming syntactically if block is required which won't do anything then we can define that empty block with pass keyword.

## Difference between del and None:
In the case del, the variable will be removed and we cannot access that variable(unbind operation)
1. s="durga"
2. del s
3. print(s)-> NameError: name 's' is not defined.
But in the case of None assignment the variable won't be removed but the corresponding object is eligible for Garbage Collection (re bind operation). Hence after assigning with None value, we can access that variable.
1. s = "durga"
2. s = None
3. print(s) -> None