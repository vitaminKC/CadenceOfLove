label intro: 
    $ povname = renpy.input("What is your name?")
    $ povname = povname.strip()

    show uniform normal_o at smallSize, default_pos

    c "\"Good morning [povname]!\""

    show uniform normal_c at smallSize, default_pos

    "You smile."

    pov "\"Good morning Cadence.\""
    pov "I've had a crush on Cadence ever since our freshman year."
    pov "I've spent all these years and I've never gotten tired of her presence."
    pov "We're seniors now and a week from graduating."
    pov "I've never even hinted that I've liked her."
    pov "I just don't want to mess up the friendship we have."

    "Cadence takes a seat next to you."

    show uniform normal_o at smallSize, default_pos

    c "\"I can't believe there's only one week left!\""
    c "\"High school really did go by in a flash.\""
    c "\"I wanna make sure I don't graduate with any regrets!\"" 

    show uniform normal_c at smallSize, default_pos

    pov "Regrets..."
    pov "Will I really graduate with no regrets?"
    pov "Will I spend the rest of my life wondering if I had a chance with Cadence?"

    show uniform normal_o at smallSize, default_pos

    c "\"Hellooo? What are you thinking about so deeply?\""

    default pos = False
    default neut = False
    default neg = False

    menu: 
        "\"You.\"":
            $ pos = True
            jump choice0

        "\"Nothing, don't worry about it.\"":
            $ neut = True
            jump choice0

        "\"Mind your own business.\"":
            $ neg = True
            jump choice0

    label choice0: 
        if pos: 
                show uniform normal_c at smallSize, default_pos

                pov "\"You.\""

                show uniform flustered_c at smallSize, default_pos

                "Cadence blushes."

                show uniform flustered_o at smallSize, default_pos

                c "\"Don't joke around like that!\""

                show uniform shy_c at smallSize, default_pos

                "She turns back around."

                jump common

        if neut: 
                show uniform normal_c at smallSize, default_pos

                pov "\"Nothing, don't worry about it.\""

                show uniform normal_o at smallSize, default_pos
                
                c "\"If you say so!\""

                show uniform normal_c at smallSize, default_pos

                "She turns back around."

                jump common

        if neg: 
                show uniform normal_c at smallSize, default_pos

                pov "\"Mind your own business.\""

                show uniform angry_o at smallSize, default_pos

                c "Jeez, it was just a question."
                c "You don't have to tell me."

                show uniform angry_c at smallSize, default_pos

                "Cadence frowns and turns back."

                jump common

    label common: 

        pov "Alright, I've decided."
        pov "I'm going to tell her how I feel."
        pov "I have one week left to try to win her over."
        pov "I won't graduate with any regret, no matter how it ends."