def citire():
    n = int(input("n = "))
    while n <= 0:
        n = int(input("n = "))
    p = [0] * n
    v = [0] * n
    for i in range(n):
        p[i] = float(input("p[ %d ] = " %i))
        while p[i] <= 0:
            print("Pretul trebuie sa fie > 0")
            p[i] = float(input("p[ %d ] = " %i))
        v[i] = float(input("v[ %d ] = " %i))
        while v[i] <= 0:
            v[i] = float(input("v[ %d ] = " %i))
    V = float(input("V =")) # fara float va da eroare ... 
    return n, p, v, V

def afisare(n, p, v, V):
    print("Preturile obiectelor ")
    for i in range(n):
        print(p[i], end = " ")
    print("\nVolumul obiectelor ")
    for i in range(n):
        print(v[i], end = " ")
    print("\nV = ", V)

def sort_desc_vect(p, v, dim):
    ok = 1;
    while ok:
        ok = 0
        for i in range(dim-1):
            if p[i] / v[i] < p[i+1] / v[i+1]:
                p[i], p[i+1] = p[i+1], p[i]
                v[i], v[i+1] = v[i+1], v[i]
                ok = 1
    return p, v

def solutie(n, p, v, V):
    x = [0] * n 
    i = 0
    vt = pt = 0
    while vt < V and i < n:
        if vt + v[i] <= V:
            x[i] = 1
            pt = pt + p[i]
            vt = vt + v[i]
        else:
            x[i] = (V-vt)/v[i]
            vt = V
            pt = pt + p[i] * x[i]
        i += 1
    print("Pretul total al obiectelor din rucsac = ", pt, "Volumul ocupat = ", vt)
    print("In rucsas s-au introdus: ")
    for i in range(n):
        if x[i] > 0:
            print("Obiectul ", i, "(", v[i] * x[i], ",", p[i], ")")

def greedy():
    n, p, v, V = citire()
    afisare(n, p, v, V)
    p, v = sort_desc_vect(p, v, n)
    afisare(n, p, v, V)
    solutie(n, p, v, V)