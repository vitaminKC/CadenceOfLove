label intro_text: 
    scene bg bedroom
    with fade

    "You received a text from Cadence!"

    show uniform excited_o at smallSize, default_pos

    c "\"hiiiii!\""

    menu: 
        "\"Heyyyyy\"": 
            $ pos = True
            $ cadence.addAffection()
            jump introTextChoices
        
        "\"Do you need something?\"":
            $ neut = True
            jump introTextChoices

        "Leave her on read.":
            $ neg = True
            $ cadence.subAffection()
            jump introTextChoices

    label introTextChoices:
        show uniform excited_c at smallSize, default_pos

        if pos: 
            $ pos = False
            pov "\"Heyyyyy\""
            pov "\"What's up?\""

            show uniform normal_o at smallSize, default_pos

            c "\"nothing muchhhhh\""

            jump introTextCommon

        if neut: 
            $ neut = False
            pov "\"Do you need something?\""

            show uniform upset_o at smallSize, default_pos

            c "\"uh no\""

            jump introTextCommon
        
        if neg: 
            $ neg = False
            "You left her on read."

            show uniform angry_o at smallSize, default_pos

            c "\"ill c u tmrw ig\""

            jump WorkDay

    label introTextCommon:
        show uniform normal_o at smallSize, default_pos

        c "\"js wanted to check in on you since you were zoning out the entire day\""

        show uniform normal_c at smallSize, default_pos

        pov "\"Yeah, I'm fine. It's nothing serious\""

        show uniform excited_o at smallSize, default_pos

        c "\"okayy, js making sure! c u tmrw! ^^\""

        jump WorkDay








    