label StartWork:
    # Total game time
    $ game_time = 30

    # Displays the starting screen and instructions for the game
    show screen dust_game_menu
    "Use arrow keys to move around and clean up the dust and earn money to buy gifts for Cadence. \nClick to start"

label WorkDay:
    # Spawns the player and dust on the screen
    $ player = Player(3, 3)
    $ dust = Dust(0, 0)
    $ dust.respawn(grid_size, grid_size, player)
    $ dust_collected = 0

    # Displays the screen for the minigame
    show screen dust_game
    call screen dust_game

label EndWork:
    # Changes screen
    hide screen dust_game_menu
    scene black

    # Adding money based off score
    $ cadence.addMoney(dust_collected)
    "Good work! You earned $[dust_collected]"

    $ day += 1

    jump shop
    