import random  # importation de la librairie random pour définir aléatoirement une grille

ligne = 0 # boolen utilisé pour la vérification des valeurs de ligne
colone = 0 # boolen utilisé pour la vérification des valeurs de colone
en_ligne = 0 # entrée de ligne du joueur //int_global_input_line
en_colone = 0 # entrée de colone du joueur
en_utilisateur = 0 # valeur que le joueur veux mettre dans la grille
rdm_valeur1 = 0 # valeur aléatoire de ligne utilisé pour définir aléatoirement ma grille
rdm_valeur2 = 0 # valeur aléatoire de colone utilisé pour définir aléatoirement ma grille
rdm = 0 # varialbe aléatoire utilisé pour la définition aléatoire de ma grille
rdm2 = 0 # seconde varialbe aléatoire utilisé pour la définition aléatoire de ma grille
jeu = 0 # variable permettant de suivre l'évolution de l'utilisateur dans le jeu
vttl = 0 # variable utilisé pour la vérification de toutes les lignes
vttc = 0 # variable utilisé pour la vérification de toutes les colones
var_ligne = 0
var_colo = 0
var_eu = 0


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

# Fonction d'affichage formatée de la grille de Sudoku
def affichage_grille():
    print(g1[0][0], "|", g1[0][1], "|", g1[0][2], "||", g1[0][3], "|", g1[0][4], "|", g1[0][5], "||", g1[0][6], "|",
          g1[0][7], "|", g1[0][8])
    print("------------------------------------")
    print(g1[1][0], "|", g1[1][1], "|", g1[1][2], "||", g1[1][3], "|", g1[1][4], "|", g1[1][5], "||", g1[1][6], "|",
          g1[1][7], "|", g1[1][8])
    print("------------------------------------")
    print(g1[2][0], "|", g1[2][1], "|", g1[2][2], "||", g1[2][3], "|", g1[2][4], "|", g1[2][5], "||", g1[2][6], "|",
          g1[2][7], "|", g1[2][8])
    print("------------------------------------")
    print("------------------------------------")
    print(g1[3][0], "|", g1[3][1], "|", g1[3][2], "||", g1[3][3], "|", g1[3][4], "|", g1[3][5], "||", g1[3][6], "|",
          g1[3][7], "|", g1[3][8])
    print("------------------------------------")
    print(g1[4][0], "|", g1[4][1], "|", g1[4][2], "||", g1[4][3], "|", g1[4][4], "|", g1[4][5], "||", g1[4][6], "|",
          g1[4][7], "|", g1[4][8])
    print("------------------------------------")
    print(g1[5][0], "|", g1[5][1], "|", g1[5][2], "||", g1[5][3], "|", g1[5][4], "|", g1[5][5], "||", g1[5][6], "|",
          g1[5][7], "|", g1[5][8])
    print("------------------------------------")
    print("------------------------------------")
    print(g1[6][0], "|", g1[6][1], "|", g1[6][2], "||", g1[6][3], "|", g1[6][4], "|", g1[6][5], "||", g1[6][6], "|",
          g1[6][7], "|", g1[6][8])
    print("------------------------------------")
    print(g1[7][0], "|", g1[7][1], "|", g1[7][2], "||", g1[7][3], "|", g1[7][4], "|", g1[7][5], "||", g1[7][6], "|",
          g1[7][7], "|", g1[7][8])
    print("------------------------------------")
    print(g1[8][0], "|", g1[8][1], "|", g1[8][2], "||", g1[8][3], "|", g1[8][4], "|", g1[8][5], "||", g1[8][6], "|",
          g1[8][7], "|", g1[8][8])
    print("")

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déjà dans la colonne
def verif_colonne():
    global colone
    tab = [g1[0][en_colone], g1[1][en_colone], g1[2][en_colone],
           g1[3][en_colone], g1[4][en_colone], g1[5][en_colone],
           g1[6][en_colone], g1[7][en_colone], g1[8][en_colone]]

    try:
        tab.index(en_utilisateur)
        print("La valeur saisie est déjà dans la colonne")
        print(tab)
        colone = False
    except ValueError:
        # print("La valeur n'est pas déjà dans la colone")
        colone = True
        print("erreur 2")

# fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la  ligne
def verif_ligne():
    global ligne
    tab = [g1[en_ligne][0], g1[en_ligne][1], g1[en_ligne][2],
           g1[en_ligne][3], g1[en_ligne][4], g1[en_ligne][5],
           g1[en_ligne][6], g1[en_ligne][7], g1[en_ligne][8]]

    try:
        tab.index(en_utilisateur)
        print("La valeur saisie est déjà dans la ligne")
        print(tab)
        ligne = False
    except ValueError:
        ligne = True
        print("erreur 1")

# fonction définissant aléatoirement une grille "vide" à patir de g1
def grille_random():
    global rdm
    global g2
    while rdm != 45:
        rdm_valeur1 = random.randint(0, 8)
        rdm_valeur2 = random.randint(0, 8)
        if g1[rdm_valeur1][rdm_valeur2] != 0:
            rdm2 = g1[rdm_valeur1][rdm_valeur2]
            g1[rdm_valeur1][rdm_valeur2] = 0
            rdm = rdm + 1
    print("")
    print("Bonne chance cette grille n'as pas l'air simple: ")
    print("")
    g2 = []  # second tableaux utilisé pour regarder si l'utilisateur ajoute ou modifie une valeur
    for i in range(len(g1)):
        g2.append(g1[i][:])
    affichage_grille()

#fonction utilisée quand la grille est entiérement rempli pour vérifier toutes les lignes
def verif_tt_lignes():
    while vttl != 8:
        if g1[vttl][0] != g1[vttl][1] != g1[vttl][2] != g1[vttl][3] != g1[vttl][4] != g1[vttl][5] != g1[vttl][6] != g1[vttl][7] != g1[vttl][8]:
            print("ok ligne :")
            print(vttl)
            print("")
            vttl = vttl + 1

        else:
            print("erreur ligne")
            print(vttl)
            vttl = vttl + 1

#fonction utilisée quand la grille est entiérement rempli pour vérifier toutes les colones
def verif_tt_colones():
    while vttc != 8:
        if g1[0][vttc] != g1[1][vttc] != g1[2][vttc] != g1[3][vttc] != g1[4][vttc] != g1[5][vttc] != g1[6][vttc] != g1[7][vttc] != g1[8][vttc]:
            print("ok colone :")
            print(vttc)
            print("")
            vttc = vttc + 1

        else:
            print("erreur colone :")
            print(vttc)
            vttc = vttc + 1

#fonction pour définir l'entrée de ligne du joueur
def entre_de_ligne():
    global var_ligne
    while var_ligne != True:
        en_ligne = input("Dans quelle ligne voulez vous jouer ? ")
        try:
            en_ligne = int(en_ligne)
            en_ligne = en_ligne - 1
            var_ligne = True
        except ValueError:
            print("Ce n'est pas un entier!")

#fonction pour définir l'entrée de colonne du joueur
def entre_de_colone():
    global var_colo
    while var_colo != True:
        en_colone = input("Dans quelle colone voulez vous jouer ? ")
        try:
            en_colone = int(en_colone)
            en_colone = en_colone - 1
            var_colo = True
        except ValueError:
            print("Ce n'est pas un entier!")

# fonction pour définir la valeur ajoutée par le joueur
def entre_utilisateur():
    global var_eu
    while var_eu != True:
        en_utilisateur = input("Quelle valeur voulez vous entrez ? ")
        try:
            en_utilisateur = int(en_utilisateur)
            var_eu = True
        except ValueError:
            print("Ce n'est pas un entier!")

#--------------------jeu--------------------

grille_random()
while jeu != 45:

    var_ligne = 0
    var_colo = 0
    var_eu = 0

    entre_de_ligne()
    entre_de_colone()
    entre_utilisateur()
    verif_ligne()
    verif_colonne()
    print(colone)
    print(ligne)

    if colone == ligne and ligne == True:# modifier avec la fonction "boucle"


        if g2[en_ligne][en_colone] == 0 and g1[en_ligne][en_colone] == 0:
            jeu = jeu + 1
            del g1[en_ligne][en_colone]
            g1[en_ligne].insert(en_colone, en_utilisateur)
            print("Vous avez ajouté une valeur")
            affichage_grille()

        elif g2[en_ligne][en_colone] != 0:
            print("vous ne pouvez pas modifier cette valeur, elle vous est donnez dès le début")

        elif g1[en_ligne][en_colone] != 0 and g2[en_ligne][en_colone] == 0:
            g1[en_ligne][en_colone] = en_utilisateur
            print("Vous avez modifié une valeur")
            affichage_grille()

        elif g2[en_ligne][en_colone] != 0 and g1[en_ligne][en_colone] != 0:
            print("vous ne pouvez pas modifié cette valeur")

        else:
            print("erreur 10")
    else:
        print("Désolé mais il semble que l'on est un probléme dans vos entrées")

verif_tt_lignes()
verif_tt_colones()
