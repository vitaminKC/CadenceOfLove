# Movie date
label date1: 
    scene bg outside
    with fade 

    pov "\"Oh man, I'm so nervous.\""
    pov "Today is my first date with Cadence."
    pov "I really don't want to mess this up."

    show movie normal_c at smallSize, default_pos

    "You spot Cadence near the entrance of the movie theater." 

    if affection >= 50:
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

    menu: 
        "Compliment her outfit":
            $ pos = True
            $ affection += 10
            jump movieChoice1
        
        "Continue":
            jump movieCommon1

        "\"Red isn't really your color\"":
            $ neg = True
            $ affection -= 10
            jump movieChoice1
        
    label movieChoice1:
        if pos:
            $ pos = False
            "You admire the effort Cadence put into her outfit."

            pov "\"Wow...\""
            pov "\"You look amazing...\""

            show movie flustered_c at smallSize, default_pos
            "Candence was surprised by your sudden compliment."

            show movie shy_o at smallSize, default_pos
            c  "\"T-thank you. I was hoping you'd notice.\""

            jump movieCommon1
        
        if neg:
            $ neg = False
            "You stare at Cadence's outfit."

            pov "\"Red doesn't really suit you...\""

            show movie angry_c at smallSize, default_pos
            "Cadence obviously gets offended."
        
            show movie angry_o at smallSize, default_pos
            c  "\"Why would you say something like that?\""
            c  "\"Whatever, let's just go.\""
            
            jump movieCommon1

    label movieCommon1:
        scene bg movie

        show movie normal_c at smallSize, default_pos
        pov "\"I've got our tickets already.\""
        pov "\"Want to grab some snacks before it starts?\""

        menu: 
            "Nerds candy":
                $ neg = True
                jump movieChoice2
             
            "Popcorn":
                $ pos = True
                jump movieChoice2
            
            "Chocolate":
                $ neut = True
                jump movieChoice2

    label movieChoice2: 
        if pos: 
            $ pos = False
            pov "\"Want to split some popcorn?\""
            pov "\"I'll go heavy on the butter if you're into that.\""
            
            show movie excited_c at smallSize, default_pos
            "Cadence playfully nudges you."

            show movie excited_o at smallSize, default_pos
            c  "\"Absolutely!\""
            c  "\"You do know the way to my heart!\""
            jump movieCommon2

        if neut: 
            $ neut = False
            pov "\"Do you wanna get some chocolate?\""

            show movie normal_o at smallSize, default_pos

            c  "\"That works. Classic choice.\""

            show movie excited_o at smallSize, default_pos

            c  "\"I might steal a piece when you're not looking!\""
            jump movieCommon1

        if neg: 
            $ neg = False
            pov "\"I'm grabbing Nerds candy.\""
            pov "\"You want some?\""

            show movie upset_c at smallSize, default_pos
            "Cadence makes a face."

            show movie upset_o at smallSize, default_pos
            c  "\"Ew, you mean the candy equivalent of gravel?\"" 
            c  "\"I'll pass.\"" 
            jump movieCommon1
       

    label movieCommon2: 
        show movie normal_c at smallSize, default_pos

        "test"


        
            
    



