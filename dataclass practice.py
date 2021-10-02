from dataclasses import dataclass, field


@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float

    def __post_init__(self):
        self.sort_index = self.cash


i1 = Investor('John', 45, 20000)
i2 = Investor('Jenny', 35, 12000)

print(i1  i2)
