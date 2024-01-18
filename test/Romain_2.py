from json import load
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
    Domaine_ = []
    Duree_ = []
    for _ in range(3):
        Domaine_.append(questions.domaine())
        Duree_.append(questions.duree_etude_input())
    user_response.append()
    
    print("\nÊtes-vous intéressé par l'alternance entre études et travail ?")
    print("1. Oui")
    print("2. Non")
    alternance_input = input("Entrez le numéro correspondant à votre choix : ")
    mapping_alternance = {"1": True, "2": False}
    
    mapping_domaine = {"1": "Education_et_Formation", "2":"Sciences_de_la_Santé", "3":"Sciences_et_Technologies", "4":"Droit_et_Gestion", "5":"Arts_et_Lettres", "6":"Sciences_Humaines_et_Sociales"}
    mapping_duree = {"1": "0-2", "2": "3-5", "3": "5+"}
    





questionaire_voeux()
with open('traitement-voeux.json') as fp:
        donnees = load(fp)
liste = []
for i in range(len(donnees)):
    if donnees[i].get("domaine") ==  '':
        liste.append(donnees[i])
print(liste)




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
    
    for filiere in traitement_voeux:
        #complete 
        pass
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
