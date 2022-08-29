# we learn about if, elif, else

myName = str(input('what is your name ')).strip( ).lower()
assert (len(myName) > 1)
if myName == 'george':
    print(f'your name is {myName}')
# elif myName == 'andrei':
#     print(f'*'*50)
# elif myName == 'paula':
#     print(f'_'*100)
# # assert len(myName) == 5
# else:
#     print(f'we expected George, but we got {myName}')


# myAge = int(input('what is your age? '))
# if myAge == 30:
#     print(f'your age is {myAge}')
# else:
#     print('you are too young')
#
#     print('you are too young')
# acelasi lucru cu ce e mai sus, intr-o singura linie

# print(f'{myAge}') if myAge >18 else print('you are too young')

# if myAge < 2 and myAge < 5:
#     print(f'the human is too young')
# elif myAge > 2 and myAge <5:
#     print(f'you are younger')

# if myAge == 0:
#     print('your age can\'t be 0 ' )
# elif 1 <= myAge <= 14:
#     print('you are minor')
# elif 15 <= myAge < 18:
#     print('you are younger')
# else:
#     print('you are major')

isCursed = 'summer'
if isCursed != 'summer':
    pass
else:
    print('you are not coursed')


#what is teh price? input si int
# daca e par - printam 'the price is even
# daca e impar 'the price is odd
# len.imput >1 <11 = assert

'''
o variabila careia ii atribuim o valoare random intre s2 si 200 si sa o printam
'''
# ce e pylint si sa instalam