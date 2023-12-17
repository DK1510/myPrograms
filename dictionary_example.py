#l = [('dhoni', 12), ('kholi', 111), ('raina', 100),('dhoni',120),('kholi',100),('dhoni',112),('dhoni',112)]
l1 = [('dhoni', 12), ('kholi', 111),('dhoni', 12), ('kholi', 111),('dhoni', 12), ('kholi', 111),('kholi', 111),('kholi', 110)]
d = {}

for name,run in l1:

    if name in d.keys():
        d[name].append(run) #existing key
    else:
        d[name] = [run] #new pair
print(d)
for name,run in l1:

    try:
        d[name].append(run)  # existing key
    except KeyError:
        d[name] = [run]  # new pair
print(d)

