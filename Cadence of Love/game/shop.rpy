
init:
    # Combines the stats screen and shop screens into a single screen
    screen combined_screens:
        use shop
        use StatsUI


label shop: 
    # Player starts with no items
    $ player_items = Items(0, 0, 0)

    # Shows shop screen
    call screen combined_screens
    $ renpy.pause()


label EndShop:
    # Summary of shop experience
    "You bought [player_items.flowers] flower(s), [player_items.choco] chocolate(s), and [player_items.teddy] teddy bear(s)."
    "Your affection is now [cadence.getAffection()]."

    # Continues with the story where they left off
    if day == 1:
        jump date1

    if day == 2: 
        jump date2
    
    if day == 3: 
        jump graduation
    