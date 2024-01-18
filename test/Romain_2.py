from json import load

def charger_donnees():
    with open('fr-esr-parcoursup.json') as fp:
        donnees = load(fp)
    return donnees

def questionnaire():
    print("Bienvenue dans le questionnaire MyParcoursup !")

    print("Choisissez un domaine :")
    print("1. Informatique")
    print("2. Médecine")
    domaine = input("Entrez le numéro correspondant à votre choix : ")

    print("\nChoisissez une région :")
    print("1. Nouvelle-Aquitaine")
    print("2. Île-de-France")
    region = input("Entrez le numéro correspondant à votre choix : ")

    print("\nChoisissez un type de contrat :")
    print("1. Public")
    print("2. Privé")
    contrat = input("Entrez le numéro correspondant à votre choix : ")

    print("\nChoisissez une durée préférée pour le cours :")
    print("1. Courte")
    print("2. Moyenne")
    print("3. Longue")
    duree_etude = input("Entrez le numéro correspondant à votre choix : ")

    print("\nÊtes-vous intéressé par l'alternance entre études et travail ?")
    print("1. Oui")
    print("2. Non")
    alternance = input("Entrez le numéro correspondant à votre choix : ")

    mapping_domaine = {"1": "Informatique", "2": "Médecine"}
    mapping_region = {"1": "Nouvelle-Aquitaine", "2": "Île-de-France"}
    mapping_contrat = {"1": "Public", "2": "Privé"}
    mapping_duree = {"1": "Courte", "2": "Moyenne", "3": "Longue"}
    mapping_alternance = {"1": True, "2": False}

    reponses_utilisateur = {
        "domaine": mapping_domaine.get(domaine),
        "region": mapping_region.get(region),
        "contrat_etab": mapping_contrat.get(contrat),
        "duree_etude": mapping_duree.get(duree_etude),
        "est_alternance": mapping_alternance.get(alternance),
    }

    return reponses_utilisateur

def voeux(donnees, reponses_utilisateur):
    filtre_domaine = [formation for formation in donnees if formation["fil_lib_voe_acc"] == reponses_utilisateur["domaine"]]
    print(f"\nNombre de Vœux après sélection du domaine : {len(filtre_domaine)}")

    filtre_region = [formation for formation in filtre_domaine if formation["region_etab_aff"] == reponses_utilisateur["region"]]
    print(f"Nombre de Vœux après sélection de la région : {len(filtre_region)}")

    filtre_contrat = [formation for formation in filtre_region if formation["contrat_etab"] == reponses_utilisateur["contrat_etab"]]
    print(f"Nombre de Vœux après sélection du type de contrat : {len(filtre_contrat)}")

    filtre_duree = [formation for formation in filtre_contrat if reponses_utilisateur["duree_etude"] in ["Courte", "Moyenne", "Longue"] or
                    (reponses_utilisateur["duree_etude"] == "Courte" and formation["capa_fin"] <= 2) or
                    (reponses_utilisateur["duree_etude"] == "Moyenne" and 2 < formation["capa_fin"] <= 5) or
                    (reponses_utilisateur["duree_etude"] == "Longue" and formation["capa_fin"] > 5)]
    print(f"Nombre de Vœux après sélection de la durée d'étude : {len(filtre_duree)}")

    if reponses_utilisateur["est_alternance"]:
        filtre_alternance = [formation for formation in filtre_duree if formation["acc_brs"] > 0]
    else:
        filtre_alternance = filtre_duree
    print(f"Nombre de Vœux après sélection de l'alternance : {len(filtre_alternance)}")

    return filtre_region

def explorer_voeux(voeux_selectionnes):
    print("\nExploration des Vœux :")
    for index, voeu in enumerate(voeux_selectionnes[:10]):
        print(f"{index + 1}. {voeu['form_lib_voe_acc']} à {voeu['ville_etab']}, {voeu['region_etab_aff']}")

def explorer_sous_voeux(voeu_selectionne):
    print(f"\nExploration des Sous-Vœux pour {voeu_selectionne['form_lib_voe_acc']}")

def consulter_stats(voeux_selectionnes):
    print("\nConsultation des statistiques :")
    print("Placeholder : Afficher les statistiques ici")

def peut_ajouter_plus_de_voeux():
    reponse = input("Voulez-vous ajouter plus de Vœux ? (oui/non) : ")
    return reponse.lower() == 'oui'

def principal():
    ajouter_voeux = True

    while ajouter_voeux:
        reponses_utilisateur = questionnaire()
        voeux_selectionnes = voeux(donnees, reponses_utilisateur)

        print("\nVœux sélectionnés :")
        for voeu in voeux_selectionnes:
            print(
                f"- {voeu['form_lib_voe_acc']} à {voeu['ville_etab']}, {voeu['region_etab_aff']}"
            )

        explorer_voeux(voeux_selectionnes)

        indice_voeu_selectionne = int(input("\nEntrez le numéro du Vœu que vous souhaitez explorer : ")) - 1
        voeu_selectionne = voeux_selectionnes[indice_voeu_selectionne]
        explorer_sous_voeux(voeu_selectionne)

        consulter_stats(voeux_selectionnes)

        ajouter_voeux = peut_ajouter_plus_de_voeux()

if __name__ == "__main__":
    donnees = charger_donnees()
    principal()


