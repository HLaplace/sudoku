import random
#import time
x = 1
a = 45
g2 = 0
i = -1
l = 0
b = 0
t = 1
q = 1
m = 0
l = 1 
c = 1
p =0
r = 0
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
        c = c + 1
        print("ok colo")
        
    else:
        print("erreur colonne")

#fonction pour verifier que l'entrée de l'utilisateur ne soit pas déja dans la ligne
def verif_ligne():
    global l
    
    tab = [g1[e][0],g1[e][1],g1[e][2],
           g1[e][3],g1[e][4],g1[e][5],
           g1[e][6],g1[e][7],g1[e][8]]
    
    if h != tab:
        l = l + 1
        print("ok ligne")
    else:
        print("erreur ligne")

#Vérification que les valeurs entrée par l'utilisateur son compatible avec le jeu du sudoku
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
    else :
        b = b + 1
        print ("ok user input")
        
#définition d'une grille aléatoire

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
    
#définition de l'entrée de l'utilisateur
j = 0
while j != 36:
    e = input("Dans quelle ligne voulez vous jouer ? ")
    f = input("Dans quelle colone voulez vous jouer ? ")
    e = int(e)
    f = int(f)
    e = e - 1
    f = f - 1
    h = input("Quelle valeur voulez vous entrez ? ")
    verif_userinput()
    verif_colonne()
    verif_ligne() 
    aff()         
#vérification de la validité des carrés à condition que la ligne et la colonne 
#associés à l'entrée de l'utilisateur soit validés ( t= 2 )
    while r != 36:
        if c == l and l == b:
       
#carré 1
            if 0 <= e <= 2 and 0 <= f <= 2:
                tab1 = [g1[0][0],g1[0][1],g1[0][2],
                        g1[1][0],g1[1][1],g1[1][2],
                        g1[2][0],g1[2][1],g1[2][2]]
                if h != tab1:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("cette valeur est déjà dans ce carré")
            
#carré 2       
            if 0 <= e <= 2 and 3 <= f <= 5:
                tab2 = [g1[0][3],g1[0][4],g1[0][5],
                        g1[1][3],g1[1][4],g1[1][5],
                        g1[2][3],g1[2][4],g1[2][5]]
                if h != tab2:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                   print("erreur carré")
            
#carré 3       
            if 0 <= e <= 2 and 6 <= f <= 8:
                tab3 = [g1[0][6],g1[0][7],g1[0][8],
                        g1[1][6],g1[1][7],g1[1][8],
                        g1[2][6],g1[2][7],g1[2][8]]
                if h != tab3:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")
            
#carré 4
            if 3<= e <= 5 and 0 <= f <= 2:
                tab4 = [g1[3][0],g1[3][1],g1[4][2],
                        g1[4][0],g1[4][1],g1[5][2],
                        g1[5][0],g1[5][1],g1[6][2]]
                if h != tab4:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")
            
#carré 5
            if 3<= e <= 5 and 3 <= f <= 5:
                tab5 = [g1[3][3],g1[3][4],g1[3][5],
                        g1[4][3],g1[4][4],g1[4][5],
                        g1[5][3],g1[5][4],g1[5][5]]
                if h != tab5: 
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")
                
#carré 6
            if 3 <= e <= 5 and 6 <= f <= 8:
                tab6 = [g1[3][6],g1[3][7],g1[3][8],
                        g1[4][6],g1[4][7],g1[4][8],
                        g1[5][6],g1[5][7],g1[5][8]]
                if h != tab6:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")
                
#carré 7                
            if 6 <= e <= 8 and 0 <= f <= 2:
                tab7 = [g1[6][0],g1[3][1],g1[3][2],
                        g1[7][0],g1[4][1],g1[4][2],
                        g1[8][0],g1[5][1],g1[5][2]]
                if h != tab7:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")

#carré 8
            if 6 <= e <= 8 and 3 <= f <= 5:
                tab8 = [g1[6][3],g1[3][4],g1[3][5],
                        g1[7][3],g1[4][4],g1[4][5],
                        g1[8][3],g1[5][4],g1[5][5]]
                if h != tab8:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")        

#carré 9
            if 6 <= e <= 8 and 6 <= f <= 8:
                tab8 = [g1[6][6],g1[3][7],g1[3][8],
                        g1[7][6],g1[4][7],g1[4][8],
                        g1[8][6],g1[5][7],g1[5][8]]
                if h != tab8:
                    p = p + 1
                    r = r + 1
                    g1[e][f] = h
                    print("ok carré")
                    aff()
                else:
                    print("erreur carré")              
#fin du jeu 
                    if p == 1:
              
                        if g2[e][f] == 0:
                            j = j + 1
                            p = 0
                            print("Vous avez complétés une case")
           

                        else:
                            print("Vous avez modifiés une valeur que vous aviez précédemment entré")

print("Fini !!")
print("Bien joué !!")
