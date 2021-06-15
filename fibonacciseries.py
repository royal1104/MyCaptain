print("Enter a positive number")
a = int(input())
f = 0
s = 1
if a<=0:
    print("The requested series is: ",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next