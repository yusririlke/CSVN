# Declare characters used by this game. The color argument colorizes the
# name of the character.

default score = 0
image library = ("images/library.png")
define student = Character("Student")
define student2 = Character("Student2")
define teacher = Character("Teacher")
define lily = Character("Lily")
define libraryw = Character("Worker")
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
image living day = "images/living_day.png"
image hw5 = "images/HW5.png"
image array1 = "images/Array1.png"
image arrays = "images/ArrayStr.png"
image array2 = "images/Array2.png"
image array3 = "images/Array3.png"
image ibook = "images/book.png"
image clock = "images/clock.png"
image prof = "images/prof.png"
image cafeteria = "images/cafeteria.png"
image  bg dorm = "images/bg_dorm.png"
image  dorm night = "images/dorm_night.png"
image  living night= "images/livingnight.png"
image hall = "images/hall.jpg"
image aud = "images/aud.png"
image blank = "images/blank.png"
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
image hello2ce = "images/hello2ce.png"
image whilel = "images/whileloop.jpg"
image whilel2 = "images/whileloop1.jpg"
image whilel3 = "images/whileloop2.jpg"
image whilel4 = "images/whileloop3.jpg"
image whilel5 = "images/whileloop4.jpg"
image libraryOut = "images/libraryOut.png"
image libraryCounter = "images/libraryCounter.png"
image computerGen = "images/computer_gen.png"
image dtype1 = "images/dtype1.png"
image dtype2 = "images/dtype2.png"
image pointer1 = "images/pointer1.png"
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
