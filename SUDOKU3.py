import random

x = 1
a = 45
g2 = 0
i = -1
t = 0
q = 0
b = 0
j = 0
c = 0
e = 0
f = 0
h = 0

#définition d'une grille de sudoku valide
g1 =[[3,6,7,9,4,1,2,8,5],
     [1,5,2,6,8,3,4,9,7],
     [4,9,8,7,5,2,1,6,3],
     [7,4,6,1,9,5,8,3,2],
     [8,1,9,2,3,7,6,5,4],
     [2,3,5,8,6,4,7,1,9],
     [9,2,1,5,7,8,3,4,6],
     [5,8,4,3,2,6,9,7,1],
     [6,7,3,4,1,9,5,2,8]]

#Fonction d'affichage
def aff():
    print(g1[0])
    print(g1[1])
    print(g1[2])
    print(g1[3])
    print(g1[4])
    print(g1[5])
    print(g1[6])
    print(g1[7])
    print(g1[8])

#fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la  colonne
def verif_colonne():
    global c
    tab = [g1[0][f],g1[1][f],g1[2][f],
           g1[3][f],g1[4][f],g1[5][f],
           g1[6][f],g1[7][f],g1[8][f]]
    
    if h != tab:
        c = True
        print("ok colo")
    else:
        print("erreur colonne")
        c = False

#fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la ligne
def verif_ligne():
    global l
    tab = [g1[e][0],g1[e][1],g1[e][2],
           g1[e][3],g1[e][4],g1[e][5],
           g1[e][6],g1[e][7],g1[e][8]]
    
    if h != tab:
        l = True
        print ("ok ligne")
    else:
        print("erreur ligne")
        l = False

#vérification de l'entrée de l'utilisateur
def verif_userinput():
    global b
    if e > 8:
        print("merci de mettre une valeur de ligne plus petite")
    if f > 8:
        print("merci de mettre une valeur de colonne plus petite")
    if e < 0:
        print("merci de mettre une valeur de ligne plus grande")
    if f < 0:
        print("merci de mettre une valeur de colonne plus grande")
    if h < 0:
        print("merci d'entrer un nombre compris entre 1 et 9")
    if h > 9:
        print("merci d'entrer un nombre compris entre 1 et 9")
    else :
        b = True
        print ("ok user input")

#définition d'une grille aléatoire
while i != 45:
    i = i + 1
    b = random.randint(0, 8)
    c = random.randint(0, 8)
    x = g1[b][c]
    g1[b][c] = 0
    g2 = g1
print("")
print("Bonne chance cette grille n'as pas l'air simple: ")
print("")
aff()

while j != 36:

    e = input("Dans quelle ligne voulez vous jouer ? ")
    f = input("Dans quelle colone voulez vous jouer ? ")
    e = int(e)
    f = int(f)
    e = e - 1
    f = f - 1
    h = input("Quelle valeur voulez vous entrez ? ")
    h = int(h)
    print("")
    verif_userinput()
    verif_colonne()
    verif_ligne()

    if b == c and c == l and l == True:

        if g2[e][f] == 0 and g1[e][f] == 0:
            j = j + 1
            g1[e][f] = h
            print("Vous avez ajouté une valeur")
            aff()
            print("")

        elif g2[e][f] != 0:
            print("Vous ne pouvez pas modifiez cette valeur")
            print("erreur 1")
            aff()
            print("")

        elif g2[e][f] == 0 and g1[e][f] != 0:
            g1[e][f] = h
            print("Vous avez modifiez une valeur")
            aff()
            print("")

        elif g2[e][f] != 0 and g1[e][f] != 0:
            print("Vous ne pouvez pas modifiez cette valeur")
            print("erreur 2")
            print("")

        else:
            print("erreur 3")
    else:
        print ("erreur 10")



