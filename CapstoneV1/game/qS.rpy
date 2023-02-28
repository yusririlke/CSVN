  #jump qEasy



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
