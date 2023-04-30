a=input("Enter a string: ")
b=a.lower()
unique=set(b)
len=len(unique)
print("unique = ",end=" ")
for i in unique:
    print(i,end="")
    if len-1>0:
        print(",",end="")
        len=len-1