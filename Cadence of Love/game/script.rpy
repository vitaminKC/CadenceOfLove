# The script of the game goes in this file.

define c = Character("Cadence")
define n = Character()
define pov = Character("[povname]")

define default_pos = Position(xalign=0.5)

transform smallSize: 
    zoom 0.65

# For choice switching
# Will switch to True when a choice is made
# Switch back to False in the response block for the next time a choice is made
default pos = False
default neut = False
default neg = False

# For stat lines
# Default affection should be 50
default cadence = Cadence(50, 0)


# For shop
define flowers = 0
define chocolates = 0
define teddies = 0
define item = ""

# Keep track of days (update after work day/shop)
## 0 - intro
## 1 - date 1
## 2 - date 2 
## 3 - graduation (ending)
default day = 0

label start: 

    scene bg classroom 
    with fade

    show screen StatsUI

    $ povname = renpy.input("What is your name?")
    $ povname = povname.strip()

    # Should start at intro 
    jump intro

    














    
