def citire():
    dictStudenti = {}
    dictNote = {}
    n = int(input("Dati nr de studenti: "))
    for i in range(n):
        sir = input("Introduceti datele despre studentul "+str(i+1)+':').split(',')
        ID = int(sir[0])
        nume = sir[1]
        note = [int(x) for x in sir[2].split()]
        dictStudenti[ID] = nume
        dictNote[ID] = note
    return dictStudenti, dictNote

def afisare_stud(dictStudenti):
    print("ID\tNume tudent")
    for i in dictStudenti: 
        print(i, "\t" + str(dictStudenti[i]))

def afisare_note(dictNote):
    print("ID\tNote")
    for i in dictNote.keys():
        print(i, "\t", *dictNote[i])

def afisare_studenti_note(dictStudenti, dictNote):
    print("ID\tNume Student\t\tNote")
    print("-" * 50)
    for i in dictStudenti.keys(): # for i in dictNote.keys()
        print(i, "\t", dictStudenti[i], "\t\t\t", *dictNote[i])
    
def cautare_student(dictStudenti, dictNote, numeStudent):
    print("ID\tNume Student\t\tNote")
    print("-" * 40)
    for i in dictStudenti.keys(): # dictNote.values() # dictNote.items() 
        if numeStudent in dictStudenti[i]:
            print(i, "\t", dictStudenti[i], "\t\t", *dictNote[i])

def afisare_studenti_promovati(dictStudenti, dictNote):
    print("ID\t\tNume Student\t\tNote")
    for i in dictNote.keys():
        s = 0
        nr = 0
        for j in dictNote[i]:
            s = s + j
            nr += 1
        media = 0
        media = s / nr
        if media >= 5:
            print(i, "\t\t", dictStudenti[i], "\t\t", media)
            
def dictionar_student():
    print("Incarcare informatii despre studenti de la tastatura")
    print("Formatul este de tipul ID, Nume Student, Note Obtinute")
    dictStudenti, dictNote = citire()
    print("Afisare studenti")
    afisare_stud(dictStudenti)
    print("Afisare note")
    afisare_note(dictNote)
    print("Afisare studenti si notele obtinute")
    afisare_studenti_note(dictStudenti, dictNote)
    print("Cautare student dupa nume")
    numeStudent = input("Dati numele studentului: ")
    print(numeStudent)
    cautare_student(dictStudenti, dictNote, numeStudent)
    print("Afisare studenti promovati")
    print("Studenti promovati")
    afisare_studenti_promovati(dictStudenti, dictNote)
