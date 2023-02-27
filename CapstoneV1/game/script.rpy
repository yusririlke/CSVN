# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define me = Character("Me")
define alarm = Character("Alarm")
define unknown = Character("?")
define roomate = Character("Vic")
define admin = Character("Admin")
define pov = Character("[povname]")
define l = Character("Fir")
define worker = Character("worker")
default knowledge = 1
default stress = 1
default money = 1

# The game starts here.

label start:

    scene bg room

    #select your name
    #python:
    #    povname = renpy.input("Name?")
    #    povname = povname.strip()

    #    if not povname:
    #         povname = "Default Name"


    # Dialogue starts
    show screen gameUI


    jump intro
	
label close:

    admin "The game will now end goodbye [povname]."

    # This ends the game.

    return