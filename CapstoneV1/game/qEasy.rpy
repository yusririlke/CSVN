label qEasy:

l "In C++ you should always end statements with..."

menu:
        extend ''
        ";":
            play sound "audio/confirm.wav"
            jump ansQE1O
        ".":
            jump ansQE1X

label ansQE1O:
        l "Correct. +1 knowledge"
        $ knowledge += 1

        play sound "audio/confirm.wav"
        jump QE2

label ansQE1X:
        l "Incorrect."
        play sound "audio/confirm.wav"
        jump QE2

label ansQE1E:
        l "[povname], what's wrong? Cat got your tongue?"

        l "Do pay attention next time."

        pov "ok"
        play sound "audio/confirm.wav"
        jump QE2

label QE2:

    l "What is a variable?"

    menu:
            extend ''
            " A pre-defined value in a program":
                play sound "audio/confirm.wav"
                jump ansQE2X
            "A function":
                play sound "audio/confirm.wav"
                jump ansQE2X
            "A piece of memory that holds a value":
                play sound "audio/confirm.wav"
                jump ansQE2O

    label ansQE2O:
            l "Correct. +1 knowledge"
            $ knowledge += 1

            play sound "audio/confirm.wav"
            jump QE3

    label ansQE2X:
            l "Incorrect. Disgraceful."
            play sound "audio/confirm.wav"
            jump QE3

label QE3:

    l "What is an algorithm?"

    menu:
            extend ''
            "  A type of hardware component":
                play sound "audio/confirm.wav"
                jump ansQE3X
            "A set of instructions to accomplish a specific task":
                play sound "audio/confirm.wav"
                jump ansQE3O
            "A programming language":
                play sound "audio/confirm.wav"
                jump ansQE3X
            " A tool for testing software":
                play sound "audio/confirm.wav"
                jump ansQE3X

    label ansQE3O:
            l "Correct. +1 knowledge"
            $ knowledge += 1

            play sound "audio/confirm.wav"
            jump QE4

    label ansQE3X:
            l "Incorrect. Disgraceful."
            play sound "audio/confirm.wav"
            jump QE4


label QE4:

    l "What is a computer program?"

    menu:
            extend ''
            "A data type":
                play sound "audio/confirm.wav"
                jump ansQE4X
            "An input device":
                play sound "audio/confirm.wav"
                jump ansQE4X
            " A sequence of instructions executed by a computer":
                play sound "audio/confirm.wav"
                jump ansQE4O

    label ansQE4O:
            l "Correct. +1 knowledge"
            $ knowledge += 1

            play sound "audio/confirm.wav"
            jump cont2

    label ansQE4X:
            l "Incorrect. Disgraceful."
            play sound "audio/confirm.wav"
            jump cont2
