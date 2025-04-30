init python:
    class Items():
        def __init__(self, teddy, flowers, choco):
            self.teddy = teddy
            self.flowers = flowers
            self.choco = choco

        # Buys a teddy bear for $30 and adds affection
        def buy_teddy(self):
            if cadence.getMoney() >= 30:
                self.teddy += 1
                cadence.subMoney(30)
                cadence.addAffection()
                "Your affection went up by 10!"

        # Buys flowers for $70 and adds affection
        def buy_flowers(self):
            if cadence.getMoney() >= 65:
                self.flowers += 1
                cadence.subMoney(65)
                cadence.addAffection()
                cadence.addAffection()
                cadence.addAffection()
                "Your affection went up by 30!"

        # Buys chocolates for $50 and adds affection
        def buy_choco(self):
            if cadence.getMoney() >= 50:
                self.choco += 1
                cadence.subMoney(50)
                cadence.addAffection()
                cadence.addAffection()
                "Your affection went up by 20!"
        
        # Resets items in inventory after affection is gained
        def reset_items(self):
            self.teddy = 0
            self.flowers = 0
            self.choco = 0


