label qEasy:

l "In C++ you should always end statements with..."

menu:
        extend ''
        ";":
            jump ansQE1O
        ".":
            jump ansQE1X
        ":":
            jump ansQE1X
        "(Why am I here)":
            jump ansQE1E

label ansQE1O:
        l "Correct. +1 knowledge"
        $ knowledge += 1


        jump QE2

label ansQE1X:
        l "Incorrect. Disgraceful."

        jump QE2

label ansQE1E:
        l "[povname], what's wrong? Cat got your tongue?"

        l "Do pay attention next time."

        pov "ok"

        jump QE2

label QE2:

    l "What is a variable?"

    menu:
            extend ''
            " A pre-defined value in a program":
                jump ansQE2X
            "A function":
                jump ansQE2X
            "A piece of memory that holds a value":
                jump ansQE2O
            "A data type":
                jump ansQE2X

    label ansQE2O:
            l "Correct. +1 knowledge"
            $ knowledge += 1


            jump QE3

    label ansQE2X:
            l "Incorrect. Disgraceful."

            jump QE3

label QE3:

    l "What is an algorithm?"

    menu:
            extend ''
            "  A type of hardware component":
                jump ansQE3X
            "A set of instructions to accomplish a specific task":
                jump ansQE3O
            "A programming language":
                jump ansQE3X
            " A tool for testing software":
                jump ansQE3X

    label ansQE3O:
            l "Correct. +1 knowledge"
            $ knowledge += 1


            jump QE4

    label ansQE3X:
            l "Incorrect. Disgraceful."

            jump QE4


label QE4:

    l "What is a computer program?"

    menu:
            extend ''
            " A type of hardware component":
                jump ansQE4X
            "A data type":
                jump ansQE4X
            "An input device":
                jump ansQE4X
            " A sequence of instructions executed by a computer":
                jump ansQE4O

    label ansQE4O:
            l "Correct. +1 knowledge"
            $ knowledge += 1


            jump cont

    label ansQE4X:
            l "Incorrect. Disgraceful."

            jump cont
