# create a class and print hello world
#
# class Group16:
#     print('Hello world!')
# object = Group16()

# create a class named Person with class var "color, state'and instance var "wallet - float
# compromised - boloean'. Instantiante the class
'''
class Person:
    color: str
    state: bool
    #wallet: float
    #compromise: bool
#color = ''
#state = False
    def __int__(self, wallet: float, compromise: bool):
        self.wallet = wallet
        self.compromise = compromise
wallet = 100
compromise = False
object2 = Person()
'''

# create class employee with 2 class var color(str), state(bool)
# create 2 metods witch print class var# and call each method
# instantiete the class and call each method
'''
class Employee:
    color = 'blue'
    state = True

    def print_color(self):
        print(f'The color is {self.color}')
    def print_state(self):
        print(f'The state is {self.state}')
object3 = Employee()
object3.print_color()
object3.print_state()
# in loc de self se poate pune numele clasei Employee
'''
# create a class base page, add 3 class var
# is displayed:True, is default: False, default tineout: 3000
# add 2 instante var called no of tries and no of users
# add method to print each class in each instance var = 5 methods
# instantiate class and all methods
# instantiate the same class in another obj and call the methods
'''
class Base_Page:
    is_displayed: bool = True
    is_default: bool = False
    default_timeout: int = 3000

    def __init__(self, number_of_tries:int, number_of_user:int):
        self.number_of_tries = number_of_tries
        self. number_of_user = number_of_user

    def custom_print(self, variable, value):
        print(f'The value of variable {variable} is: {value}')

    def print_is_displayed(self):
        #print(f'The base page is: {self.is_displayed}')
        #self.custom_print(variable= 'paula', value=56)
        self.custom_print(variable='is_displayed', value=self.is_displayed)

    def print_is_default(self):
        print(f'The default page is: {self.is_default}')

    def print_default_timeout(self):
        print(f'The default page is: {self.default_timeout}')

    def print_number_tries(self):
        print(f'The number of tries is: {self.number_of_tries}')

    def print_number_of_user(self):
        print(f'The number of user is: {self.number_of_user}')


class_base_page = Base_Page(number_of_tries=3, number_of_user=1)
class_base_page.print_default_timeout()
class_base_page.print_is_default()
class_base_page.print_is_displayed()
class_base_page.print_number_of_user()
class_base_page.print_number_tries()

another_object = Base_Page(number_of_tries=5, number_of_user=2)
another_object.print_number_tries()
another_object.print_number_of_user()
another_object.print_is_displayed()
another_object.print_is_default()
another_object.print_default_timeout()
'''

# create a new py file colour class_imported_from_file
# create a class called imported_class inside the new created file
# add inside the class 2 var caller and maker
# add one method inside the class witch will print the 2 var inside the same line
# import the class into meeting6_oop
# instantiate the class and call the method

from class_imported_from_file import imported_class

# cream obiect/instantiate
# var_1 = imported_class(colour='red', maker='Andrei')
# var_1.print_self_default()
# call the method
# var_1.custom_print()
# var_2 = imported_class(colour='blue', maker='Mia')
# var_2.custom_print()

# repositori in github
# cretae a branch group_16
# file named homework sesion 6
# add comenturi - what is bondary testing
# 2. what is echivalent partition in testing
# create a pull request: read the file added
# hint: how to create a github repro, a branch,
# cli, source tree
# link catre pull request

