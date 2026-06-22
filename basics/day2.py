# user = 'rita'
# print(f'hello {user}')

#  calculator addition

# str_num_a = input('enter 1st no:')
# str_num_b = input('enter 2nd no:')

# num_a = int(str_num_a)
# num_b = int(str_num_b)

# total = num_a + num_b
# print(total)

#lists
my_list = ['people','leg','arm','nose','hair','man','woman','eye','arm']
# print(my_list[2])
# print(my_list[2:]) #get from 2nd inc
# print(my_list[:2]) #get until 2nd excluding
# print(my_list[1:3]) #get from first ic until third excluding
# print(my_list[::2]) #every 2nd item
# print(my_list[2:6:2])#get every 2nd item from 2nd inc until 6th exc
# print(my_list[::-1]) #rev
list_two = ['life','death']
# my_list.append('boot')#add single item
# my_list += ['time']
# my_list.extend(list_two)#join two list
my_list.sort() #sort alphabetically

# print(my_list.count('hair')) count items 

print(my_list.index('arm')) #rn working on sorted list
print(my_list)

# tuple ()
# sets unique
first = {'hello','goodbye','meow'}
print(set(my_list))