from random import choice


class Charity:
    CHARITIES = {}

    def __init__(self):
        key = choice(Charity.CHARITIES.keys())
        self.to_number = key
        self.code = Charity.CHARITIES[key]
