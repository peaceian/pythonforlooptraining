#方法1 f string

for x in range(1,10):
    for y in range(1,10):
        print(f"{y:}*{x:}={y*x:2}",end=" ")
    print()
    
#方式2 format

for x in range(1,10):
    for y in range(1,10):
        print("{:}*{:}={:>2}".format(y,x,y*x),end=" ")
    print()
    
#方式3 %d

for x in range(1,10):
    for y in range(1,10):
        print("%d*%d=%2d"%(y,x,y*x),end=" ")
    print()