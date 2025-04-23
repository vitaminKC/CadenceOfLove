# Movie date
label date1: 
    scene bg outside
    with fade 

    pov "\"Oh man, I'm so nervous.\""
    pov "Today is my first date with Cadence."
    pov "I really don't want to mess this up."

    show movie normal_c at smallSize, default_pos

    "You spot Cadence near the entrance of the movie theater." 

    if cadence.getAffection() >= 50:
        show movie excited_c at smallSize, default_pos

        "She lights up when she sees you."

        show movie excited_o at smallSize, default_pos

        c  "\"Hi!\""
        c  "\"I'm so pumped for this movie, you have no idea!\""
        c  "\"I've been counting down the days.\""

    else: 
        show movie normal_o at smallSize, default_pos
        c  "\"Hi!\""
        c  "\"I'm so pumped for this movie, you have no idea!\""

    show movie normal_c at smallSize, default_pos
    pov "\"Same here.\""
    pov "\"I've been avoiding spoilers like my life depends on it.\""

    # Allow user to compliment her outfit
    menu: 
        "Compliment her outfit":
            $ pos = True
            $ cadence.addAffection()
            jump movieCompliment
        
        "Continue":
            jump movieSnack

        "\"Red isn't really your color\"":
            $ neg = True
            $ cadence.subAffection()
            jump movieCompliment
    
    # Compliment response
    label movieCompliment:
        if pos:
            $ pos = False
            "You admire the effort Cadence put into her outfit."

            pov "\"Wow...\""
            pov "\"You look amazing...\""

            show movie flustered_c at smallSize, default_pos
            "Candence was surprised by your sudden compliment."

            show movie shy_o at smallSize, default_pos
            c  "\"T-thank you. I was hoping you'd notice.\""

            jump movieSnack
        
        if neg:
            $ neg = False
            "You stare at Cadence's outfit."

            pov "\"Red doesn't really suit you...\""

            show movie angry_c at smallSize, default_pos
            "Cadence obviously gets offended."
        
            show movie angry_o at smallSize, default_pos
            c  "\"Why would you say something like that?\""
            c  "\"Whatever, let's just go.\""
            
            jump movieSnack

    # Snack scene
    label movieSnack:
        scene bg movie

        show movie normal_c at smallSize, default_pos
        pov "\"I've got our tickets already.\""
        pov "\"Want to grab some snacks before it starts?\""

        menu: 
            "Nerds candy":
                $ neg = True
                $ cadence.subAffection()
                jump movieSnackChoice
             
            "Popcorn":
                $ pos = True
                $ cadence.addAffection()
                jump movieSnackChoice
            
            "Chocolate":
                $ neut = True
                jump movieSnackChoice

    # Snack response
    label movieSnackChoice: 
        if pos: 
            $ pos = False
            pov "\"Want to split some popcorn?\""
            pov "\"I'll go heavy on the butter if you're into that.\""
            
            show movie excited_c at smallSize, default_pos
            "Cadence playfully nudges you."

            show movie excited_o at smallSize, default_pos
            c  "\"Absolutely!\""
            c  "\"You do know the way to my heart!\""
            jump movieViewing

        if neut: 
            $ neut = False
            pov "\"Do you wanna get some chocolate?\""

            show movie normal_o at smallSize, default_pos

            c  "\"That works. Classic choice.\""

            show movie excited_o at smallSize, default_pos

            c  "\"I might steal a piece when you're not looking!\""
            jump movieViewing

        if neg: 
            $ neg = False
            pov "\"I'm grabbing Nerds candy.\""
            pov "\"You want some?\""

            show movie upset_c at smallSize, default_pos
            "Cadence makes a face."

            show movie upset_o at smallSize, default_pos
            c  "\"Ew, you mean the candy equivalent of gravel?\"" 
            c  "\"I'll pass.\"" 
            jump movieViewing
       
    # Post movie
    label movieViewing: 
        show movie normal_c at smallSize, default_pos

        "With snacks in hand, the two of you find your seats and settle in as the lights dim."

        scene bg movie_outside

        "After the movie..."

        show movie excited_o at smallSize, default_pos
        c  "\"That was so much fun!\""

        show movie normal_o at smallSize, default_pos
        c  "\"Thanks for inviting me.\""

        show movie shy_o at smallSize, default_pos
        c  "\"..and for not talking through the whole movie.\""

        show movie normal_c at smallSize, default_pos
        "Cadence winks."

        pov "\"It was fun for me as well.\""
        pov "\"I'll always have a good time, as long as it's with you.\""

        show movie shy_o at smallSize, default_pos
        c  "\"Is that so?\""

        show movie normal_o at smallSize, default_pos
        c  "\"I guess we'll both be looking forward to the next time we hang out together.\""

        show movie excited_c at smallSize, default_pos
        "She waves goodbye and disappears into the crowd with a lingering smile."

        jump date1Text



        
            
    



