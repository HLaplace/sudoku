import random

# import time
c = 0
l = 0
e = 0
f = 0
a = 0
b = 0
c = 0
i = 0
j = 0
x = 0
r = 0
z = 0

# définition d'une grille de sudoku valide
g1 = [[3, 6, 7, 9, 4, 1, 2, 8, 5],
      [1, 5, 2, 6, 8, 3, 4, 9, 7],
      [4, 9, 8, 7, 5, 2, 1, 6, 3],
      [7, 4, 6, 1, 9, 5, 8, 3, 2],
      [8, 1, 9, 2, 3, 7, 6, 5, 4],
      [2, 3, 5, 8, 6, 4, 7, 1, 9],
      [9, 2, 1, 5, 7, 8, 3, 4, 6],
      [5, 8, 4, 3, 2, 6, 9, 7, 1],
      [6, 7, 3, 4, 1, 9, 5, 2, 8]]

carré1 = [g1[0][0], g1[0][1], g1[0][2],
          g1[1][0], g1[1][1], g1[1][2],
          g1[2][0], g1[2][1], g1[2][2]]

carré2 = [g1[3][0], g1[3][1], g1[3][2],
          g1[4][0], g1[4][1], g1[4][2],
          g1[5][0], g1[5][1], g1[5][2]]

carré3 = [g1[6][0], g1[6][1], g1[6][2],
          g1[7][0], g1[7][1], g1[7][2],
          g1[8][0], g1[8][1], g1[8][2]]

# Fonction d'affichage
def aff():
    print(g1[0][0],"|",g1[0][1],"|",g1[0][2],"||",g1[0][3],"|",g1[0][4],"|",g1[0][5],"||",g1[0][6],"|",g1[0][7],"|",g1[0][8])
    print("------------------------------------")
    print(g1[1][0],"|",g1[1][1],"|",g1[1][2],"||",g1[1][3],"|",g1[1][4],"|",g1[1][5],"||",g1[1][6],"|",g1[1][7],"|",g1[1][8])
    print("------------------------------------")
    print(g1[2][0],"|",g1[2][1],"|",g1[2][2],"||",g1[2][3],"|",g1[2][4],"|",g1[2][5],"||",g1[2][6],"|",g1[2][7],"|",g1[2][8])
    print("------------------------------------")
    print("------------------------------------")
    print(g1[3][0],"|",g1[3][1],"|",g1[3][2],"||",g1[3][3],"|",g1[3][4],"|",g1[3][5],"||",g1[3][6],"|",g1[3][7],"|",g1[3][8])
    print("------------------------------------")
    print(g1[4][0],"|",g1[4][1],"|",g1[4][2],"||",g1[4][3],"|",g1[4][4],"|",g1[4][5],"||",g1[4][6],"|",g1[4][7],"|",g1[4][8])
    print("------------------------------------")
    print(g1[5][0],"|",g1[5][1],"|",g1[5][2],"||",g1[5][3],"|",g1[5][4],"|",g1[5][5],"||",g1[5][6],"|",g1[5][7],"|",g1[5][8])
    print("------------------------------------")
    print("------------------------------------")
    print(g1[6][0],"|",g1[6][1],"|",g1[6][2],"||",g1[6][3],"|",g1[6][4],"|",g1[6][5],"||",g1[6][6],"|",g1[6][7],"|",g1[6][8])
    print("------------------------------------")
    print(g1[7][0],"|",g1[7][1],"|",g1[7][2],"||",g1[7][3],"|",g1[7][4],"|",g1[7][5],"||",g1[7][6],"|",g1[7][7],"|",g1[7][8])
    print("------------------------------------")
    print(g1[8][0],"|",g1[8][1],"|",g1[8][2],"||",g1[8][3],"|",g1[8][4],"|",g1[8][5],"||",g1[8][6],"|",g1[8][7],"|",g1[8][8])

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la  colonne
def verif_colonne():
    global c
    c = 4
    tab = [g1[0][f], g1[1][f], g1[2][f],
           g1[3][f], g1[4][f], g1[5][f],
           g1[6][f], g1[7][f], g1[8][f]]

    if h != tab:
        c = True
        print("ok colo")

    else:
        print("erreur colonne")
        c = False

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la ligne
def verif_ligne():
    global l
    l = 4

    tab = [g1[e][0], g1[e][1], g1[e][2],
           g1[e][3], g1[e][4], g1[e][5],
           g1[e][6], g1[e][7], g1[e][8]]

    if h != tab:
        l = True
        print("ok ligne")

    else:
        print("erreur ligne")
        l = False

# Vérification que les valeurs entrée par l'utilisateur pour les lignes et les colones sont compatible
def verif_userinput():
    global b
    b = 4
    if e > 8:
        print("merci de mettre une valeur de ligne plus petite")
        b =False
    if f > 8:
        print("merci de mettre une valeur de colonne plus petite")
        b = False
    if e < 0:
        print("merci de mettre une valeur de ligne plus grande")
        b = False
    if f < 0:
        print("merci de mettre une valeur de colonne plus grande")
        b = False
    else:
        b = True
        print("")
        print("ok user input")

# Vérification que les valeurs entrée par l'utilisateur son compatible avec le jeu du sudoku
def verif_h():
    global z
    if h >= 10 or h <= 0:
        print("erreur h")
        z = False

    else:
        print("ok h")
        print("")
        z = True

# définition d'une grille aléatoire
while i != 45:
    i = i + 1
    b = random.randint(0, 8)
    c = random.randint(0, 8)
    x = g1[b][c]
    g1[b][c] = 0
print("Bonne chance cette grille n'as pas l'air simple: ")
print("")
g2 = g1
aff()

# définition de l'entrée de l'utilisateur
while j != 33:
    print("")
    e = input("Dans quelle ligne voulez vous jouer ? ")
    f = input("Dans quelle colone voulez vous jouer ? ")
    e = int(e)
    f = int(f)
    e = e - 1
    f = f - 1
    h = input("Quelle valeur voulez vous entrez ? ")
    h = int(h)
    verif_userinput()
    verif_colonne()
    verif_ligne()
    verif_h()

    # vérification de la validité des carrés à condition que la ligne et la colonne
    # associés à l'entrée de l'utilisateur soit validés ( t= 2 )
    if c == l and l == b and b == z and z == True:

        if g2[e][f] == 0 and g1[e][f] == 0:
            j = j + 1
            r = r + 1
            g1[e][f] = h
            print ("Vous avez ajouté une valeur")
            aff()

        elif g2[e][f] != 0:
            print("vous ne pouvez pas modifié cette valeur")
            print("erreur 1")

        elif g1[e][f] != 0 and g2[e][f] == 0:
            g1[e][f] = h
            print("Vous avez modifié une valeur")
            aff()

        elif g2[e][f] != 0 and g1[e][f] != 0:
            print("vous ne pouvez pas modifié cette valeur")
            print("erreur 2")

        else:
            print("erreur 4")
    else :
        print("erreur 100")

while a != 8:
    if g1[a][0] != g1[a][1] != g1[a][2] != g1[a][3] != g1[a][4] != g1[a][5] != g1[a][6] != g1[a][7] != g1[a][8]:
        print ("ok ligne :")
        print(a)
        print("")
        a = a + 1
    else :
        print ("erreur ligne")
        print (a)
        a = a + 1