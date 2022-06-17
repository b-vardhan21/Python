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
