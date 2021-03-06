# CLI-app-Python
CLI application in Python

## Programul reprezinta o interfata de tip meniu in CLI, command line interface. Meniul a fost proiectat ca o bucla infinita, adica printr-o structura while True: 

### Doar apasarea tastei X va duce la oprirea secventei infinite while True: (moment in care se  apeleaza functia exit() care inchide script-ul scris in Python). 

### Practic, are loc terminarea aplicatiei. Celelalte optiuni ale meniului introduc diverse concepte studiate la disciplinele de programare din Stiinta Calculatoarelor. 

Se prezinta diferite probleme, lucrandu-se in paradigma programarii modulare, adica s-a utilizat conceptul de "Python modules", fiecare fisier ce contine diverse functii fiind 
importat in fisierul main. 

# 1. Operatii basic cu dictionare in Python. Modulul dictionar.py contine diverse functii care ajuta la gestiunea scolara a studentilor. 
Programul citeste informatii despre studenti in formatul ID, Nume Student, Note (inregistrarea text fiind formata din 2 campuri separate cu o virgula, primul camp fiind ID-ul studentului). Executia acestei functii produce o iesire cu un format specific. 

# 2. Operatii cu polinoame. Acest modul implementeaza diverse functii legate de polinoame. 

Programul citeste informatii despre un polinom dintr-un fisier cu extensia txt avand urmatoarea structura: 

	- pe prima linie sunt gradele fiecarui monom
	- pe a 2-a linie regasim coeficientii polinomului

Executia functiei polynom din fisierul importat polynom.py va produce o iesire cu un anumit format. 

# 3. Greedy. 

## Metoda Greedy o folosim intr-o situatie in care de exemplu avem o multime A si se cere sa se gaseasca o submultime B a sa care sa indeplineasca anumite conditii sau un anumit criteriu. De precizat faptul ca aceasta metoda nu isi propune gasirea celor mai bune solutii ale problemei date, ci doar a uneia dintre ele care indeplineste criteriul de optimizare ales. 

Mecanismul general al metodei Greedy este urmatorul: 

	- se initializeaza multimea solutiile cu multimea vida (B = null, adica multime vida) 
	- se alege un element x din multimea A 
	- se verifica daca un element ales poate fi adaugat la multimea solutiilor, daca da va fi adaugat B = B + {x} 
	- se continua repetitiv cu pasul al doilea pana cand au fost determinate toate elementele din multimea solutiilor 

In continuare se rezolva problema rucsacului (are un anumit volum V si n obiecte avand fiecare volumele vi si pretul pi). 
Rucsacul va fi umplut astfel incat pretul total al obiectelor introduse sa fie maxim. 

Rezolvarea consta in faptul ca se introduc in rucsac obiectele unul cate unul, in ordinea descrescatoare a raportului pi/vi, 
incat suma volumelor introduse sa fie mai mica sau cel mult egala cu V. 

De remarcat faptul ca metoda Greedy rezolva anumite probleme de optimizare. 

Este important ca listele / vectorii p si v sa fie sortati descrescator. 

# 4. Backtracking - metoda de cautare cu revenire. 

## Se rezolva problema podurilor sau a arhipelagului pe insule. 

Avem un arhipelag de insule cu n poduri, podul fiind cel care leaga acele insule. Trebuie sa determinam care este ordinea de parcurgere din poduri pornind de la o insula de start, apoi vom afisa toate drumurile posibile. 

  - n reprezinta numarul de poduri
  - variabila ins_start reprezinta de unde porneste parcurgerea (insula de la care se porneste parcurgerea 
  - pentru fiecare pod in parte avem o pereche de valori ins1 si ins2, ce vor fi inlocuite cu, coloana 0 si 1 din matricea pod. 

pod[n] poate fi vazut ca un vector de structuri, insa pentru ca in Python nu avem conceptul de structura, ci de clasa, vom memora "pod" intr-o matrice de n linii si 2 coloane. 

Daca am dori sa manipulam ca in structurile din C, adica accesand datele membre, insula 2 si insula 2, putem declara o clasa pod in care avem 2 variabile si apoi putem accesa aceste campuri ca si structuri. Pentru simplitate, s-a preferat ca informatiile sa fie stocate intr-o matrice de n linii si 2 coloane. Coloana cu index 0 pentru prima, respectiv coloana cu index 1 pentru a doua insula. 

Datele de iesire va fi sirul x1, x2, ..., xn, fiecare element xi reprezentand indicele unui pod [0, n-1]. 

Solutia problemei consta intr-un vector de n elemente in care specificam indicele podului in ordinea traversarii lui. Avem n poduri, adica n-1 indice. 

Variabilele n, x si pod, adica tabloul de poduri, vor fi declarate toate global. 

Variabila ins_crt reprezinta insula curenta. 

Prima conditie din structura backtracking este ca traversarea podului se va face o singura data, deci una din conditiile pe care trebuie sa le indeplineasca este ca acel pod nu trebuie sa existe deja. 

A doua conditie este ca insula curenta sa se afle pe unul din capetele podului. 

De precizat faptul ca in momentul cand nu mai avem seturi de date din fisier, bucata de program se va opri. Fiecare problema apartinand fiecarui set de date este, evident, rezolvata. 

Backtracking este si cea mai costisitoare metoda din punct de veder eal timpului de executie. 

Este o metoda generala de programare si poate fi adaptata pentru orice problema penrtru care dorim sa obtinem toate solutiile posibile, sau sa selectam o solutie optima, din multimea solutiilor posibile. 

