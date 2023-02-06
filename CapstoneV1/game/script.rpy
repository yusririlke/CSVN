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
        extend ''
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
        l "Next up, an intermediate question"

        pov "I think I'm ready..."

        l "What is a linked list?"

    menu:
        extend ''
        "An array of elements stored in contiguous memory locations":
            jump anse
        " A linear collection of elements, where each element points to the next":
            jump ansb
        "A data structure with elements stored in a tree-like hierarchy":
            jump anse
        "A two-dimensional array of elements":
            jump anse

    label ansb:
        l "Correct. +1 knowledge"
        $ knowledge += 1


        jump cont1

    label anse:
        l "Incorrect. Disgraceful."

        jump cont1

    label cont1:
        l "Next up, an advanced question"

        pov "Guh"

        l "Why is the umask 777 bad ?"

    menu:
        extend ''
        "It's actually fine":
            jump ansg
        "Oh, that gives access to everyone for everything":
            jump ansa
        "We can't access it?":
            jump ansg
        "The program can't access it.":
            jump ansg

    label ansa:
        l "Correct. +1 knowledge"
        $ knowledge += 1

        jump cont2

    label ansg:
        l "Incorrect. Disgraceful."

        jump cont2

    label cont2:
        l "This game is ending"



    admin "The game will now end goodbye [povname]."

    # This ends the game.

    return
