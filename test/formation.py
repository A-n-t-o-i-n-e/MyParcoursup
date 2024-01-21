from json import load, dumps

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)


def get_all_formation(data, parametre = 'form_lib_voe_acc'):
    list_ = []
    for veaux in data:
        if veaux[parametre] not in list_:
            list_.append(veaux[parametre])
    list_.sort()
    return list_

def get_but(data):
    for voeux in data:
        if voeux['fil_lib_voe_acc']  == 'Informatique' and voeux['fili']  == 'BUT'and voeux['dep'] == '33':
            print(dumps(voeux, indent=2))

def get_fil_lib_voe_acc_of_form_lib_voe_acc(data, parametre = 'BUT - Production'):
    list_ = []
    for veaux in data:
        if (veaux['fil_lib_voe_acc'] not in list_) and veaux['form_lib_voe_acc'] == parametre:
            list_.append(veaux['fil_lib_voe_acc'])
    list_.sort()
    return list_


# mis en forme des données
print(
    dumps(
        get_fil_lib_voe_acc_of_form_lib_voe_acc(data, "Classe préparatoire scientifique"), 
        indent=2
    ),
    len(get_fil_lib_voe_acc_of_form_lib_voe_acc(data, "Classe préparatoire scientifique"))
)

"""with open('formation.json',  'w') as fp:
    dump(get_all_formation(data), fp, sort_keys=True, indent=2)"""
