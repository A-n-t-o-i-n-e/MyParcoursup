def questionaire_voeux():
    """
    Pour chaque question, trie les formations choisis par ordre de préférence 
    

    Retourne la liste des résultats du questionnaire:
    - max 3 domaines
    - duree etude
    - alternance 
    - dans un lycee 

    Exemple de retour :
    [
        ["D.E secteur sanitaire", "DEUST", None],
        ["0-2", "3-5", "5+"],
        [True],
        [False]
    ]
    """
    pass


def traitement_voeux(resultat_questionaire_voeux, traitement_voeux):
    """
    Attribue une note a chaque filiere de 0 a 1 
    pour faire un classement des filières et seletionneé les 10 premières filières.
    
    Exemple:
    

    Arguements : 
    - filieres : liste de toutes les filières (filieres.json)
    Retourne :
    - liste de 10 voeux (filiere)
    """
    filieres_notees = {filiere["fili"] : 0 for filiere in traitement_voeux}

    key = ["fili", "domaine", "duree_etude", "alternance", "lycee"]
    
    # parcours des filiere 
    for i_filiere, filiere in enumerate(traitement_voeux):
        #parcours des domaines des resultats
        for i_domaine, domaine in enumerate(resultat_questionaire_voeux[0]):
            if filiere['domaine'] == domaine:  # le res du user est dans la filiere parcouru
                filieres_notees[filiere['fili']] = 1 - i_domaine / len(resultat_questionaire_voeux[0])
        # parcours des duree_etude des resultats
        for i_duree_etude, duree_etude in enumerate(resultat_questionaire_voeux[1 ]):

    return filieres_notees
            

def questionaire_sous_voeux():
    """
    Arguements : 
    - formations : liste de toutes les formations (fr-esr-parcoursup.json)
    - voeux_selectionnes : liste de 10 voeux (filieres)
    Retourne :
    - liste de 20 sous-voeux (formations)
    """
    pass


def traitement_sous_voeux(formations, voeux_selectionnes, resultat_questionaire_sous_voeux):
    """
    Arguements : 
    - formations : liste de toutes les formations (fr-esr-parcoursup.json)
    - voeux_selectionnes : liste de 10 voeux (filieres)
    Retourne :
    - liste de 20 sous-voeux (formations)
    """
    pass