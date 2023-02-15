
feladat = int(input(("válasz feladatot: ")))

if feladat ==1:
 def my_function():
    a = open("input.txt","r")
    data = a.read()
    List = data.split(",")
    a.close()
    print(List)
 my_function()
 print()

elif feladat==2:
 def my_function2(input, mode):

    a = open(input, mode)
    data = a.read()
    List = data.split(",")
    print(List)
    a.close()

 my_function2("input.txt","r")
 print()

elif feladat==3:
 def my_function3(input, mode):
    with open(input,mode) as input_file:
        Line = input_file.read() .split(",")
    print()
    for i in Line:
        print(i)
 my_function3("input.txt","r")
 print()

elif feladat==4:
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

elif feladat==5:
 def masodfokumegoldokeplet(a,b,c):
     if a == 0:
       print("a nem lehett nulla")
     else:
      print("A megadott másodfokú egyenlet: f(x)=",a,"*X2",b,"x","+",c)
      D = (b*b)-(4*a*c)
     if D < 0:
      x1 = -b + math.sqrt(D)/(2*a) 
      x2 = -b - math.sqrt(D)/(2*a) 
      print ("Az egyik gyök: x1=", x1)
      print ("A másik gyök: x2=", x2)
 masodfokumegoldokeplet(2,5,9)
 masodfokumegoldokeplet(3,9,4)
 masodfokumegoldokeplet(5,7,2)
 print()

else:
    print ("ez nem feladat")