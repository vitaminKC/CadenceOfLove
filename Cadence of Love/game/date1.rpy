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
    



