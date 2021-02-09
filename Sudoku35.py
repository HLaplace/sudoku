import random #importation de la librairie random pour définir aléatoirement une grille

ligne = 0 # booléen utilisé pour la vérification des valeurs de ligne
colonne = 0 # booléen utilisé pour la vérification des valeurs de colonne

en_ligne = 0 # entrée de ligne du joueur
en_colonne = 0 # entrée de colonne du joueur
en_utilisateur = 0 #valeur que le joueur veux mettre dans la grille

rdm = 0 # varialbe aléatoire utilisé pour la définition aléatoire de ma grille
rdm2 = 0 # seconde varialbe aléatoire utilisé pour la définition aléatoire de ma grille
rdm_valeur1 = 0 # valeur aléatoire de ligne utilisé pour définir aléatoirement ma grille
rdm_valeur2 = 0 # valeur aléatoire de colonne utilisé pour définir aléatoirement ma grille

jeu = 0 # variable permettant de suivre l'évolution de l'utilisateur dans le jeu

# définition d'une grille de sudoku valide
grille1 = [ [3, 6, 7, 9, 4, 1, 2, 8, 5],
            [1, 5, 2, 6, 8, 3, 4, 9, 7],
            [4, 9, 8, 7, 5, 2, 1, 6, 3],
            [7, 4, 6, 1, 9, 5, 8, 3, 2],
            [8, 1, 9, 2, 3, 7, 6, 5, 4],
            [2, 3, 5, 8, 6, 4, 7, 1, 9],
            [9, 2, 1, 5, 7, 8, 3, 4, 6],
            [5, 8, 4, 3, 2, 6, 9, 7, 1],
            [6, 7, 3, 4, 1, 9, 5, 2, 8] ]

# Fonction d'affichage formatée de la grille de Sudoku
def affichage_grille():

    for k in range(9):
        print('|', end = '')
        for j in range(9):
            print(grille1[k][j], end = ' | ')
        print('\n------------------------------------')
    print("")

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la  colonne
def verif_colonne():

    tab = [grille1[0][en_colonne - 1], grille1[1][en_colonne - 1], grille1[2][en_colonne - 1],
           grille1[3][en_colonne - 1], grille1[4][en_colonne - 1], grille1[5][en_colonne - 1],
           grille1[6][en_colonne - 1], grille1[7][en_colonne - 1], grille1[8][en_colonne - 1]]
    try:
        tab.index(en_utilisateur) #Si la valeur n'est pas trouvée, un erreur est lancée et je retourne True. Je False sinon.
        print("La valeur est déjà dans la colonne")
        return False
    except ValueError:
        return True

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la  ligne
def verif_ligne():
    tab = [grille1[en_ligne - 1][0], grille1[en_ligne - 1][1], grille1[en_ligne - 1][2],
           grille1[en_ligne - 1][3], grille1[en_ligne - 1][4], grille1[en_ligne - 1][5],
           grille1[en_ligne - 1][6], grille1[en_ligne - 1][7], grille1[en_ligne - 1][8]]
    try:
        tab.index(en_utilisateur)
        print("La valeur est déjà dans la ligne")
        return False
    except ValueError:
        return True

#Fonction qui verifie qu'un entier est entre 1 est 9 compris
def verif_valeur(int_to_test):
    temp_var = 0
    if int_to_test >= 10 or int_to_test <= 0:
        print("mettre une valeur entre 1 et 9")
        temp_var = False
    else:
        temp_var = True
    return temp_var

def verif_carre():
    l, c = n // 9, n % 9
    lb, lr = l // 3, l % 3
    cb, cr = c // 3, c % 3

    for lr2 in range(0, 3):
        for cr2 in range(0, 3):
            if ((lr2 != lr or cr2 != cr) and grille[(lb * 3 + lr2) * 9 + (cb * 3 + cr2)] == grille[n]):
                return False
    return True

# fonction pour dfinir  aléatoirment la grille
def grille_aleatoire():
    global rdm
    while rdm != 45:
        rdm_valeur1 = random.randint(0, 8)
        rdm_valeur2= random.randint(0, 8)
        if grille1[rdm_valeur1][rdm_valeur2] != 0:
            rdm2 = grille1[rdm_valeur1][rdm_valeur2]
            grille1[rdm_valeur1][rdm_valeur2] = 0
            rdm = rdm + 1
    print("")
    print("Bonne chance cette grille n'as pas l'air simple: ")
    print("")

#----------------------------------------------------
#------------------Lancement du jeu------------------
#----------------------------------------------------

grille_aleatoire()

#copie de grille1 dans grille2
grille2 = []
for i in range(len(grille1)):
    grille2.append(grille1[i][:])
affichage_grille()

while jeu != 45:

    var_ligne = 0
    var_colo = 0
    var_eu = 0

# entrée de ligne
    while var_ligne != True:
        en_ligne = input("Dans quelle ligne voulez vous jouer ? ")
        try:
            #On vérifie que c'est un entier
            en_ligne = int(en_ligne)
            #On verifie qu'il est entre 1 et 9
            if (verif_valeur(en_ligne)):
                var_ligne = True
        except ValueError:
            print("Ce n'est pas un entier!")

# entrée de colonne
    while var_colo != True:
        en_colonne = input("Dans quelle colonne voulez vous jouer ? ")
        try:
            #On vérifie que c'est un entier
            en_colonne = int(en_colonne)
            #On verifie qu'il est entre 1 et 9
            if verif_valeur(en_colonne):
                var_colo = True
        except ValueError:
            print("Ce n'est pas un entier!")

# entrée de l'utilisateur
    while var_eu != True:
        en_utilisateur = input("Quelle valeur voulez vous entrez ? ")
        print("")
        try:
            #On vérifie que c'est un entier
            en_utilisateur = int(en_utilisateur)
            #On verifie qu'il est entre 1 et 9
            if (verif_valeur(en_utilisateur)):
                var_eu = True
        except ValueError:
            print("Ce n'est pas un entier!")

# Vérification que l'utilisateur essai de modifier une valeur qui n'est pas une des valeurs données au départ de la grille
    if verif_colonne() == verif_ligne() == True :

        if grille2[en_ligne - 1][en_colonne - 1] == 0 and grille1[en_ligne - 1][en_colonne - 1] == 0:
            jeu = jeu + 1
            del grille1[en_ligne - 1][en_colonne - 1]
            grille1[en_ligne - 1 ].insert(en_colonne - 1, en_utilisateur)
            print("Vous avez ajouté une valeur")
            print("")
            affichage_grille()

        elif grille2[en_ligne - 1][en_colonne - 1] != 0:
            print("Vous ne pouvez pas modifier cette valeur, elle vous est donnée dès le début")

        elif grille1[en_ligne - 1][en_colonne - 1] != 0 and grille2[en_ligne - 1][en_colonne - 1] == 0:
            grille1[en_ligne - 1][en_colonne - 1] = en_utilisateur
            print("Vous avez modifié une valeur")
            print("")
            affichage_grille()



