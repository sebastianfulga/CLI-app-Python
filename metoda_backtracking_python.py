def Plimbare(insula_crt, k):
    global n, x, pod
    if n == k:
        afisSolutie()
    else:
        for i in range(n):
            if POSIBIL(i, k, insula_crt):
                x[k] = i
                if insula_crt == pod[i][0]:
                    ins = pod[i][1]
                else:
                    ins = pod[i][0]
                Plimbare(ins, k+1)

def POSIBIL(alfa, k, ins_crt):
    global x, pod
    for j in range(k):
        if x[j] == alfa:
            return False
    return pod[alfa][0] == ins_crt or pod[alfa][1] == ins_crt

def afisSolutie():
    global n, x, nsol
    nsol += 1
    print("\nSolutia", nsol,"x =", x)
    

# pod[alfa][0]
# global n, x, pod

#n = 5
#ins_start = 'E'
#
'''
pod = [
    ['A', 'B'],
    ['B', 'C'],
    ['A', 'C'], # nu conteaza ordinea 
    ['B', 'D'],
    ['D', 'E']
    ]
# x = [[0 for i in range(n)] for i in range(n)]
Plimbare('E', 0)
'''

def init():
    global n, ins_start, pod
    n = 5 # numarul de poduri ...
    ins_start = 'E'
    
    pod = [
    ['A', 'B'],
    ['B', 'C'],
    ['A', 'C'], # nu conteaza ordinea 
    ['B', 'D'],
    ['D', 'E']
    ]
        
def afisare(n, ins_start, pod):
    print("Insula de start: ", ins_start)
    print("Afisarea podurilor Matricea drumurilor: ")
    for i in range(n):
        print("Podul %d: " %(i+1), pod[i][0], pod[i][1]) # sau cu + str(pod[i][0]) + str(pod[i][1])

def citire_fisier(fp):
    global n, ins_start, pod
    n = fp.readline().split()
    while not len(n):
        n = fp.readline().split()
    n = int(n[0])
    ins_start = fp.readline().split()
    ins_start = str(ins_start[0])
    pod = [[0 for i in range(2)] for j in range(n)]
    for i in range(n):
        pod[i] = fp.readline().split()
        
def rezolvare():
    global x, nsol
    nsol = 0
    x = [0] * n
    Plimbare(ins_start, 0)

def metoda_backtracking_python():
    fp = open("seturi.txt", "rt")
    nr = 0
    print("Initializare date")
    init()
    print("Afiseaza matricea drumurilor")
    afisare(n, ins_start, pod)
    print("Rezolvare pentru setul initializat ...")
    rezolvare()
    print("Citire date din fisier")
    for i in range(4): # 4 reprezinta numarul de seturi din fisier 
        citire_fisier(fp)
        print("A avut loc citirea setului %d din fisier !" %(i+1))
        rezolvare()
    print("Nu mai sunt seturi de date in fiser !")
    fp.close()
