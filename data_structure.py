# colours = [] # list
# colours_2 = {} # dictionary
# colours_3 = set() #set
# colours_4 = () # tuple
# print(type(colours))
# print(type(colours_2))
# print(type(colours_3))
# print(type(colours_4))

'''
variabila = list # daca punem acum paranteze () le printeaza asa cum sunt, nu conteaza ce tip de paranteze pui
variabila_2 = dict
variabila_3 = set
variabila_4 = tuple
print(variabila)
print(variabila_2)
print(variabila_3)
print(variabila_4)
print(type(variabila()))
'''

# my_group_is_awesome = ['car', 12, True, 12.22]
# print(my_group_is_awesome)

# var_with_5_words = [True, False, 12, 155.21, 'group', None]
# print(var_with_5_words[-1])
# print(var_with_5_words[::-1])
#:: step

# my_list = []
# print(my_list)
# my_list.append(12)
# my_list.append('Maria')
# print(my_list)
# append adauga in lista NUMAI 1 element pe rand

# another_list = [None, 4, 'Mircea', 'Ion', 14.2]
# print(another_list)
# another_list.pop() # pop sterge ultimul element din lista daca nu e trecut altceva
# print(another_list)
# another_list.pop(0)
# print(another_list) # sterge elementul cu index 0

# sample_list = [6, 3, True, 'Maia', 3, True, 0, 6, True, 12, 'Maia']
# print(sample_list.count(True))

# new_list = ['canto', 44]
# print(new_list[0])
# new_list [1] = 'Georgica'
# print(new_list)
# new_list.insert(1, 'horia')
# print(new_list)

# list_2 = [1, True, 'mare', 3, 44, False, 'mare', 3, 'yes', True]
# print(list_2)
# list_2.remove('yes')
# print(list_2)

# my_fruits = ['apple', 'grape', 'pear']
# my_vegetable = ['cucumber', 'zuchini', 'tomato']
# my_fruits.extend(my_vegetable)
# print(my_fruits)
# my_fruits.reverse()
# print(my_fruits)
# print(my_fruits[::-1]) # daca pui :-1 scoate ultimul element
# ::-1 reverse la lista

# dict1 = {
#     'name':'Paula',
#     'age': '22',
#     'hair':'blue'
# }
# print(dict1)
# print(type(dict1))
# print(dict1.keys())
# print(dict1.values())
# print(dict1['name'])

# dict_2 = {
#     'age':'21',
#     'name':'Paula'
# }
# print(dict_2.get('namee', 45)) # get - daca cheia nu este gasita, printeaza ce apare dupa , - un fel de if
# print(dict_2.setdefault('name', '45')) # default -daca nu exista adauga in dictionar, nu da eroare daca nu exista
# print(dict_2)

# my_set = {'ball', 12, 'one'}
# my_set.add('banana') # un set nu poate adauga aceeasi valoare
# my_set.add(12)
# print(type(my_set))
# print(my_set)
# #my_set.clear()
# print(my_set)
# my_set_2 = {12, 17,1}
# print(my_set.difference(my_set_2))

'''
tema
sa facem un set sa scoatem un item din set fara eroare
mai facem un set (variabila). copiem valorile primului set in set 2 si print set 2
se da un string cu min 10 caractere, convertiti-l in tuple
se da un tuple cu integer si float min 5, printam minim si max si suma
'''

one_tuple = ('one', 'four', 17, 'four') # aflam la ce index e o valoare
print(one_tuple.index('four')) # il vede doar pe primul de la stg la dr
two_tuple = (2, 17,2.14)
merged_tuple = one_tuple + two_tuple
print(merged_tuple)
