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



# Start screen for minigame
screen dust_game_menu():
    add Solid("#000000")
    add "bg minigame.png":
        xpos (1280 - 720) // 2
        ypos 0
        xsize 720
        ysize 720
        

# Minigame screen
screen dust_game():
    # Minigame background 
    add Solid("#000000")
    add "bg minigame.png":
        xpos (1280 - 720) // 2
        ypos 0
        xsize 720
        ysize 720

    # Player movement
    key "K_UP" action Function(try_move_player, 0, -1)
    key "K_DOWN" action Function(try_move_player, 0, 1)
    key "K_LEFT" action Function(try_move_player, -1, 0)
    key "K_RIGHT" action Function(try_move_player, 1, 0)

    # Spawns dust 
    add "minigame dust.png":
        xpos (1280 - 720) // 2 + dust.x * cell_size
        ypos dust.y * cell_size
        xsize cell_size
        ysize cell_size

    # Spawns player 
    add "minigame mc.png":
        xpos (1280 - 720) // 2 + player.x * cell_size
        ypos player.y * cell_size - cell_size
        xsize 90
        ysize 180

    # Displays game score
    text "Points: [dust_collected]":
        xpos 500
        ypos 40 
        size 20
        color "#ffdefb"

    # Timer
    timer 1.0 repeat True action Function(decrement_timer)
    timer game_time action Jump ("EndWork")

    # Displays time    
    text "Time: [game_time]":
        xpos 500
        ypos 70 
        size 20
        color "#ffdefb"
    

# Shop screen
screen shop():
    add Solid("#f9dcf6")

    add "shop shop.png":
        xpos 620
        ypos 50
        xanchor 0.5

    add "shop cart.png":
        xpos 40
        ypos 500

    #Next button
    imagebutton:
        xpos 1010
        ypos 500
        idle "shop next.png"
        action Jump ("EndShop")


    # Item buttons to buy and text descriptions
    imagebutton:
        xpos 160
        ypos 170
        idle "shop teddy.png"
        action Function(player_items.buy_teddy)

    text "Teddy Bear: $30":
        xpos 220
        ypos 450 
        size 20
        color "#000000"


    imagebutton:
        xpos 480
        ypos 170
        idle "shop choco.png"
        action Function(player_items.buy_choco)

    text "Chocolates: $50":
        xpos 550
        ypos 450 
        size 20
        color "#000000"


    imagebutton:
        xpos 800
        ypos 170
        idle "shop flower.png"
        action Function(player_items.buy_flowers)

    text "Flowers: $70":
        xpos 855
        ypos 450 
        size 20
        color "#000000"
    