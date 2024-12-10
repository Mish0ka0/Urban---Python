from math import pi, sqrt


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.__color = []
        self.__sides = []
        if len(color) <= 3:
            for col in color:
                self.__color.append(col)
        if len(sides) == self.sides_count:
            for side in sides:
                self.__sides.append(side)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            if not self.__color:
                for i in (r, g, b):
                    self.__color.append(i)
            else:
                self.__color.clear()
                for i in (r, g, b):
                    self.__color.append(i)

    def __is_valid_sides(self, *new_sides):
        a = 0
        for side in new_sides:
            if isinstance(side, int) and side > 0:
                a += 1
        return a == len(new_sides) and a == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for side in self.__sides:
            p += side
        return p

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *radius):
        super().__init__(color, *radius)
        self.__radius = round(radius[0] / (2 * pi), 2)

    def get_square(self):
        return round(pi * pow(self.__radius, 2), 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self.get_sides()
        p = 0.5 * sum(a)
        return sqrt(p * (p - a[0]) * (p - a[1]) * (p - a[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) > 1:
            a = [1] * self.sides_count
        else:
            a = [*sides] * self.sides_count
        super().__init__(color, *a)

    def get_volume(self):
        a = self.get_sides()
        return pow(a[0], 3)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((232, 123, 213), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
