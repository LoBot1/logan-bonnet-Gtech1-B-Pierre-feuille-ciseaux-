#DEBUT 
from random import randint

def game(pseudoj1,pseudoj2):

    #assigner a joueur_1_coup un input de parametre ("Choisissez un chiffre:\n0: pierre = 1\n1: feuille = 2 \n2: ciseaux = 3 \n-> ") en int 
    pseudoj1 = (int(input( pseudoj1 +" Choisissez un chiffre:\n0: pierre = 0\n1: feuille = 1 \n2: ciseaux = 2 \n-> ")))
    if pseudoj2 != "bot":
        #assigner a joueur_2_coup un input de parametre ("Choisissez un chiffre:\n0: pierre = 1\n1: feuille = 2 \n2: ciseaux = 3 \n-> ") en int  
        pseudoj2 = (int(input(pseudoj2+ " Choisissez un chiffre:\n0: pierre = 0\n1: feuille = 1 \n2: ciseaux = 2 \n-> ")))
    #sinon si le retour de l'execution du retour de l'execution de la fonction joueurAdverse est egale a 1 
    else:
        pseudoj2 = choixOrdinateur()
        #alors renvoyer le retour de l'execution de la fonction choixOrdinateur (nom de la fonction choixRandom)
        print(pseudoj2)
    
    # initialiser Points_joueur_1_coup egale a 0 
    Points_joueur_1_coup = 0
        # initialiser Points_joueur_2_coup egale a 0 
    Points_joueur_2_coup = 0

    #si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a pierre  
    if pseudoj1 == 0 and pseudoj2 == 0:
        #renvoyer la valeur str "egalité"
        print("égalité")

    #sinon si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a ciseaux
    elif pseudoj1 == 0 and pseudoj2 == 2 :
        #iterer 1 a Points_joueur_1_coup
        Points_joueur_1_coup = Points_joueur_1_coup + 1 
        #renvoyer la valeur str "joueur_1 gagnant"
        print ( "joueur1 gagnant")

    #sinon si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a feuille
    elif pseudoj1 == 0 and pseudoj2 == 1 :
        #iterer 1 a Points_joueur_2_coup
        Points_joueur_2_coup = Points_joueur_2_coup + 1  
        #renvoyer la valeur str "joueur_2 gagnan"
        print("joueur_2 gagnant") 


    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a pierre
    elif pseudoj1 == 1 and pseudoj2 == 0 :
        #iterer 1 a Points_joueur_1_coup
        Points_joueur_1_coup = Points_joueur_1_coup + 1 
        #renvoyer la valeur str "joueur_1 gagnant"
        print("joueur_1 gagnant")

    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a ciseaux
    elif pseudoj1 == 1 and pseudoj2 == 2:
        #iterer 1 a Points_joueur_2_coup
        Points_joueur_2_coup = Points_joueur_2_coup + 1  
        #renvoyer la valeur str "joueur_2 gagnant"
        print("joueur_2 gagnant") 

    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a feuille
    elif pseudoj1 == 1 and pseudoj2 == 1:
        #renvoyer la valeur str "egalité"
        print("égalité")

    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a pierre
    elif pseudoj1 == 2 and pseudoj2 == 0:
        #iterer 1 a Points_joueur_2_coup
        Points_joueur_2_coup = Points_joueur_2_coup + 1  
        #renvoyer la valeur str "joueur_2 gagnant"
        print("joueur_2 gagnant") 

    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a ciseaux
    elif pseudoj1 == 2 and pseudoj2 == 2 :
        #renvoyer la valeur str "egalité"
        print("égalité")

    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a feuille
    elif pseudoj1 == 2 and pseudoj2 == 1 :
        #iterer 1 a Points_joueur_1_coup
        Points_joueur_1_coup = Points_joueur_1_coup + 1 
        #renvoyer la valeur str "joueur_1 gagnant"
        print("joueur_1 gagnant")
    else :
        print('erreur')

#definir une fonction game de parametre joueur_1_coup, joueur_2_coup 



#initialiser choixRegle a 0 
choixRegle = 0
#definir une fonction Regle de parametre x  
def Regle ():
    #alors renvoyer "la pierre gagne contre le ciseaux mais perd contre la feuille /n le ciseaux gagne contre la feuille mais perd contre la pierre /n la feuille gagne contre la pierre mais perd contre le ciseaux"
    print("la pierre gagne contre le ciseaux mais perd contre la feuille \nle ciseaux gagne contre la feuille mais perd contre la pierre \nla feuille gagne contre la pierre mais perd contre le ciseaux")

  
#initialiser joueur_2 egal a 0 
joueur_2 = 0 
#initialiser bot egal a 1 
bot = 1

#definir une fonction joueurAdverse qui prend pour parametre joueur_2 et bot 
def joueurAdverse():
    #initialisé choixJoueurAdverse egale a un int input de parametre ("tu veux un joueur 2 mon copin ou(0=J2 1= bot): ")
    choixJoueurAdverse = (int(input("tu veux un joueur 2 mon copin ou(0=J2 1= bot): ")))
    #si choixJoueurAdverse equivalent a 0 
    if choixJoueurAdverse == 0:
        #initialisé pseudo egal a un input de parametre (input('votre pseudo : '))
        pseudo = (input('votre pseudo : '))
        #Alors renvoyer pseudo  
        return pseudo

    #sinon si choixJoueurAdverse equivalent a 1
    elif choixJoueurAdverse == 1:
        #initialisé pseudo egale "bot"
        pseudo = "bot" 
        #Alors renvoyer pseudo 
        return pseudo 
    game()

def choixOrdinateur():

    ordi = randint(0,2)
    print(ordi)
    
def menu():

    choix = int(input("Indiquer votre choix (1 pour Regle et 2 pour lancé la partie ): " ))
    if choix == 1:
        Regle()
    elif choix == 2:
        pseudoj1 = (input("votre pseudoj1 : "))
        game(pseudoj1,pseudoj2=joueurAdverse())
menu()







