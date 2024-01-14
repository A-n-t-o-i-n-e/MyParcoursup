from json import load, dump, dumps

with open('traitement-voeux.json', "r", encoding="utf-8") as fp:
    _traitement_voeux = load(fp)


resultat_questionaire_voeux = [
    ["Sciences_et_Technologies", "Education_et_Formation"],
    ["0-2", "3-5", "5+"],
    [False],
    [False]
]

def traitement_voeux(resultat_questionnaire_voeux, traitement_voeux):
    """
    Attribue une note à chaque filière de 0 à 1 pour faire un classement des filières et sélectionner les 10 premières filières.

    Arguments :
    - resultat_questionnaire_voeux : liste des réponses au questionnaire de voeux
    - traitement_voeux : liste de toutes les filières (filieres.json)

    Retourne :
    - liste des 10 voeux (filière)
    """
    filieres_notees = {filiere["fili"]: 0 for filiere in traitement_voeux}

    key = ["domaine", "duree_etude", "alternance", "lycee"]

    for filiere in traitement_voeux:
        for key_index, value in enumerate(resultat_questionnaire_voeux):
            if filiere[key[key_index]] == value:
                filieres_notees[filiere["fili"]] += 1

    # Trie les filières par note de manière décroissante
    filieres_triees = sorted(filieres_notees.items(), key=lambda x: x[1], reverse=True)

    # Sélectionne les 10 premières filières
    voeux_selectionnes = [filiere[0] for filiere in filieres_triees[:10]]

    # Retourne la liste des 10 voeux sélectionnés
    return voeux_selectionnes

filieres_notees = traitement_voeux(resultat_questionaire_voeux, _traitement_voeux)
print(sorted(filieres_notees, key=filieres_notees.get, reverse=True)[:15])





# mis en forme des données
print(
    dumps(
        traitement_voeux(resultat_questionaire_voeux, traitement_voeux), 
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