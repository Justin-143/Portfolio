a = int(input("Enter num1"))
b = int(input("Enter num2"))
c = int(input("Enter num3"))
a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(b)]
c1=[int(i) for i in str(c)]

key2=max(a1)+max(b1)+max(c1)
key1=min(a1)+min(b1)+min(c1)
print(key1+key2)
