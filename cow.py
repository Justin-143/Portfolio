legs = int(input("Enter the number of total legs"))
heads = int(input("Enter the number of total heads"))
flag=False
for c in range(0,heads):
    h=heads-c
    if(c*4+h*2==legs):
        print("the total cows=",c)
        print("the total hens=")
        flag=True
        break

