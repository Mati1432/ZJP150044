import gc


class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name, self.last_name}'


person = Person('James', 'Bond')
person2 = Person('Bond', 'James')

for obj in gc.get_objects():
    if isinstance(obj, Person):
        print(obj)
