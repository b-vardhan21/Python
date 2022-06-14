#Example 1
s=input("Enter String:")
i=0
for x in s:
    print("The character present at ",i,"index is :",x)
i=i+1

#Example 2
list=eval(input("EnterList:"))
sum=0
for x in list:
    sum=sum+x
print("The Sum =",sum)

#Example 3
for x in range(10,0,-1):
    print(x)