# creata c class which has 2 class atributes and 3 constructors atributes
# class atribute 1 = model, 2 = manufacturer
#  constructor var 1 = engine, 2 = colour, 3 = is running
#  create a method which sets a model and manufacturer
#  create another method which prints both model and manufacturer
#  encapsulation


class Car:
    __model = 'Rav 4'
    __manufacturer = 'Toyota'

    def __init__(self, engine, colour, is_running):
        self.engine = engine
        self.colour = colour
        self.is_running = is_running

    def set_new_model(self, model):
        self.__model = model

    def set_creator(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_model_creator(self):
        print(f'The model is {self.__model} and the manufacturer is {self.__manufacturer}')

my_car = Car(engine='Eco', colour='blue', is_running= True)
my_car.get_model_creator()
my_car.set_new_model(model='Rav 6')
my_car.set_creator(manufacturer='Suzuki')
my_car.get_model_creator()







