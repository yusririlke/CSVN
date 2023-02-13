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
