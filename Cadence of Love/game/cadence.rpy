init python: 
    class Cadence():
        def __init__(self, affection, money):
            self.affection = affection
            self.money = money

        def getAffection(self):
            return self.affection

        def getMoney(self):
            return self.money

        def addAffection(self):
            self.affection += 10

        def subAffection(self):
            self.affection -= 10

        def addMoney(self, amount):
            self.money += amount

        def subMoney(self, amount):
            self.money -= amount

    