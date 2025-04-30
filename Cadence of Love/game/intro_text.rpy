label intro_text: 
    scene bg bedroom
    with fade

    "You received a text from Cadence!"

    show uniform excited_o at smallSize, default_pos

    c "\"hiiiii!\""

    # Text choices
    menu: 
        # Positive choice
        "\"Heyyyyy\"": 
            $ pos = True
            $ cadence.addAffection()
            "Your affection went up by 10!"
            jump introTextChoices
        
        # Neutral choice
        "\"Do you need something?\"":
            $ neut = True
            jump introTextChoices

        # Negative choice
        "Leave her on read.":
            $ neg = True
            $ cadence.subAffection()
            "Your affection went down by 10."
            jump introTextChoices

    label introTextChoices:
        show uniform excited_c at smallSize, default_pos

        # Positive response
        if pos: 
            $ pos = False
            pov "\"Heyyyyy\""
            pov "\"What's up?\""

            show uniform normal_o at smallSize, default_pos

            c "\"nothing muchhhhh\""

            jump introTextCommon

        # Neutral response
        if neut: 
            $ neut = False
            pov "\"Do you need something?\""

            show uniform upset_o at smallSize, default_pos

            c "\"uh no\""

            jump introTextCommon
        
        # Negative response
        if neg: 
            $ neg = False
            "You left her on read."

            show uniform angry_o at smallSize, default_pos

            c "\"ill c u tmrw ig\""

            jump StartWork

    label introTextCommon:
        show uniform normal_o at smallSize, default_pos

        c "\"js wanted to check in on you since you were zoning out the entire day\""

        show uniform normal_c at smallSize, default_pos

        pov "\"Yeah, I'm fine. It's nothing serious\""

        show uniform excited_o at smallSize, default_pos

        c "\"okayy, js making sure! c u tmrw! ^^\""

        jump StartWork








    