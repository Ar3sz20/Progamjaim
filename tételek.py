import os
os.system("cls")
lista =[11,12,13,14,15,16,17,18,19]
print("az input lista: ", lista)
print("a lista hossza", len(lista))

for index,elem in enumerate(lista):
    print("index: ",index , "az elem: ", elem)

print("/n")

def osszegzes_kl(lista):
 ossz = 0
 for elem in lista:
  osszeg = ossz + elem
 print("az összege az adatoknak: ", osszeg)

osszegzes_kl(lista)

def osszegzes(lista):
    osz = sum(lista)
    print(osz)
osszegzes(lista)
print("/n")