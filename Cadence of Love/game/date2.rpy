label date2: 
    scene bg study

    pov "Today is my second date with Cadence."
    pov "I don't know if I'm more nervous for our upcoming physics test or this date."

    show uniform normal_c at smallSize, default_pos

    "You find Cadence sitting alone at a table in the corner of the classroom." 
    "She stares intently at her work, not noticing you walk in."

    # Greeting choices
    menu: 
        # Negative choice
        "Walk up from behind her and scare her.": 
            $ neg = True
            $ cadence.subAffection()
            "Your affection went down by 10."
            jump studyResponse

        # Neutral choice
        "Sit across from her and wait until she notices.":
            $ neut = True
            jump studyResponse

        # Positive choice
        "Walk up and greet her.":
            $ pos = True
            $ cadence.addAffection()
            "Your affection went up by 10!"
            jump studyResponse

    # Greet responses
    label studyResponse:
        # Positive response
        if pos:
            $ pos = False
            pov  "\"Hey!\""
            pov  "\"I hope you weren't waiting too long.\""

            show uniform shy_o at smallSize, default_pos
            c "\"Oh hey!\""
            c "\"I haven't been here long.\""

            show uniform excited_o at smallSize, default_pos
            c "\"Let's work hard to pass that physics test tomorrow!\""

            show uniform excited_c at smallSize, default_pos
            pov "\"I’ll make sure to study twice as hard so I can catch up.\""

            jump studyHelpScene

        # Neutral response
        if neut: 
            $ neut = False
            "You stand next to Cadence and watch her do her work."
            "Cadence notices you after a couple minutes."

            show uniform flustered_o at smallSize, default_pos
            c  "\"Oh my gosh, hi!\""

            show uniform normal_o at smallSize, default_pos
            c  "\"I didn't even notice you there.\""
            c  "\"When did you get here?\""

            show uniform normal_c at smallSize, default_pos
            pov "\"Not long ago.\""
            pov "\"Mind if I sit here?\""

            "She pulls out the seat beside her and motions for you to sit down."

            jump studyHelpScene

        # Negative response
        if neg: 
            $ neg = False
            "You walk up behind her and scare her."

            show uniform flustered_c at smallSize, default_pos
            "Cadence jumps in her seat and turns to look at you annoyed."

            show uniform angry_c at smallSize, default_pos
            "She rolls her eyes."

            show uniform angry_o at smallSize, default_pos
            c  "\"Very funny.\""

            show uniform angry_c at smallSize, default_pos
            pov  "\"...\""

            jump studyHelpScene

    # Helping Cadence with physics problem scene
    label studyHelpScene: 
        show uniform upset_c at smallSize, default_pos
        "Some time has passed and Cadence is still staring intently at the problem she's working on."

        show uniform upset_o at smallSize, default_pos
        c "\"I've been trying to solve this problem and I just can't figure it out.\""
        
        show uniform upset_c at smallSize, default_pos

        # Help choices
        menu:
            # Positive choice
            "Offer to help.":
                $ pos = True
                $ cadence.addAffection()
                "Your affection went up by 10!"
                jump studyHelpChoice

            # Neutral choice
            "Encourage her.":
                $ neut = True
                jump studyHelpChoice
            
            # Negative choice
            # This will end the date and skip to the ending (lose extra affection)
            "\"How are you getting stuck on something like that?\"":
                $ neg = True
                $ cadence.subAffection()
                $ cadence.subAffection()
                "Your affection went down by 20."
                jump studyHelpChoice

    # Help Response
    label studyHelpChoice:
        # Positive response
        if pos: 
            $ pos = False
            pov  "\"Which problem are you working on?\""
            pov  "\"I could take a look at it.\""

            show uniform shy_c at smallSize, default_pos
            "Cadence turns her paper towards you."

            pov  "\"Oh I see.\""
            pov  "\"So for this question, even though the object is rotating...\""
            pov  "\"If you use the object's center of mass,\""

            show uniform normal_c at smallSize, default_pos
            pov  "\"You can just treat it as a normal projectile motion problem!\""

            show uniform normal_o at smallSize, default_pos
            c "\"Oh, I see!\""
            c "\"From there, I can break up the velocity into components and solve the problem!\""
            c "\"Let me try that.\""

            show uniform normal_c at smallSize, default_pos
            "Cadence scribbles furiously on her paper."

            show uniform shy_o at smallSize, default_pos
            c "\"It should be like that, right?\""

            show uniform shy_c at smallSize, default_pos
            pov "\"Looks good to me.\""

            show uniform excited_o at smallSize, default_pos
            c "\"Yay! I think I get it now.\""

            show uniform normal_o at smallSize, default_pos
            c "\"Thanks so much.\""

            show uniform shy_o at smallSize, default_pos
            c "\"You're a really good teacher.\""

            show uniform shy_c at smallSize, default_pos
            pov "\"I'm glad I could help.\""
            
            jump studyEnding

        # Neutral response
        if neut:
            $ neut = False
            pov "\"You got this.\""

            show uniform upset_o at smallSize, default_pos
            c "\"I'm not so sure...\""

            show uniform upset_c at smallSize, default_pos
            pov "\"I believe in you.\""

            show uniform upset_o at smallSize, default_pos
            c "\"I guess that makes one of us.\""

            show uniform upset_c at smallSize, default_pos
            "Cadence turns back around and continues doing the problem in silence."

            jump studyEnding

        # Negative response
        # Should skip directly to ending (end date)
        if neg:
            $ neg = False
            pov "\"How are you getting stuck on something like that?\""

            show uniform angry_o at smallSize, default_pos
            c "\"Are you kidding?\""
            c "\"Why would you say something like that?\""

            show uniform angry_c at smallSize, default_pos
            pov "\"It's a really simple problem.\""
            pov "\"I don't know why a question like that is taking you so long.\""

            show uniform angry_o at smallSize, default_pos
            c "\"Did you come here to study with me or to insult me?\""
            
            show uniform angry_c at smallSize, default_pos
            pov "\"I-\""

            show uniform angry_o at smallSize, default_pos
            c "\"Whatever, this is obviously a waste of time.\""
            c "\"I'm leaving.\""

            jump ending

    label studyEnding:
        scene bg outside
        "After a whole day of studying, you offer to walk Cadence home."

        show uniform normal_o at smallSize, default_pos

        c "\"Thank you for all the physics help today.\""

        show uniform excited_o at smallSize, default_pos
        c "\"On top of all that help, you even walked me home!\""

        show uniform normal_c at smallSize, default_pos
        pov "\"I wanted to make sure you got home safe.\""
        pov "\"After all...\""
        pov "\"You're someone really special to me.\""

        show uniform shy_o at smallSize, default_pos
        c "\"Is that so...\""
        c "\"I...\""

        show uniform shy_c at smallSize, default_pos
        "Cadence thinks to herself for a moment."

        show uniform shy_o at smallSize, default_pos
        c "\"Actually..\""
        c "\"Nevermind.\""

        show uniform shy_o at smallSize, default_pos
        c "\"I really appreciate the help today.\""
        c "\"I'll catch you later!\""

        scene bg outside
        "Cadence turns around quickly and enters her house..."
        "Leaving you wondering how she really feels..."

        jump date2_text