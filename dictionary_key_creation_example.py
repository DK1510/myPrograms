d = [('Dhoni',13),('Kholi',34),('Dhoni',45),('Dhoni',25),('Kholi',67),('Dhoni',50),('Kholi',34),('Dhoni',67),('Rohit',99)]
score = {}

for name,run in d:
    if name not in score.keys():
        score[name] = [run]  # To create new key with list value
    else:
        score[name].append(run)
print(score)

# if 'Dhoni' not in score.keys():
#     score['Dhoni']=[13]   #To create new key with list value









# d = {'name':'kumar','company':'accenture','location':'chennai'}
# print(d.get('name'))    # to get the values
# del d   # To delete a dict
#
# d.clear()   #clear entire dict
# print(d)




# d.pop('location')   #remove item from a dictionary
# print(d)
# d.popitem() #last item will get removed
# print(d)


