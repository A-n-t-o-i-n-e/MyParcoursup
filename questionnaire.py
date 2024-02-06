import questions

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
    user_response = []
    user_response.append(questions.domaine())
    user_response.append(questions.duree_etude())
    user_response.append(questions.alternance())
    user_response.append(questions.dans_lycee())


def traitement_voeux(resultat_questionaire_voeux, _traitement_voeux):
    """
    Attribue une note a chaque filiere de 0 a 4 
    pour faire un classement des filières et seletionneé les 10 premières filières.
    
    Arguements : 
    - _traitement_voeux : liste de toutes les filières avec d'autres info(traitement-voeux.json)
    exemple:
    {"fili" :"Année préparatoire", "domaine" : "Education_et_Formation", "duree_etude" : "0-2", "alternance" : false, "lycee" : false},
    
    - resultat_questionaire_voeux
    exemple:
    [
        ["Sciences_et_Technologies", "Education_et_Formation"],
        ["0-2", "3-5", "5+"],
        [False],
        [False]
    ]
    Retourne :
    - liste de 10 voeux (filiere)
    exemple:
    [
        'CUPGE - Sciences, technologie, santé', 
        'Licence - Sciences - technologies - santé', 
        'Année préparatoire', 
        'Formation des écoles de commerce et de management', 
        "Formation des écoles supérieure d'art", 
        'Formation des écoles supérieures de cuisine', 
        'Formation professionnelle', 
        'Formation valant grade de licence', 
        'Mention complémentaire', 
        'Mise à niveau'
    ]
    """
    filieres_notees = {filiere["fili"] : 0 for filiere in _traitement_voeux}

    key = ["domaine", "duree_etude", "alternance", "lycee"]
    
    # parcours des filiere 
    for i_filiere, filiere in enumerate(_traitement_voeux):
        for i_res_q in range(len(resultat_questionaire_voeux)):
            #parcours des domaines des resultats
            for i_domaine, domaine in enumerate(resultat_questionaire_voeux[i_res_q]):
                if filiere[key[i_res_q]] == domaine:  # le res du user est dans la filiere parcouru
                    filieres_notees[filiere['fili']] += 1 - i_domaine / len(resultat_questionaire_voeux[i_res_q])
    return sorted(filieres_notees, key=filieres_notees.get, reverse=True)[:10]
            

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
