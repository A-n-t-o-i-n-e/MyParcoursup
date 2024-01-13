# main 

from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)



def voeux(data):
    """
    la taille de data est de 13000 formations, cette fonction permet de réduire la taille de data
    qui est un nombre de formations, a 20 formations, a l'aide de différentes paramètres tel que ce que la personne aime : 
    
    Questionnaire en 3 parties :
    
    Partie 1 : selection des 10 voeux
    - domaine
    - ce que la personne aime

    Partie 2 : selection des 20 sous-voeux

    - poublic ou privé
    - durée du cursus
    - mode de formation : en alternance ou non
    - zone géographique
    
    Partie 3 : selection des options liées aux formations
    - centre intéret
    - en rapport avec le domaine
    """
    pass