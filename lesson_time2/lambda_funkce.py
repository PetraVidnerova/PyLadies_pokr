
def pozdrav():
    print("*** Ahoj! ***")

def kratky_pozdrav():
    print("Ahoj!")

pozdrav()
kratky_pozdrav()

# fce jako parametr funkce

def opakuj(fce):
    for _ in range(5):
        fce()

opakuj(pozdrav)
opakuj(kratky_pozdrav)

# lambda funkce 
pozdrav_lbd = lambda: print("*** Ahoj! ***")
kratky_pozdrav_lbd = lambda: print("Ahoj!")

pozdrav_lbd()
kratky_pozdrav_lbd()

opakuj(pozdrav_lbd)

opakuj(lambda: print("Tohle je lambda funkce!"))

fce_x = lambda x: int(x)**2

def proved_funkci(fce):
    x = input("Zadej x: ")
    print("Vysledek: ", fce(x))

proved_funkci(fce_x)

proved_funkci(lambda x: int(x)*5)

# slovnik lambda funkci
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a*b
}

operace = input("Zadej operaci +,-,*: ")

a = int(input("Zadej a: "))
b = int(input("Zadej b: "))

print(operators[operace](a, b))

