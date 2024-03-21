from json import load, dump, dumps

with open('traitement-voeux.json', "r", encoding="utf-8") as fp:
    _traitement_voeux = load(fp)


resultat_questionaire_voeux = [
    ["Sciences_et_Technologies"],
    ["5+", "3-5", "0-2"],
    [False],
    [True]
]

def traitement_voeux(resultat_questionaire_voeux, _traitement_voeux):
    """
    Attribue une note a chaque filiere de 0 a 1 
    pour faire un classement des filières et seletionneé les 10 premières filières.
    
    Exemple:
    

    Arguements : 
    - filieres : liste de toutes les filières (filieres.json)
    Retourne : 
    - liste de 10 voeux (filiere)
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
    return filieres_notees

filieres_notees = traitement_voeux(resultat_questionaire_voeux, _traitement_voeux)
print(sorted(filieres_notees, key=filieres_notees.get, reverse=True)[:15])





# mis en forme des données
print(
    dumps(
        dict(sorted(filieres_notees.items(), key=lambda item: item[1], reverse=True)), 
        indent=2
    )
)


"""
for i in range(len(resultat_questionaire_voeux[0])):
        for domaine in domaines.keys():
            if resultat_questionaire_voeux[0][i] == domaine:
                for filiere in domaines[domaine]:
                    filieres_notees[filiere] += 1-i/len(resultat_questionaire_voeux[0])
"""