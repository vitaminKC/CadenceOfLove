init python: 
    class Cadence():
        def __init__(self, affection, money):
            self.affection = affection
            self.money = money

        # Used to get current affection
        def getAffection(self):
            return self.affection

        # Used to get current money
        def getMoney(self):
            return self.money

        # Add default affection for positive choices
        def addAffection(self):
            self.affection += 10

        # Subtract default affection for negative choices
        def subAffection(self):
            self.affection -= 10

        # Add money (used in minigame)
        def addMoney(self, amount):
            self.money += amount

        # Subtract money (used in shop)
        def subMoney(self, amount):
            self.money -= amount

    