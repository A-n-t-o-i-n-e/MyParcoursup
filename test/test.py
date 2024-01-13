from json import load, dump, dumps

with open('filieres.json', "r", encoding="utf-8") as fp:
    filieres = load(fp)

with open('domaines.json', "r", encoding="utf-8") as fp:
    domaines = load(fp)

resultat_questionaire_voeux = [
    ["Sciences_et_Technologies", "Education_et_Formation"],
    ["0-2", "3-5", "5+"],
    [True],
    [False],
    [False]
]

def traitement_voeux(filieres, resultat_questionaire_voeux, domaines):
    """
    Attribue une note a chaque filiere de 0 a 1 
    pour faire un classement des filières et seletionneé les 10 premières filières.
    
    Exemple:
    

    Arguements : 
    - filieres : liste de toutes les filières (filieres.json)
    Retourne :
    - liste de 10 voeux (filiere)
    """
    filieres_notees = {filiere : 0 for filiere in filieres}

    for i in range(len(resultat_questionaire_voeux[0])):
        for domaine in domaines.keys():
            if resultat_questionaire_voeux[0][i] == domaine:
                for filiere in domaines[domaine]:
                    filieres_notees[filiere] += 1-i/len(resultat_questionaire_voeux[0])
    return filieres_notees

filieres_notees = traitement_voeux(filieres, resultat_questionaire_voeux, domaines)
print(sorted(filieres_notees, key=filieres_notees.get, reverse=True)[:15])





# mis en forme des données
print(
    dumps(
        traitement_voeux(filieres, resultat_questionaire_voeux, domaines), 
        indent=2
    )
)