class Vehicle:
    def __init__(self, owner,__model, __color,__engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, __model):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет:  {self.__color}")

    def print_info(self):
        print(f" Модель: {self.__model}\n Мощность двигателя: {self.__engine_power}\n Цвет:  {self.__color}\n"
              f" Владелец: {self.owner}")

    def set_color(self, new_color):
      #  new_color = str(new_color)
        for i in self.__COLOR_VARIANTS:
            if i.lower() == new_color.lower():
                self.__color = new_color
                break
            else:
                continue
        if self.__color != new_color:
            print(f" Нельзя сменить цвет на {new_color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()