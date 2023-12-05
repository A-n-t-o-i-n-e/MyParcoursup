# main 

from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)

def questionaire():
    """
    Cette fonction permet de poser des questions a la personne qui utilise le programme, afin de lui proposer des formations qui lui correspondent.

    Returns:
        dict: Un dictionnaire contenant les réponses de la personne, sous la forme suivante :
        {
            "domaine": "Informatique", #
            "region": "Nouvelle-Aquitaine",
            "contrat_etab": "Public",
            "filiere": "Informatique",  # fil_lib_voe_acc
            "specialite": "Informatique",  # form_lib_voe_acc
            "taux_reussite": 0.8,  # taux_acces_ens
            "taille": "Moyenne",  # nb_cla_pp, nb_voe_pp
            "duree": "Courte",  # capa_fin
            "proximite": "Proche",  # ville_etab
            "autre": "Internat"  # acc_internat
        }
    """
    pass

def voeux(data, questionnaire = questionaire()):
    """
    la taille de data est de 13000 formations, cette fonction permet de réduire la taille de data
    qui est un nombre de formations, a 20 formations, a l'aide de différentes paramètres tel que ce que la personne aime : 
    
    Quesrtionnaire en 3 parties :
    
    Partie 1 : selection des 10 voeux
    - le domaine
    - poublic ou privé
    - durée du cursus
    - mode de formation : en alternance ou non

    Partie 2 : selection des 20 sous-voeux
    - zone géographique
    
    Partie 3 : selection des options liées aux formations
    - centre intéret
    - en rapport avec le domaine
    """
    pass