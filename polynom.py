def citire_polinom(polinom):
    fp = open("polinom.txt", "rt")
    polinom = {}
    
    grade_polinom = list(fp.readline().split())
    coeficienti_polinom = list(fp.readline().split())
    k = 0
    for i in grade_polinom:
        polinom[i] = coeficienti_polinom[k]
        k += 1
    print("A avut loc citirea polinomului din fisier")
    return polinom

def afisare_polinom(polinom):
    sir = ""
    for i in polinom.keys():
        #print(str(polinom[i]) + str("*X^") + str(i), end = " + ") # + ca sa elimin acel spatiu dupa print
        sir += polinom[i] + "*X^" + i + " + "
        # sir += "*X^"
        # sir += i
        # sir = sir[:-2]
    sir = sir.rstrip(' +')
    return sir
    # print(polinom)    

def calcul_polinom(polinom):
    x = int(input("Calculati valoarea polinomului in punctul "))
    val = 0
    for i in polinom.keys():
        val += float(polinom[i]) * (x ** float(i)) 
        # observatie: am pus float, deoarece coeficientii monomului dar si gradul monomului pot fi de tip float
    return val

def schimbare_monom(polinom):
    grad = input("Introduceti gradul noului monom: ") # nu merge cu cast 
    coef = input("Introduceti coeficientului noului monom: ")
    '''
    OK = 0
    for i in polinom.keys():
        #if float(grad) == float(i):
        print(polinom[i])
        if polinom[i] == float(coef):
        # de ce nu merge cu if grad in polinom.keys():
        # sau for grad in i: 
            polinom[grad] = float(coef) # nu este necesar float 
            OK = 1
    if OK:
        print("Noul polinom: ", afisare_polinom(polinom))
    else:
        print("Gradul sau coefientul introdusi nu exista in polinomul nostru") '''
    polinom[grad] = coef
    return polinom

def polynoms():
    print("1. Citirea polinomului din fisier")
    polinom = {}
    polinom = citire_polinom(polinom)
    print("2. Afisarea polinomului citit")
    print("Afisare polinom: ")
    print(afisare_polinom(polinom))
    print("3. Calculul valorii polinomului in punctul X")
    val = calcul_polinom(polinom)
    print("Valoarea polinomului", afisare_polinom(polinom), "este:", val)
    print("4. Modificarea unui monom din polinom")
    polinom = schimbare_monom(polinom)
    print(afisare_polinom(polinom))
    