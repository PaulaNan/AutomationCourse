class imported_class:
    def __init__(self, colour:str, maker:str):
        self.colour = colour
        self.maker = maker
        self.phone = self.custom_print()

    def custom_print(self):
        print(f'The colour is: {self.colour} and the maker is: {self.maker}')
        return 29
    def print_self_default(self):
        print(f'Self default is {self.phone}')