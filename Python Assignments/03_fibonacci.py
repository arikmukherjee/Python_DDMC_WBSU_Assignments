n=int(input("Enter Number: "))
n1=0
n2=1
next=n2
count=1
while count<=n:
    print(next,end=" ")
    count=count+1
    next=n1+n2
    n1,n2=n2,next
    print("Fibonacci series is: ",next)