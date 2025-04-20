# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cadence")
define n = Character()
define pov = Character("[povname]")

define default_pos = Position(xalign=0.5)

transform smallSize: 
    zoom 0.65

# For choice switching
default pos = False
default neut = False
default neg = False

# For stat lines
default affection = 50
default money = 0

# Keep track of days (update after work day/shop)
## 0 - intro
## 1 - date 1
## 2 - date 2 
## 3 - graduation
default day = 0

label start:

    scene bg classroom 
    with fade

    show screen StatsUI

    $ povname = renpy.input("What is your name?")
    $ povname = povname.strip()

    jump intro

    














    
