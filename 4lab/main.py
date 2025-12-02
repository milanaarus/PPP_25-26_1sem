import math

class Shape:
    def area(self):
        raise NotImplementedError('Метод area не запущен')

    def perimeter(self):
        raise NotImplementedError('Метод perimeter не запущен')

    def vertices(self):
        raise NotImplementedError('Метод vertices не запущен')


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = [(x1, y1), (x2, y2), (x3, y3)]

    def area(self):
        a = math.sqrt((self.points[0][0] - self.points[1][0]) ** 2 + (self.points[0][1] - self.points[1][1]) ** 2)
        b = math.sqrt((self.points[1][0] - self.points[2][0]) ** 2 + (self.points[1][1] - self.points[2][1]) ** 2)
        c = math.sqrt((self.points[2][0] - self.points[0][0]) ** 2 + (self.points[2][1] - self.points[0][1]) ** 2)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def perimeter(self):
        a = math.sqrt((self.points[0][0] - self.points[1][0]) ** 2 + (self.points[0][1] - self.points[1][1]) ** 2)
        b = math.sqrt((self.points[1][0] - self.points[2][0]) ** 2 + (self.points[1][1] - self.points[2][1]) ** 2)
        c = math.sqrt((self.points[2][0] - self.points[0][0]) ** 2 + (self.points[2][1] - self.points[0][1]) ** 2)
        return a + b + c

    def vertices(self):
        return 3


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def vertices(self):
        return 4


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.center = (x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def vertices(self):
        return 0  


def main():
    shapes = []
    
    while True:
        user_input = input("Введите фигуру в формате: 'triangle 0 0 1 0 0 1' или 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            break
        
        parts = user_input.split()
        
        try:
            if parts[0] == 'triangle':
                _, x1, y1, x2, y2, x3, y3 = parts
                shapes.append(Triangle(float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)))
            elif parts[0] == 'rectangle':
                _, x1, y1, x2, y2 = parts
                shapes.append(Rectangle(float(x1), float(y1), float(x2), float(y2)))
            elif parts[0] == 'circle':
                _, x, y, radius = parts
                shapes.append(Circle(float(x), float(y), float(radius)))
            else:
                print('Неизвестный тип фигуры.')
                continue
            
            print(f'Фигура добавлена: {parts[0]}')

        except ValueError:
            print('Ошибка: некорректные параметры.')
    
    while True:
        command = input("Введите команду: 'area', 'perimeter', 'vertices' или 'exit' для выхода ")
        if command.lower() == 'exit':
            break
        
        if command == 'area':
            total_area = sum(shape.area() for shape in shapes)
            print(f'Total area: {total_area:.3f}')
        elif command == 'perimeter':
            total_perimeter = sum(shape.perimeter() for shape in shapes)
            print(f'Total perimetr: {total_perimeter:.3f}')
        elif command == 'vertices':
            total_vertices = sum(shape.vertices() for shape in shapes)
            print(f'Total vertices: {total_vertices}')
        else:
            print('Неизвестная команда.')


if __name__ == "__main__":
    main()
