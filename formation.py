from json import load, dump

with open('fr-esr-parcoursup.json') as fp:
    data = load(fp)

# with open('fr-esr-parcoursup.json',  'w') as fp:
#     dump(data, fp, sort_keys=True, indent=2)

def GetFormation(data):
    list_ = []
    for veaux in data:
        if not veaux['form_lib_voe_acc'] in list_:
            list_.append(veaux['form_lib_voe_acc'])
    list_.sort()
    return list_
print(GetFormation(data))

with open('formation.json',  'w') as fp:
    dump(GetFormation(data), fp, sort_keys=True, indent=2)