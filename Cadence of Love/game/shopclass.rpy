init python:
    class Items():
        def __init__(self, teddy, flowers, choco):
            self.teddy = teddy
            self.flowers = flowers
            self.choco = choco

        def buy_teddy(self):
            if cadence.getMoney() >= 30:
                self.teddy += 1
                cadence.subMoney(30)
                cadence.addAffection()

        def buy_flowers(self):
            if cadence.getMoney() >= 70:
                self.flowers += 1
                cadence.subMoney(70)
                cadence.addAffection()
                cadence.addAffection()
                cadence.addAffection()

        def buy_choco(self):
            if cadence.getMoney() >= 50:
                self.choco += 1
                cadence.subMoney(50)
                cadence.addAffection()
                cadence.addAffection()
            
        def reset_items(self):
            self.teddy = 0
            self.flowers = 0
            self.choco = 0


