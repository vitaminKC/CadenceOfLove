## Stats UI
screen StatsUI:
    frame:
        xalign 0.9
        yalign 0.1
        xpadding 10
        ypadding 10

        hbox:
            spacing 20
            # Text Column
            vbox:
                spacing 10
                text "Affection" size 20
                text "Money" size 20

            # Values Column     
            vbox:    
                spacing 10
                text "[cadence.getAffection()]" size 20
                text "[cadence.getMoney()]" size 20



screen dust_game_menu():

    add Solid("#000000")
    add "images/bg minigame.png":
        xpos (1280 - 720) // 2
        ypos 0
        xsize 720
        ysize 720


    imagebutton:
        idle "minigame start.png"
        hover "minigame start.png"
        action Start(label="WorkDay")
        xpos 480
        ypos 290
        xsize 50
        ysize 50
        xanchor 0.5
        


screen dust_game():
    # Minigame background 
    add Solid("#000000")
    add "images/bg minigame.png":
        xpos (1280 - 720) // 2
        ypos 0
        xsize 720
        ysize 720

    # Player movement
    key "K_UP" action Function(try_move_player, 0, -1)
    key "K_DOWN" action Function(try_move_player, 0, 1)
    key "K_LEFT" action Function(try_move_player, -1, 0)
    key "K_RIGHT" action Function(try_move_player, 1, 0)

    # Dust 
    add "images/minigame dust.png":
        xpos (1280 - 720) // 2 + dust.x * cell_size
        ypos dust.y * cell_size
        xsize cell_size
        ysize cell_size

    # Player 
    add "images/minigame mc.png":
        xpos (1280 - 720) // 2 + player.x * cell_size
        ypos player.y * cell_size
        xsize 49
        ysize cell_size


    text "Points: [dust_collected]":
        xpos 500
        ypos 40 
        size 20
        color "#ffdefb"

    timer 1.0 repeat True action Function(decrement_timer)
    timer game_time action Jump ("EndWork")
        
    text "Time: [game_time]":
        xpos 500
        ypos 70 
        size 20
        color "#ffdefb"
    


