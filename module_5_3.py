class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

        # операция сравнения
    def __eq__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors == other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция меньше
    def __lt__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors < other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция меньше или равно
    def __le__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors <= other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция больше
    def __gt__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors > other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция больше или равно
    def __ge__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors >= other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция неравенства
    def __ne__(self, other):
        if isinstance(other, House):
            if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
                return self.number_of_floors != other.number_of_floors
        else:
            return f'Сравниваемый объект "{other}" не является объектом класса "House"'

        # операция увеличения
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return f'Значение "{value}" не является целым числом'

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            return f'Значение "{value}" не является целым числом'

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f'Значение "{value}" не является целым числом'

        # операция уменьшения
    def __sub__(self, value):
        if isinstance(value, int):
            if self.number_of_floors > value:
                self.number_of_floors = self.number_of_floors - value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __isub__(self, value):
        if isinstance(value, int):
            if self.number_of_floors > value:
                self.number_of_floors -= value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __rsub__(self, value):
        if isinstance(value, int):
            if self.number_of_floors < value:
                self.number_of_floors = value - self.number_of_floors
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

        # операция умножения
    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors * value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __imul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __rmul__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value * self.number_of_floors
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

        # операция целочисленного деления
    def __floordiv__(self, value):
        if isinstance(value, int):
            if self.number_of_floors > value:
                self.number_of_floors = self.number_of_floors // value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __ifloordiv__(self, value):
        if isinstance(value, int):
            if self.number_of_floors > value:
                self.number_of_floors //= value
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self

    def __rfloordiv__(self, value):
        if isinstance(value, int):
            if value > self.number_of_floors:
                self.number_of_floors = value // self.number_of_floors
            return self
        else:
            print(f'Ошибка! Значение "{value}" не является целым числом')
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
