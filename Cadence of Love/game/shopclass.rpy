init python:
    class Items():
        def __init__(self, teddy, flowers, choco):
            self.teddy = teddy
            self.flowers = flowers
            self.choco = choco

        def buy_teddy(self):
            if cadence.getMoney() >= 15:
                self.teddy += 1
                cadence.subMoney(15)

        def buy_flowers(self):
            if cadence.getMoney() >= 35:
                self.flowers += 1
                cadence.subMoney(35)

        def buy_choco(self):
            if cadence.getMoney() >= 25:
                self.choco += 1
                cadence.subMoney(25)
            
        def reset_items(self):
            self.teddy = 0
            self.flowers = 0
            self.choco = 0

        def shop_affection(self):
            return (self.teddy*15 + self.flowers*35 + self.choco*25)
