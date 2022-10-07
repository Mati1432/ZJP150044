class Rectangle:
    shorter_side: float
    longer_side: float

    def __init__(self, shorter_side: float, longer_side: float) -> None:
        self.longer_side = longer_side
        self.shorter_side = shorter_side

    def __str__(self) -> str:
        return f'{self.shorter_side, self.longer_side}'

    def surface_area(self) -> float:
        return self.shorter_side * self.longer_side


rectangle = Rectangle(2.5, 3.5)

print(rectangle)
print(rectangle.surface_area())

second_rectangle = Rectangle(3, 4)


def show(rectangle: list[float]):
    print(rectangle.shorter_side, rectangle.longer_side, rectangle.surface_area())


def rectangle_function():
    empty_list = []

    for item in [rectangle, second_rectangle]:
        print(item)
        empty_list.append(item)

    for item in empty_list:
        print(item.surface_area())

    for item in empty_list:
        show(item)


rectangle_function()
