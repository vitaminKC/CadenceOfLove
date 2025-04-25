
init:
    screen combined_screens:
        use shop
        use StatsUI


label shop: 
    $ player_items = Items(0, 0, 0)
    call screen combined_screens
    $ renpy.pause()


label EndShop:
    "You bought [player_items.flowers] flowers, [player_items.choco] chocolates, and [player_items.teddy] teddy bears"
    "Your affection went up by [player_items.shop_affection()]"


    # $ cadence.addAffection(player_items.shop_affection())
    $ player_items = (0, 0, 0)

    if day == 1:
        jump date1

    if day == 2: 
        jump date2
    
    if day == 3: 
        jump graduation
    