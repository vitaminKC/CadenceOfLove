label StartWork:
    $ game_time = 30
    show screen dust_game_menu
    $ renpy.pause() 

label WorkDay:
    $ player = Player(3, 3)
    $ dust = Dust(0, 0)
    $ dust.respawn(grid_size, grid_size, player)
    $ dust_collected = 0

    call screen dust_game

label EndWork:
    hide screen dust_game_menu
    with fade
    # scene bg classroom 
    # with fade

    $ cadence.addMoney(dust_collected)
    "Good work! You earned $[dust_collected]"

    $ day += 1

    if day == 1:
        jump date1

    if day == 2: 
        jump date2
    
    if day == 3: 
        jump graduation
    