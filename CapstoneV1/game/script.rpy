# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define teacher = Character("Teacher")
define profe = Character("Array")
define phone = Character("Phone")
define conwell = Character("Conwell")
define me = Character("Me")
define alarm = Character("Alarm")
define unknown = Character("?")
define vic = Character("Vic")
define admin = Character("Admin")
define povname = Character("[povname]")
define l = Character("Fir")
define reena = Character("Reena")
define stomach = Character("Stomach")
define worker = Character("Volunteer")
define book = Character("Textbook")
default knowledge = 1
default stress = 5
default money = 10
image ibook = "images/book.png"
image clock = "images/clock.png"
image prof = "images/prof.png"
image cafeteria = "images/cafeteria.png"
image  bg dorm = "images/bg_dorm.png"
image hall = "images/hall.jpg"
image aud = "images/aud.png"
image blank = "images/blank.jpg"
image orientation = "images/orientation.png"
image girl = "images/girl.png"
image vicNeutral = "vicNeutral.png"
image reena = "reena.png"
image outschool = "images/outschool.png"
image classday = "images/classroom.png"
image hello = "images/helloworld.png"
image hello1 = "images/helloworld1.png"
image hello2 = "images/helloworld2.png"
image hellop = "images/helloworldprac.png"

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
