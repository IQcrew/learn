# https://docs.python.org/3/library/itertools.html

import itertools   # vsetky intertools su napisane v C

print("-----count------")
y= [1,2,3,4,5,6,7,8,9]
cntr = itertools.count(0,2)
y = list(map(lambda x: x+cntr.__next__(), y))
print(y)

print("-----cycle------")
obrazky = itertools.cycle([0,1,2,3]) #skoda ze som o tomto nevedel davnejsie XD
for i in range(10):
    print(obrazky.__next__())
    
print("-----repeat------")
print(list(map(pow, range(10), itertools.repeat(2))))  #dobre ako vstupny parameter pre zip z plavajucim počtom prvkov

print("------compress-------")
print(list(itertools.compress(["a","b","c","d","e"], [1,0,0,1,0]))) # zjednodusenie triedenia elementov podla indexu (aj debugovana)

print("------dropwhile-------") #take while is opposite
x = list(itertools.dropwhile(lambda y: y<10, [9,2,4,5,6,8,10,2,5,13,23,5,6,43,64,6]))
print(x)

print("------starmap-------")   # velmi cool (nahradi list comprehention )
print(list(itertools.starmap(pow, [(2,5), (3,2), (10,3)])))
print(list(itertools.starmap(lambda x,y : x*y, [(2,5), (3,2), (10,3)])))

print("------product-------")    # kombinarotika
print(list(itertools.product('ABCD', 'xy')))
print(list(itertools.product(range(2), repeat=3)))

print("------permutations-------") # skoro to iste ako .combinations() ... (alurat ze combinations musia byt iba sorted)
print(list(itertools.permutations('ABCD', 2)))
print(list(itertools.permutations([1,2,3])))
