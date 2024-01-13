from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)


def get_all_formation(data, parametre = 'form_lib_voe_acc'):
    list_ = []
    for veaux in data:
        if veaux[parametre] not in list_:
            list_.append(veaux[parametre])
    list_.sort()
    return list_

print(get_all_formation(data, 'fili'))
"""with open('formation.json',  'w') as fp:
    dump(get_all_formation(data), fp, sort_keys=True, indent=2)"""