import random


class Coin:
    def __init__(self) -> None:
        self.throw()

    def side(self) -> str:
        return self.side

    def throw(self) -> None:
        self.side = random.choice(['1', '0'])


coin_flip = Coin()

print(coin_flip.side)
coin_flip.throw()
print(coin_flip.side)

coin_flip2 = Coin()
print(coin_flip2.side)
coin_flip.throw()
print(coin_flip2.side)

coin_flip3 = Coin()
print(coin_flip3.side)
coin_flip.throw()
print(coin_flip3.side)
