from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)

def GetFormation(data):
    list_ = []
    for voeux in data:
        if not voeux['form_lib_voe_acc'] in list_:
            list_.append(voeux['form_lib_voe_acc'])
    list_.sort()
    return list_
#print(GetFormation(data))

def GetAcademie(data):
    list_ = []
    for voeux in data:
        if not voeux['acad_mies'] in list_:
            list_.append(voeux['acad_mies'])
    list_.sort()
    return list_
#print(GetAcademie(data))

# Fonction to get formation by academie
def GetFormationByAcademie(data, academie):
    list_ = []
    for voeux in data:
        if voeux['acad_mies'] == academie:
            list_.append(voeux['form_lib_voe_acc'])
    list_.sort()
    return list_
#print(GetFormationByAcademie(data, 'Aix-Marseille'))


import re

def get_categories(formation):
  """
  Renvoie une liste de catégories pour une formation.

  Args:
    formation: Le nom de la formation.

  Returns:
    Une liste de catégories.
  """

  categories = []

  # Niveau d'études

  if re.match(r"(Année préparatoire|BTS|BUT|CPGE|CUPGE|DE|DN MADE|Licence|LP|DCG|DEUST|DJE\w+|CPES|FCIL|Licence professionnelle|Licence valant grade de licence|Mention complémentaire|Mise à niveau)", formation):
    categories.append("Niveau d'études")

  # Domaine d'études

  if re.match(r"(Arts|Droit|Economie|Gestion|Sciences|Technologies|Santé|Sciences humaines et sociales)", formation):
    categories.append("Domaine d'études")

  # Secteur d'activité

  if re.match(r"(Agricole|Maritime|Production|Services|Sanitaire et social|Commerce et distribution|Restauration|Construction|Informatique|Technologies de l'information et de la communication|Santé|Social|Enseignement|Recherche)", formation):
    categories.append("Secteur d'activité")

  # Discipline

  if re.match(r"(Lettres|Langues|Histoire|Géographie|Philosophie|Sciences humaines|Sociologie|Economie|Gestion|Mathématiques|Physique|Chimie|Biologie|Sciences de la santé|Droit|Sciences politiques|Communication|Marketing|Commerce|Hôtellerie|Restauration|Informatique|Technologies de l'information et de la communication|Génie civil|Architecture|Ingénierie|Santé|Social|Enseignement|Recherche)", formation):
    categories.append("Discipline")

  return categories


formations = ["Année préparatoire", "BPJEPS", "BTS - Agricole", "BTS - Maritime", "BTS - Production", "BTS - Services", "BUT - Production", "BUT - Service", "C.M.I - Cursus Master en Ingénieurie", "CPES", "CUPGE - Arts Lettres Langues", "CUPGE - Droit-Économie-Gestion", "CUPGE - Sciences, technologie, santé", "Cadre Technique", "Certificat de Spécification Agricole", "Classe préparatoire aux Études Supérieures", "Classe préparatoire Littéraire", "Classe préparatoire Scientifique", "Classe préparatoire Économique et Commerciale", "D.E secteur sanitaire", "D.E secteur social", "DCG", "DEJEPS", "DEUST", "DN MADE", "Diplôme National d'Art", "Diplôme d'Etablissement", "Diplôme d'Université", "Diplôme d'Établissement", "FCIL", "Formation des Écoles de Commerce et de Management", "Formation des Écoles Supérieures d'Art", "Formation des Écoles Supérieures de Cuisine", "Formation professionnelle", "Formation valant grade de licence", "Formations  des Écoles d'Ingénieurs", "Formations Bac + 3", "Formations Bac + 5", "Formations des Écoles Vétérinaires", "LP - Sciences Humaines et Sociales", "LP - Droit-Économie-Gestion", "LP - Sciences - Technologies - Santé", "Licence - Arts-Lettres-Langues", "Licence - Arts-Lettres-Langues / Sciences humaines et sociales", "Licence - Droit-Économie-Gestion", "Licence - Droit-Économie-Gestion / Arts-Lettres-Langues", "Licence - Droit-Économie-Gestion / Sciences - Technologies - Santé", "Licence - Droit-Économie-Gestion / Sciences humaines et sociales", "Licence - STAPS", "Licence - Sciences - Technologies - Santé", "Licence - Sciences humaines et sociales", "Mention complémentaire", "Mise à niveau", "Sciences politiques"]

categories = []
for formation in formations:
  categories.append(get_categories(formation))

print(categories)



