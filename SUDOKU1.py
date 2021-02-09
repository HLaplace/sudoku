import random

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
g2 = g1

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

#définition d'une grille aléatoire
a = 45
i = -1
while i != 45:
    i = i + 1
    b = random.randint(0, 8)
    c = random.randint(0, 8)
    x = g1[b][c]
    g1[b][c] = 0
print("")
print("Bonne chance cette grille n'as pas l'air simple: ")
print("")
g2 = g1
aff()

#définition du jeu
j = 0
while j != 36:
    #définition de l'entrée de l'utilisateur
    e = input("Dans quelle ligne voulez vous jouer ? ")
    f = input("Dans quelle colone voulez vous jouer ? ")
    e = int(e)
    f = int(f)
    e = e - 1
    f = f - 1

    if g1[e][f] == 0:
        h = input("--> ")
        print("")
        if g1[e][f] == g2[e][f]:
            g1[e][f] = int(h)
            j = j + 1
            aff()
        else :
            print ("\033[31mCe n'est pas la bonne valeur.\033[0m")
    else :
        print("\033[31mVous ne pouvez pas modifier cette valeur.\033[0m")

print("Well done")







