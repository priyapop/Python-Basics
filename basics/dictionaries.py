# phonebook = {
#     'Ricky':'+45 42322 3222',
#     'tommy':'+45 43432 3242',
#     'klaus':'+45 42332 3252'
# }
# #add more items
# phonebook['erik'] = '+22 56888 3443'

# print(phonebook)
# number = phonebook['erik']
# print(f'clling erik....({number})')


player = {
    'Name' : 'Erik',
    'Class':'Warrior',
    'Health':100,
    'level' :1,
    'Backpack':[]
}
#Modify Stats 
player['level'] += 1

#Add items
player['Backpack'].append('Item-a')
player['Backpack'].append('Item-b')
player['Backpack'].append('Item-c')
player['Backpack'].append([10,20,30])

for k,v in player.items():
    print(k,v)