def my_function():   #definiálom a fügvényem majd behívom
  print("Hello from a function")

my_function()

def my_function(fname): #definiálom a fügvényt majd argumeneket adok meg a hozzá és egyben írodik ki
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname): #egyszere bármennyi "érvet" lehet a fügvényhez hozzá adni
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(*kids): #definiálom a fügvényt úgy hogy azt írja lista harmadik eleme elé hogy "a legfiatalabb gyerek"
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1): #itt csak a legfitalabb gyerek neve írodik ki
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(country = "Norway"): #itt ahol nincs megadva argument oda írja hogy Norway
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food): #kiírja a lista elemeit egy más alá
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):  # vissza hívja az argument ötszöröséhez
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction(): #az űres fügvényt kihagyod
  pass