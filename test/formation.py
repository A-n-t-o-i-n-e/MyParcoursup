from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)


def GetFormation(data):
    list_ = []
    for veaux in data:
        if veaux['form_lib_voe_acc'] not in list_:
            list_.append(veaux['form_lib_voe_acc'])
    list_.sort()
    return list_


with open('formation.json',  'w') as fp:
    dump(GetFormation(data), fp, sort_keys=True, indent=2)