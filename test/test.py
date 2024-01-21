from json import load, dump, dumps

with open('traitement-voeux.json', "r", encoding="utf-8") as fp:
    _traitement_voeux = load(fp)


resultat_questionaire_voeux = [
    ["Sciences_et_Technologies", "Education_et_Formation"],
    ["0-2", "3-5", "5+"],
    [False],
    [False]
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

    key = ["fili", "domaine", "duree_etude", "alternance", "lycee"]
    
    # parcours des filiere 
    for i_filiere, filiere in enumerate(_traitement_voeux):
        #parcours des domaines des resultats
        for i_domaine, domaine in enumerate(resultat_questionaire_voeux[0]):
            if filiere['domaine'] == domaine:  # le res du user est dans la filiere parcouru
                filieres_notees[filiere['fili']] += 1 - i_domaine / len(resultat_questionaire_voeux[0])
        # parcours des duree_etude des resultats
        for i_duree_etude, duree_etude in enumerate(resultat_questionaire_voeux[1]):
            if filiere['duree_etude'] == duree_etude:
                filieres_notees[filiere['fili']] += 1 - i_duree_etude / len(resultat_questionaire_voeux[1])
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