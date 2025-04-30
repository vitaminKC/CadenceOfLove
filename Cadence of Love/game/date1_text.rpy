label date1Text: 
    scene bg bedroom with fade

    "Later that evening..."
    "You received a text from Cadence!"

    show uniform normal_o at smallSize, default_pos
    c "\"heyyy, i had a great time today\""

    show uniform normal_c at smallSize, default_pos
    pov "\"I'm just glad you enjoyed it.\""

    show uniform normal_o at smallSize, default_pos
    c "\"oh! that reminds me...\""
    c "\"what kind of movies do you usually like to watch?\""

    # Choice menu
    menu: 
        # Neutral choice
        "Horror":
            $ neut = True
            jump movieTextResponse
        
        # Positive choice
        "Romance":
            $ pos = True
            $ cadence.addAffection()
            "Your affection went up by 10!"
            jump movieTextResponse

        # Negative choice
        "\"I hate movies.\"":
            $ neg = True
            $ cadence.subAffection()
            "Your affection went down by 10."
            jump movieTextResponse

    label movieTextResponse:
        # Postive response
        if pos: 
            $ pos = False
            show uniform normal_c at smallSize, default_pos
            pov "\"It might be embarrassing but I'm a real sucker for a good romance movie.\""

            show uniform excited_o at smallSize, default_pos
            c "\"i luv romance movies!!\""

            show uniform excited_c at smallSize, default_pos
            pov "\"You seem like the type to like them.\""

            show uniform normal_o at smallSize, default_pos
            c "\"yeah they're rly sweet\""
            c "\"i also like to read them, though theyre normally kinda sappy\""
            c "\"what kind of romance do you like?\""

            show uniform normal_c at smallSize, default_pos
            pov "\"I like the type of romance I would have with you.\""

            show uniform flustered_o at smallSize, default_pos
            c "\"i wasnt expecting an answer like that\""
            
            show uniform shy_o at smallSize, default_pos
            c "\"im really flattered...\""

            show uniform normal_o at smallSize, default_pos
            c "\"ig ill see you at school tmrw :)\""

            jump StartWork

        # Neutral response
        if neut: 
            $ neut = False
            show uniform normal_c at smallSize, default_pos
            pov "\"I like horror movies.\""

            show uniform flustered_o at smallSize, default_pos
            c "\"i could never...\""
            c "\"i get so scared, i cant sleep at night x)\""

            show uniform normal_o at smallSize, default_pos
            c "\"speaking of sleep...\""
            c "\"i should probably head to bed\""
            c "\"c u tmrw!\""

            jump StartWork
        
        # Negative response
        if neg: 
            $ neg = False
            show uniform normal_c at smallSize, default_pos
            pov "\"I hate movies.\""

            show uniform angry_o at smallSize, default_pos
            c "\"y bother taking me to one then?\""
            c "\"i gtg. c u tmrw\""

            jump StartWork




            



        

        
    