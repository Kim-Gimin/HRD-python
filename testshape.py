from shape.circle import Circle
from shape.rectangle import Rectangle


def print_area(shape):
    if type(shape) == Rectangle:
        s = "rectangle diagonal"
        s += f"{shape.get_diagonal():.2f}"
    elif type(shape) == Circle:
         s = "circle circumference"
         s += f"{shape.get_circumference():.2f}"
    else :
         pass
    print(s, "area:", shape.area())

shapes = [
     Rectangle(10, 10, 5, 20), Circle(50, 50, 5), Rectangle(0, 0, 100, 5), Rectangle(50, 50, 5, 20)
]

for shape in shapes:
     print_area(shape)