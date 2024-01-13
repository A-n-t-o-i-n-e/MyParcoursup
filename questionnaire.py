def questionaire_voeux():
    """
    Pour chaque question, trie les formations choisis par ordre de préférence 
    

    Retourne la liste des résultats du questionnaire:
    - max 5 domaines
    - duree etude
    - alternance 
    - autonome
    - dans un lycee 

    Exemple de retour :
    [
        ["D.E secteur sanitaire", "D.E secteur social", "DCG", "DEJEPS", "DEUST", "DN MADE"],
        ["0-2", "3-5", "5+"],
        True,
        False,
        False
    ]
    """


def traitement_voeux(filieres, resultat_questionaire_voeux):
    """
    Attribue une note a chaque filiere de 0 a 1 
    pour faire un classement des filières et seletionneé les 10 premières filières.
    
    exemple : 
    
    Arguements : 
    - filieres : liste de toutes les filières (filieres.json)
    Retourne :
    - liste de 10 voeux (filiere)
    """


def questionaire_sous_voeux():
    """
    Arguements : 
    - formations : liste de toutes les formations (fr-esr-parcoursup.json)
    - voeux_selectionnes : liste de 10 voeux (filieres)
    Retourne :
    - liste de 20 sous-voeux (formations)
    """


def traitement_sous_voeux(formations, voeux_selectionnes, resultat_questionaire_sous_voeux):
    """
    Arguements : 
    - formations : liste de toutes les formations (fr-esr-parcoursup.json)
    - voeux_selectionnes : liste de 10 voeux (filieres)
    Retourne :
    - liste de 20 sous-voeux (formations)
    """