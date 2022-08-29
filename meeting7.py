'''
create a class named person witch has a method print value for index,
method wich takes an argument called index(int)
inside that method add a list with five int
add a try except and the except sould catch index error toghether
    wich will show the index and the error
add also a cod logic(print) wich will run even 2 to the codewill enter the
print(exception)instantiate the class and call the method
'''
'''
class Person:
    def print_value_for_index(self, index: int):
        integer = [0, 3, 12, 9,17]
        try:
            print(f'Return value from list: {integer[index]}, and the index is {index}')
        except IndexError as index_error:
            # print(f'index: {index}, eroare: {index_error}')
            #raise NotImplementedError(f'index: {index}, eroare: {index_error}')
            # print(f'the value of index {index} is {integer[index]}')
            raise IndexError
        finally:
            print(f'the value of index {index} is {integer[index]}')

person_object = Person()
person_object.print_value_for_index(index=2)
person_object.print_value_for_index(index=10)

'''


# create a class called Person which will have a methods print_hello_world
# which will print hello world
# create another class called Employee which will enharite  from person
# inside the class Employee create a method called print_hello_name (str)
# which will take an argument default_value = mister robot
# initialize the class employee and call the method hello name

# class Person:
#     @staticmethod
#     def print_hello_world():
#         print('Hello world')
#
#
# class Employee(Person):
#     @staticmethod
#     def print_hello_name(name: str = 'mister robot'):
#         print(f'Hello {name}')
#
#
# pharmacist = Employee()
# pharmacist.print_hello_world()
# pharmacist.print_hello_name()
#
#
# class Employee2(Employee):
#     pass
#
#
# engineer = Employee2()
# engineer.print_hello_name(name='Paula')
# engineer.print_hello_world()

# create a class base_page which has another method prin_hello_world
# which will print hello world
# create another class login_page which inherits from base_page and has a method
# print_hello_world. Inside the method we will prin Hello universe
# initiate login_page and call the method

# class BasePage:
#     def print_hello_world(self):
#         print('Hello world')
#
#
# class LoginPage(BasePage):
#     def print_hello_world(self):
#         print('Hello universe')
#
# page = LoginPage()
# page.print_hello_world()


# create a class called BasePage and add one method called print_hello_world
# which must be implemented in all child classes
# create a class called SettingsPage which enharits from BasePage
# inside the Settings create a method that will bring the sum of 2 arg
# initiate class and call the method

# from abc import ABC, abstractmethod
# class BasePage(ABC):
#     @abstractmethod
#     def print_hello_world(self):
#         raise NotImplementedError('method is not implemented')
#
#
# class SettingsPage(BasePage):
#     def print_sum(self, number1, number2):
#         total = int(number1) + int(number2)
#         print(f'suma este: {total} ')
#
#     def print_hello_world(self):
#         print('world')
#
# sum_number = SettingsPage()
# sum_number.print_sum(number1=5, number2=6)

# encapsulation
class Car:
    __running = False
    __model = 'Toyota'

    def set_running_state(self, state):
        self.__running = state

    def set_model(self, model):
        self.__model = model

    def get_running_state(self):
        return self.__running

    def get_model(self):
        return self.__model

    def __find_number(self):
        return 0

    def get_number(self):
        print(self.__find_number())

obj_car  = Car



# tema
# definitii la oop ce e incapsulation, inharitance, polimorfism
# create a class Person, inside add respect patern __is_alive si __hair
# 4 method set colour self.__colour (set si get)
# instantiate and call the method
# set,, get..

class Person:
    __is_alive = True
    __hair = 'brown'

    def set_is_alive(self, state):
        self.__is_alive = state

    def set_hair(self, hair):
        self.__hair = hair

    def get_is_alive(self):
        return self.__is_alive

    def get_hair(self):
        return self.__hair

info_person = Person()
info_person.set_hair(hair='red')
info_person.set_is_alive(False)
info_person.get_hair()
info_person.get_is_alive()