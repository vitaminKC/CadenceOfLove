label StartWork:
    $ game_time = 30
    show screen dust_game_menu
    "Use arrow keys to move around and clean up the dust and earn money to buy gifts for Cadence"
    $ renpy.pause() 

label WorkDay:
    $ player = Player(3, 3)
    $ dust = Dust(0, 0)
    $ dust.respawn(grid_size, grid_size, player)
    $ dust_collected = 0
    show screen dust_game
    call screen dust_game

label EndWork:
    hide screen dust_game_menu
    scene black

    $ cadence.addMoney(dust_collected)
    "Good work! You earned $[dust_collected]"

    $ day += 1

    jump shop
    