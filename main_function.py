from dictionar import *
from polynom import *
from metoda_greedy_python import *
from metoda_backtracking_python import *

print("1. Dictionar studenti")
print("2. Operatii polinom din fisier")
print("3. Greedy")
print("4. Backtracking")
print("I. Informatii autor")
print("X. <terminare app>")

while True:
    c = input("Introduceti o valoare: ")
    if c == '1':
        dictionar_student()
    elif c == '2':
        polynoms()
    elif c == '3':
        greedy()
    elif c == '4':
        metoda_backtracking_python()
    elif c.upper() == 'I':
        print("Fulga Sergiu-Sebastian")
        print("github.com/sebastianfulga")
    elif c.upper() == 'X':
        print("<terminare app>")
        exit()
    else:
        print("S-a introdus o valoare gresita din meniu !")
