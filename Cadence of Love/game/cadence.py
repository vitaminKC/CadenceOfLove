class Cadence():
    def __init__(self):
        self.affection = 50
        self.money = 0

    def addAffection(self):
        self.affection += 10

    def subAffection(self):
        self.affection -= 10

    def addMoney(self, amount):
        self.money += amount

    def subMoney(self, amount):
        self.money -= amount

    