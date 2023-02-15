
if input(1):
 def my_function():
    a = open("input.txt","r")
    data = a.read()
    List = data.split(",")
    a.close()
    print(List)
 my_function()
 print()

elif input(2):
 def my_function2(input, mode):

    a = open(input, mode)
    data = a.read()
    List = data.split(",")
    print(List)
    a.close()

 my_function2("input.txt","r")
 print()

elif input(3):
 def my_function3(input, mode):
    with open(input,mode) as input_file:
        Line = input_file.read() .split(",")
    print()
    for i in Line:
        print(i)
 my_function3("input.txt","r")
 print()

elif input(4):
 import math
 def elsofokumegoldokeplet(m,b):
    if m == 0:
     print("nem lehet nulla az m paraméter")
    else:
        x = -b/m
        print("f(x)=",m,"*x","+",b)
        print("x = ", x)
 elsofokumegoldokeplet(4,5)
 elsofokumegoldokeplet(-4,3)
 elsofokumegoldokeplet(4,1)
 print()
elif input(5):
 def masodfokumegoldokeplet(a,b,c):
     if b**2 -4 * a * c < 0:
        return "sfge"
     else:
        x1 = (-b + math.sqrt(b**2 -4* a * c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 -4* a * c)) / (2*a)
        return x1,x2
 masodfokumegoldokeplet(2,5,9)
 print()

else:
    print ("ez nem feladat")