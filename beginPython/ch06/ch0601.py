def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        # print(names)
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            # print(label)
            # print(name)
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


# storge = {}
# init(storge)
# print(storge)
# print(lookup(storge, 'middle', ''))
# me = 'Ma Lie Het'
# storge['first']['Ma'] = [me]
# storge['middle']['Lie'] = [me]
# storge['last']['Het'] = [me]
# print(lookup(storge, 'middle', 'Lie'))


MyNames = {}
init(MyNames)
store(MyNames,'Mag Lie Het')
print(lookup(MyNames,'middle','Lie'))

store(MyNames,'Robin Hood','Robin Hood','Robin Hood')
store(MyNames,'Robin Locksley')
print(lookup(MyNames,'first','Robin'))


store(MyNames,'Mr. Gumby')
print(lookup(MyNames,'middle',''))
