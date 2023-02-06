# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define admin = Character("Admin")
define pov = Character("[povname]")
define l = Character("Fir")
default knowledge = 1
default stress = 1
default money = 1

# The game starts here.

label start:

    scene bg room

    #select your name
    python:
        povname = renpy.input("Name?")
        povname = povname.strip()

        if not povname:
             povname = "Default Name"


    # Dialogue starts
    show screen gameUI

    admin "This is a basic display of the project."

    pov "Testing who is saying this."

    l "In C++ you should always end statements with..."

    menu:
        ";":
            jump ans1
        ".":
            jump ans2
        ":":
            jump ans2
        "(Why am I here)":
            jump ans3

    label ans1:
        l "Correct. +1 knowledge"
        $ knowledge += 1


        jump cont

    label ans2:
        l "Incorrect. Disgraceful."

        jump cont

    label ans3:
        l "[povname], what's wrong? Cat got your tongue?"

        l "Do pay attention next time."

        pov "ok"

        jump cont

    label cont:
        l "Next up, this game will end abruptly"

        pov "EHHHH??"




    admin "The game will now end goodbye [povname]."

    # This ends the game.

    return
