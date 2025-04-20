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
                text "[affection]" size 20
                text "[money]" size 20