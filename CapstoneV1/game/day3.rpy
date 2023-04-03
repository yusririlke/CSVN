label day3:

scene bg dorm with dissolve

povname "'mmnh'"
povname "Well, I beat the alarm today."
play music "audio/dorm.wav"
povname "I get ready for a morning of class and oh, my first day at work."

# spain peko

scene living day with dissolve
povname "Huh, I guess Vic has a morning class today."
povname "Oh, well. off to class then"

scene outschool with dissolve
povname "I eventually reach the main building where my classes take place."
#TODO: Other classes time passing comment. show hallway?
povname "After a few other classes, I head to my last class of the day before I start my job."

scene classday with dissolve
povname "Much like yesterday, I showed up more or less at the same time..."
povname "...and yet, the class still seems a little sparse."
povname "Still unclear whether it's a function of first year students or just Computer Science students in genral."
show prof with dissolve
#Data Type bit fr
profe "Alright class, let's pick up the pace a little, and talk about data types."
profe "So, most programming languages have something called data types."
profe "They exist to help the compiler understand what you're trying to do."
profe "For example, lets take a look at yesterday's Hello World program."
show hello with dissolve
profe "On line 5, we can see the code to print out to the console."
profe "Now in this code there is only one data type, the main function."
profe "There are multiple data types in C++ and they can be split into three different classes."
profe "The most basic of which is Primary Data Types, these help us identify what data type a variable is."
profe "These include the ones here."
#TODO: Show primary data types
profe "The next class is derived data types. These are data types that hold multiple instances of the same or different data types."
#TODO: sHOW hELLO0 PROGRAM
profe "This includes functions, like the main function in our hello world program, between lines 3 and 7."
profe "Arrays which are a collection of the same data type..."
profe "Pointers and References, which , as the name suggests, points to and refers to the address of a certain area in memory."
profe "Fortunately, thats not a problem for today."
show prof with dissolve
profe "We can also define our own data types with constructs such as Classes, Structures or just a straight up type definition."
profe "This allows us to do all sorts of cool things such as..."
profe "*clears throat*"
profe "Again, a story for another day."
povname "...a! That's a lot of knowledge."
hide prof with dissolve
#Variables frfr on oath on code
profe "Now let's move on to Variables."
#Hello World code should already be up at this point.
profe "I like to say that variables are like buckets. In the sense that they can hold things."
profe "But unlike buckets, in C++, every variable has its own color."
povname "What? Eh? How's that work?"
profe "I mean, each variable has its own data type."
povname "Ah, okay. that makes sense"
profe "For example, consider line 5 here."
profe "What if we wanted to type that line several times? Without having to retype it?"
profe "That's where we can assign data to variables!"
show dtype1 with dissolve
profe "Direct your attention to line 5"
profe "the structure of a variable assignment is as follows."
profe "The first word there is the data type. Since this is a series of characters, the appropriate data type is string."
profe "The second word is the variable name. All variables need a name."
profe "And the next bit is the data we're putting in it. In this case, it's the string \"Hello World\""
profe "Strings are quite special since to assign them to a variable, they need the  quotation marks to be accepted."
profe "This will print out Hello World like our previous program."
profe "Here are some examples of other variable assignments."
#TODO:Show other examples
povname "I wonder what happens when we assign a variable the wrong data type?"
scene classday with dissolve
show prof with dissolve
profe "Alright, that's all the learning we have for today. Dismissed"
povname "I should probably head out to the library"
#TODO: Show library entrance, outside, something.
povname "This should be the place, I think."
#TODO: Show library inside with counter
povname "As I pass through the large glass entrance, a familiar face looks up at me."
#TODO: Show Lily
povname "'Hi, I'm here to start work,I think.'"
lily "Ah, you're uhm... [povname] right? They told me there was a new hire"
lily "Right, I assume the boss has given you the whole onboarding schtick,eh?"
povname "I nod my head sheepishly."
lily "Ah, good. Here's your assignment for the day, you're stacking books over at Periodicals."
#TODO: Jump to minigame
lily "Well then, remember to check the app for your schedules, but you already know that, right?"
povname "'The management portal?'"
lily "Yep, yep. That's right, see ya at the next shift."
povname "Right, see ya then."
scene living day with dissolve
povname "'I'm back~'"
vic "Ah, look who's back, back again."
show vicNeutral with dissolve
vic "Have ya eaten? I ordered waaay too much. Feel free to take a plate and dig in."
povname "I looked at the whole smorgasbord on the table."
povname "There was half a cheesesteak, what was once some cheesy nachos and half a bowl of salad."
povname "I gave vic a judgemental stare"
vic "Look, In my defense I was REALLY hungry."
povname "I grab a plate from the rack and picked up..."
menu:
    extend ''
    "The cheesesteak":
        play sound "audio/confirm.wav"
        jump cheesesteak
    "The Nachos":
        play sound "audio/confirm.wav"
        jump nachos
    "The Salad":
        play sound "audio/confirm.wav"
        jump salad

label cheesesteak:
    vic "Ah, the cheesesteak. Good, but not as good as Wawa's though."
    povname "'Isn't that a gas station?'"
    vic "Nah, it's a fuel station for you and your car."
    povname "I rolled my eyes at him."

label nachos:
    vic "Oh Nachos! Those were super cheesy at some point."
    povname "'Yeah, but its nacho call now and I say it's soggyyy~'"
    vic "I take it back, that's waay cheesier"

label salad:
    vic "I see someone's on a diet. There's extra dressing on the side."
    povname "'Ranch, really?'"
    vic "I mean it's just spicy mayonnaise"
    povname "'Vic, no.'"

scene bg dorm with dissolve
povname "I finished the rest of the food and settled into bed"
povname "Never thought stacking books would take so much out of me. Hopefully tomorrow will be better. "
scene blank with dissolve
jump day4
#TODO: Fade to black?
