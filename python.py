def time_to_reach_top(x,y,z):
    h=0
    m=0
    while(h<x):
        m +=1
        if m%2 ==1:
            h +=y
        else:
            h -=z
    return m
print("Testcase1 output:",time_to_reach_top(30,10,5))
print("Testcase2 output:",time_to_reach_top(21,5,3))