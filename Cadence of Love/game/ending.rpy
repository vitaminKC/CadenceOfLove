label ending:
    scene bg graduation

    "It's finally graduation day."
    "The ceremony is over." 
    "Families cheer, classmates hug, and caps scatter across the field."

    show uniform excited_c at smallSize, default_pos
    "You spot Cadence by the fence, alone, taking pictures of the sunset."
    "Your heart pounds."
    "Today is the day you ask her out."
    "You walk up behind her."
    show uniform excited_c at smallSize, default_pos

    if cadence.getAffection() >= 130:
        jump goodEnding 

    elif cadence.getAffection() >= 90:
        jump normalEnding

    else:
        jump badEnding


label goodEnding:




label normalEnding: 




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
    

