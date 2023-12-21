print("enter 1 to find area of Square")
print("enter 2 to find area of Rectangle")
print("enter 3 to find area of Triangle")
print("enter 4 to find area of Circle")
choice=float(input())
if(choice==1):
 print("enter a side of a square")
 sq=float(input())
 SqArea=sq*sq
 print("Area of Square=",SqArea)
elif(choice==2):
 print("enter length and breadth")
 l=float(input())
 b=float(input())
 RecArea=l*b
 print("Area of rectangle=", RecArea)
elif(choice==3):
 print("enter base and height") 
 base=float(input())
 height=float(input())
 TriArea=base*height
 print("Area of tri triangle=", TriArea)
 r=float(input())
 print("Area of Circle=",CtrArea)
else:
 print("enter radius")
 CirArea=(22/7)*г*г
 print("invalid choice")