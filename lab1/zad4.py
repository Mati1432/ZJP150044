import statistics


class Stat:
    stat_list: list[float]

    def __init__(self, stat_list: list[float]):
        self.stat_list = stat_list

    def list_sum(self) -> float:
        return sum(self.stat_list)

    def mean(self) -> float:
        return self.list_sum() / len(self.stat_list)

    def median(self) -> float:
        return statistics.median(self.stat_list)

    def min(self) -> float:
        return min(self.stat_list)

    def max(self) -> float:
        return max(self.stat_list)


stat1 = Stat([11, 22, 33, 44, 55, 66, 77, 88, 99, ])
print(stat1.list_sum())
print(stat1.mean())
print(stat1.median())
print(stat1.min())
print(stat1.max())
