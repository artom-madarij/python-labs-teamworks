class Lamp:

    def __init__(self, types=None, power=None, diode=None, producer=None, model=None, price=None):
        self.__types = types
        self.__power = power
        self.__diode = diode
        self.__producer = producer
        self.model = model
        self.price = price

    def get_types(self):
        return self.__types

    def get_power(self):
        return self.__power

    def get_diode(self):
        return self.__diode

    def get_producer(self):
        return self.__producer

    def __str__(self):
        return f"Тип: {self.__types} \nПотужність: {self.__power} \nКількість діодів: {self.__diode} \nВиробник: {self.__producer}"

    def __repr__(self):
        return (f'Тип: {self.__types} '
                f'\nПотужність: {self.__power}'
                f'\nКількість діодів: {self.__diode} '
                f'\nВиробник: {self.__producer} '
                f'\nЦіна: {self.price} грн'
                f'\nМодель: {self.model}\n ')
    def __del__(self):
        print(f"{self.__str__()} \ndel\n")



def main():
    lamp1 = Lamp('Розжарювання', 4, 3, "LED FILAMENT", 'g45', 14)
    print('Lamp1:\n',repr(lamp1))
    lamp2 = Lamp('Галогенка', 5, 3)
    print('Lamp2:\n', repr(lamp2))
    lamp3 = Lamp()
    print('Lamp1:\n',repr(lamp1))
    print('Lamp3:\n', repr(lamp3))
main()
