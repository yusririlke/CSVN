# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define admin = Character("Admin")
define pov = Character("[povname]")


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

    admin "This is a basic display of the project."

    pov "Testing who is saying this."

    admin "The game will now end goodbye [povname]."

    # This ends the game.

    return
