# create list with 5 items and print each one = for each - e pt lista diversa
# my_list = ['house', 5, 6.18, 'table', 10]
# for i in my_list:
#     print(f'{i}')

# print no 1 to 5
# for i in range(1,6):
#     print(i)

# create a list with 3 items, one of it is "goup 16" - string
#add conditional statement that the variable is = 'group 16' print...
# cool_list = ['group 16', 'face', 4,15, True]
# for course in cool_list:
#     print(type(course), (course))
#     if course == 'group 16':
#         print('well done')

# create a dictionary one is 'group' and one is '16'
# if key= 'group' and value = '16' - print... else print...

first_dict = {
    'group' :'16',
    'car':'red',
    'class' : '15'
}
for i, y in first_dict.items():
    print(f' I is {i} and y is {y}')  #var 1
#  print(first_dict[i])
if i == 'group'and y == 16:  # var 2
       print('passed')
       pass
     # print(i)
     # print('ok')
else:
     print('fail')

'''
# create a tuple with 5 items
# print iterator and value
my_tuple = ('Andrei', 5, 14.3, 'university', -20)
for i in range(len(my_tuple)):  #var 1
    print(f'index {i} and value is {my_tuple[i]}')
for index, value in enumerate(my_tuple):
    print(f'index {index} and value {value}')   # var 2
'''
'''
# create a blank list and add numbers until 99
# for each itteration print add content and content of the list
my_list = []
for number in range(1, 100):
#    print(number)
    my_list.append(number)
    print(f' {number}, and {my_list}')
'''
'''
# create a set with 5 items and print index and item and if the len.set is 5 exit loop
# end of the loop = print 'out of the loop'
my_set = {'Andrei', 5, 14.3, 'university', -20, 7, 6}
for item, value in enumerate(my_set):
    if item ==5:
#    if len(my_set) == 5:
        break
    print(f' index de {item} is value  {value}')
# if index =5 sa faca brake
else:
    print('out of the loop')
'''

# print a numer for  2 to 150 with while loop
# i= 2
# while i < 151:
#     print(i)
#     i += 1

# 5 items on the list string with my last name
# if item = name - continue, else print...., else print 'in loop'

the_list = [3, 4, 'Nicu', 6, 7]
for name in the_list:
    if name == 'Nicu':
        continue
    else:
        print(name)
    print('in loop')

# in a list add fibonacy sequals until 1000 and print the list
