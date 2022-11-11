#DEBUT 
#initialiser la pierre egal a 1 
#initialiser la feuille  egal a 2 
#initialiser le ciseaux egal a 3

# initialiser Points_joueur_1_coup egale a 0 
# initialiser Points_joueur_2_coup egale a 0 
#definir une fonction game de parametre joueur_1_coup, joueur_2_coup 
    #si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a pierre  
        #renvoyer la valeur str "egalité"
    #sinon si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a ciseaux
        #renvoyer la valeur str "joueur_1 gagnant"
        #iterer 1 a Points_joueur_1_coup
    #sinon si le joueur_1_coup est egal pierre et si le joueur_2_coup est egal a feuille
        #renvoyer la valeur str "joueur_2 gagnant"
        #iterer 1 a Points_joueur_2_coup
    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a pierre
        #renvoyer la valeur str "joueur_1 gagnant"
        #iterer 1 a Points_joueur_1_coup
    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a ciseaux
        #renvoyer la valeur str "joueur_2 gagnant"
        #iterer 1 a Points_joueur_2_coup
    #sinon si le joueur_1_coup est egal feuille et si le joueur_2_coup est egal a feuille
        #renvoyer la valeur str "egalité"
    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a pierre
        #renvoyer la valeur str "joueur_2 gagnant"
        #iterer 1 a Points_joueur_2_coup
    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a ciseaux
        #renvoyer la valeur str "egalité"
    #sinon si le joueur_1_coup est egal ciseaux et si le joueur_2_coup est egal a feuille
        #renvoyer la valeur str "joueur_1 gagnant"
        #iterer 1 a Points_joueur_1_coup


#initialiser choixRegle a 0 
#definir une fonction Regle de parametre x  
    #assigner a choixRegle un input de parametre "voullez vous les regles (1=Oui et 0=Non)" 
    #si choixRegle equivalent a 1
        #alors renvoyer "la pierre gagne contre le ciseaux mais perd contre la feuille /n le ciseaux gagne contre la feuille mais perd contre la pierre /n la feuille gagne contre la pierre mais perd contre le ciseaux"
    #sinon si choixRegle est different de 1 ou 0 
        #alors renvoyer "le choix se limite a 1 pour avoir les regle et 0 pour ne pas les avoirs"
        #renvoyer la fonction Regle


#definir une fonction pseudoJoueur qui prend pour parametre pseudo
    #Assigner a pseudo le retour de l'execution de la fonction joueurAdverse pour lui assigner un pseudo 



#initialiser joueur_2 egal a 0 
#initialiser bot egal a 1 
#definir une fonction joueurAdverse qui prend pour parametre joueur_2 et bot 
    #si joueur_2 equivalent a 0 
        #Alors renvoyer le retour de l'execution de la fonction pseudoJoueur 
    #sinon si bot equivalent a 1
        #Alors renvoyer le retour de la fonction pseudoJoueur qui aura pour parametre le pseudo "bot"

# definir une fonction CoupLancé de parametre joueur_1_coup, joueur_2_coup 
    #assigner a joueur_1_coup un input de parametre ("Choisissez un chiffre:\n0: pierre = 1\n1: feuille = 2 \n2: ciseaux = 3 \n-> ") en int 
    #si le retour de l'execution du retour de l'execution de la fonction joueurAdverse est egale a 0 
        #assigner a joueur_2_coup un input de parametre ("Choisissez un chiffre:\n0: pierre = 1\n1: feuille = 2 \n2: ciseaux = 3 \n-> ") en int  
    #sinon si le retour de l'execution du retour de l'execution de la fonction joueurAdverse est egale a 1 
        #alors renvoyer le retour de l'execution de la fonction choixOrdinateur (nom de la fonction choixRandom)
#renvoyer le retour de l'execution de la fonction game 
        









