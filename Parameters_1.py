# create a function to print 'Hello World'
# def hello_world():
#     print('Hello world')
# hello_world()

# create a function who is taking a parameter ' user' and to print 'hello user'
# def name(user):
#     print(f'Hello {user}')
# name('nicu')

# create a function with parameter user and age
# make an asert user = name and age >18
# print 'we expected ..., but we got....
# def expected_user_age(user, age):
#     assert user == 'George', f' expected George, and actual is {user}'
#     assert age > 18 , f'  expected 18, but actual is {age}'
# expected_user_age('George', 17)

# create a function with 3 parameters: user, age, hair
# age default 25, print user is, age is, hair is
# call function
# change age 35

# def user_age_hair(user, hair, age=25):
#     print(f'user is {user}, age is {hair}, hair is {age}')
# user_age_hair('Paula', 'grey')
# user_age_hair('Paula', 'grey', 35)

#create a function with 3 parameters/arguments int
# return sum  and print
'''
def sum_3_no(no1, no2, no3):
    my_list = [no1, no2, no3]
    for number in my_list:
        assert isinstance(number, int), f'expected {number} to be an int, actual is {type(number)}'
    # assert isinstance(no1,int), f'expected no1 to be an int, actual is {type(no1)}'
    # assert isinstance(no2, int), f'expected no2 to be an int actual is {type(no2)}'
    # assert isinstance(no3, int), f'expected no3 to be an int actual is {type(no3)}'
    sum = no1+no2+no3
    return sum

print(sum_3_no(3, 4,3))
'''

# create a function with infinite no of arguments
# print each argument

def info(*args):
    print(type(args))
    for i in args:
        print(i)
info(3, 5, 'bianca', [2, 'mia', 8, 'op'])

# create a function with infinite arguments (kwargs **)
# documentam ce face functia = descriere la functie (docstring) si paramentii la kwargs
# pt fiecare parametru adaugam in lista si return la lista
# aceast return este un type list (typehint)
# assert (inainte de return sau dupa logica de function) len list >0






