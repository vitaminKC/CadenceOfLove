label ending:
    scene bg graduation

    "Some time has passed since your last date with Cadence."
    "You guys text every once and a while, but you both have been busy with finals."
    "But, it's finally graduation day."
    "The ceremony is over." 
    "Families cheer, classmates hug, and caps scatter across the field."

    show uniform excited_c at smallSize, default_pos
    "You spot Cadence by the fence, alone, taking pictures of the sunset."
    "Your heart pounds."
    "Today is the day you ask her out."
    "You walk up behind her."
    show uniform excited_c at smallSize, default_pos

    if cadence.getAffection() >= 120:
        jump goodEnding 

    elif cadence.getAffection() >= 80:
        jump normalEnding

    else:
        jump badEnding


label goodEnding:
    pov "\"There you are.\""
    pov "\"I've been looking for you.\""

    show uniform normal_o at smallSize, default_pos
    c "\"Took you long enough.\""

    show uniform excited_o at smallSize, default_pos
    c "\"It's official!\""
    c "\"We've finished high school!\""

    show uniform normal_o at smallSize, default_pos
    c "\"Can't you believe it?\""
    c "\"Honestly, I'm really lucky to have you as a friend for all these years.\""

    show uniform shy_o at smallSize, default_pos 
    c "\"You're always thinking of me.\""
    c "\"The past week especially...\""

    show uniform shy_c at smallSize, default_pos
    pov "\"Yeah...friends...\""
    pov "\"About that...\""
    pov "\"For all these years...\""
    pov "\"You're the only person I've ever had eyes for.\""
    pov "\"To me,\""
    pov "\"You're the smartest, kindest, and prettiest girl I've ever known.\""

    show uniform flustered_c at smallSize, default_pos
    pov "\"I really like you.\""
    pov "\"Would you...let me be your boyfriend?\""

    "Cadence blinks, surprised..."
    
    show uniform excited_c at smallSize, default_pos
    "...then breaks into a huge grin."

    show uniform excited_o at smallSize, default_pos
    c "\"Yes! Of course!\""

    show uniform normal_o at smallSize, default_pos
    c "\"I was hoping you'd ask.\""

    show uniform shy_o at smallSize, default_pos
    c "\"I was actually getting ready to ask you myself...\""

    show uniform shy_c at smallSize, default_pos
    pov "\"Wait, really?\""    

    show uniform normal_o at smallSize, default_pos
    "Cadence lets out a little laugh."

    c "\"Yeah. At least we both made it here.\""

    show uniform excited_c at smallSize, default_pos
    "She steps closer, wrapping her arms around you."
    "The cheers and music blur into the background."
    "It’s the end of high school"
    "but the start of something new."
    jump exitGame

label normalEnding: 
    pov "\"Cadence!\""
    pov "\"Mind if I steal you for a sec?\""

    show uniform normal_o at smallSize, default_pos
    c "\"For you? Always.\""
    c "\"What's up?\""

    show uniform normal_c at smallSize, default_pos
    pov "\"Okay, so this might be kind of dumb.\""
    pov "\"But I was wondering if maybe you'd want to be more than friends?\""
    pov "\"Like...will you be my girlfriend?\""

    show uniform flustered_o at smallSize, default_pos
    c "\"Oh...\""

    show uniform shy_o at smallSize, default_pos
    c "\"You're really sweet. And I do care about you.\""
    c "\"But I really like where we are now...\""
    c "\"...as friends.\""

    show uniform upset_o at smallSize, default_pos
    c "\"I'm sorry.\""

    show uniform upset_c at smallSize, default_pos
    pov "\"No, I get it.\""
    pov "\"I really value our friendship too.\""
    pov "\"I wouldn't want to risk what we have right now.\""

    show uniform shy_o at smallSize, default_pos
    c "\"Honestly, I'm glad you told me.\""

    show uniform normal_o at smallSize, default_pos
    c "\"That took guts.\""

    show uniform shy_o at smallSize, default_pos 
    c "\"And I still want us to keep in touch\""
    c "\"Okay?\""

    show uniform shy_c at smallSize, default_pos
    pov "\"Yeah...\""

    show uniform normal_c at smallSize, default_pos
    pov "\"Of course.\""

    "It’s not the ending you hoped for"
    "But there's comfort in knowing that she still wants you in her life."
    jump exitGame


label badEnding: 
    pov "\"Hey Cadence...\""
    pov "\"Can I talk to you for a second?\""

    show uniform flustered_o at smallSize, default_pos
    c "\"Oh!\""

    show uniform normal_o at smallSize, default_pos
    c "\"Sure, what's up?\""

    show uniform normal_c at smallSize, default_pos
    pov "\"So...\""
    pov "\"This might be totally out of the blue, but...\""
    pov "\"We've hung out a few times, and I really like you.\""
    pov "\"I was wondering if you'd maybe want to be my girlfriend?\""

    show uniform flustered_c at smallSize, default_pos
    "Cadence freezes up."

    show uniform upset_o at smallSize, default_pos
    c "\"Wait...seriously?\""

    show uniform upset_c at smallSize, default_pos
    pov "\"Yeah. I know we haven’t known each other that long, but I thought maybe—\""

    show uniform upset_o at smallSize, default_pos
    c "\"Look... I don't want to be mean, but...\""
    c "\"I didn't think you saw this as anything more than casual.\""
    c "\"You're...nice, but you're not really my type.\""

    show uniform upset_c at smallSize, default_pos
    "She looks away for a second, clearly uncomfortable."

    show uniform upset_o at smallSize, default_pos
    c "\"Honestly, this is kinda of awkward.\""
    c "\"You probably misread things.\""
    
    show uniform upset_c at smallSize, default_pos
    pov "\"Oh. I just thought...\""

    show uniform upset_o at smallSize, default_pos
    c "\"I just wish you'd say something earlier.\""
    c "\"Or maybe...not at all.\""
    c "\"It's graduation.\""
    c "\"I kind of wanted today to be perfect.\""

    show uniform upset_c at smallSize, default_pos
    "She gives you a tight uncomfortable smile and turns away, leaving you standing alone as the noise
    of the crowd swells behind you."

    hide uniform upset_c with fade
    "The sun sets on the field as students laugh and take photos"
    "But none of them include you."
    "Maybe some people are just meant to be side characters in someone else's happy ending."

    jump exitGame

label exitGame:
        "Thank you for playing!"
    

