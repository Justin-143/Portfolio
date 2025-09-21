def find(x,y,z):
    time=0
    ht=0
    step=1
    while(ht<x):
        if(step%2!=0):
            ht=ht+y
            time=time+1
            step=step+1
        else:
            ht=ht-z
            time=time+1
            step=step+1
    print("Time is",time)
find(x=21,y=5,z=3)
