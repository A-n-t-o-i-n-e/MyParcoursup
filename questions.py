def domaine():
    dom =['Education_et_Formation', 'Sciences_de_la_Santé', 'Sciences_et_Technologies', 'Droit_et_Gestion', 'Arts_et_Lettres', 'Sciences_Humaines_et_Sociales', None]
    domaine_output = []
    for _ in range(3):
        print("Choix :", domaine_output)
        print("Choisissez un domaine :")
        for i in range(1, len(dom)+1):
            print(i, dom[i-1])
        domaine_input = int(input("Entrez le numéro correspondant à votre choix : "))
        domaine_output.append(dom.pop(domaine_input-1))

    return domaine_output

def duree_etude():
    etude = ['0-2', '3-5', '5+']
    etude_output = []
    for _ in range(3): ######## Faire que 2 vu que dernier obligatoire 
        print("Choix :", etude_output)
        print("\nChoisissez une durée préférée pour le cours :")
        for i in range(1, len(etude)+1):
            print(i, etude[i-1])
        duree_etude_input = int(input("Entrez le numéro correspondant à votre choix : "))
        etude_output.append(etude.pop(duree_etude_input-1))
    
    return etude_output

def alternance():
    print("\nÊtes-vous intéressé par l'alternance entre études et travail ?")
    print("1. Oui")
    print("2. Non")
    alternance_input = input("Entrez le numéro correspondant à votre choix : ")
    mapping_alternance = {"1": True, "2": False}
    return [mapping_alternance.get(alternance_input)]

def dans_lycee():
    print("\nÊtes-vous intéressé pour la continuité dans un lycée ?")
    print("1. Oui")
    print("2. Non")
    lycee_input = input("Entrez le numéro correspondant à votre choix : ")
    mapping_lycee = {"1": True, "2": False}
    return [mapping_lycee.get(lycee_input)]
