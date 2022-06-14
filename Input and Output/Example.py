# Example 1
# By default output values are seperated by space.If we want we can specify seperator by
# using "sep" attribute
a,b,c=10,20,30
print(a,b,c,sep=',')
print(a,b,c,sep=':')

##Example 2
name="Durga"
salary=10000
gf="Sunny"
print("Hello{0}yoursalaryis{1}andYourFriend{2}iswaiting". format(name,salary,gf))
print("Hello{x}yoursalaryis{y}andYourFriend{z}iswaiting". format(x=name,y=salary,z=gf))

# Example 3
eno=int(input("EnterEmployeeNo:"))
ename=input("EnterEmployeeName:")
esal=float(input("EnterEmployeeSalary:"))
eaddr=input("EnterEmployeeAddress:")
married=bool(input("EmployeeMarried?[True|False]:"))
print("PleaseConfirmInformation")
print("EmployeeNo:",eno)
print("EmployeeName:",ename)
print("EmployeeSalary:",esal)
print("Employee Address :",eaddr)
print("Employee Married ? :",married)