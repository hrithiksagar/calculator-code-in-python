#program using different operators
x=int(input("enter first number"))
y=int(input("enter second number"))
add=x+y
sub=x-y
mul=x*y
div=x/y
pow=x**y

print("enter your choice")
print("1:addition,2:substraction,3:multiplication,4:division,5:power,6:equality")
ch=int(input())
if(ch==1):
    print(add)
elif(ch==2):
    print(sub)
elif(ch==3):
    print(mul)
elif(ch==4):
    print(div)
elif(ch==5):
    print(pow)
elif(x>y):
    print(true)
else:
    print("invalid input")