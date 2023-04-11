label day3:
show clock with dissolve
povname "'mmnh'"
povname "Well, I beat the alarm today."
play music "audio/alarm.mp3" volume 8 loop

scene bg dorm with dissolve


play music "audio/dorm.wav"
povname "I get ready for a morning of class and oh, my first day at work."

# spain peko

scene living day with dissolve
povname "Huh, I guess Vic has a morning class today."
povname "Oh, well. Off to class then."

scene outschool with dissolve
povname "I eventually reach the main building where my classes take place."

scene blank with dissolve
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
scene hello with dissolve
profe "On line 5, we can see the code to print out to the console."
profe "Now in this code there is only one data type, the main function."
profe "There are multiple data types in C++ and they can be split into three different classes."
profe "The most basic of which is Primary Data Types, these help us identify what data type a variable is."
scene dtype2 with dissolve
profe "These include the ones here."

profe "The next class is derived data types. These are data types that hold multiple instances of the same or different data types."
scene hello with dissolve
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
profe "For example, consider line 6 here."
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
show dtype2 with dissolve
povname "I wonder what happens when we assign a variable the wrong data type?"
scene classday with dissolve
show prof with dissolve
profe "Alright, that's all the learning we have for today. Dismissed"
povname "I should probably head out to the library"
scene libraryOut with dissolve
povname "This should be the place, I think."
scene libraryCounter with dissolve
povname "As I pass through the large glass entrance, a familiar face looks up at me."

show girl
povname "'Hi, I'm here to start work,I think.'"
lily "Ah, you're uhm... [povname] right? They told me there was a new hire"
lily "Right, I assume the boss has given you the whole onboarding schtick,eh?"
povname "I nod my head sheepishly."
lily "Ah, good. Here's your assignment for the day, you're stacking books over at Periodicals."


jump tetris3

label continue3:
    scene library with dissolve
    play music "audio/dorm.wav" loop
    show girl with fade
    if dog <= 1000:
        jump worst_ending3
    elif dog <= 1001:
        jump medium_ending3
    elif dog <= 1002:
        jump best_ending3

    label worst_ending3:
        lily "'You got a score of [dog]!'"
        lily "'That means you earned $5'"
        $money += 5
        lily "Nice try but you're still very new at this, huh?"
        lily "You'll get the hang of it soon."
        povname "Well, that could've gone better, but I still got paid so guess I'll go home."
        jump homeward3

    label medium_ending3:
        lily "'You got a score of [dog3]!'"
        lily "'That means you earned $10'"
        $money += 10
        lily "Not bad for a newbie."
        lily "You'll be a total pro in no time."
        povname "Well, that wasn't the best possible result, but I still got paid so guess I'll go home."
        povname "I then started walking home."
        jump homeward3
    label best_ending3:
        lily "'You got a score of [dog3]!'"
        lily "'That means you earned $20'"
        $money += 20
        lily "Wow, you're a natural at this."
        lily "Boss sure made the right hire."
        povname "'Ehe'"
        povname "Wow that was the best result, I got paid so I'll start going home."
        povname "I then started walking home."
        jump homeward3

label homeward3:

lily "Well then, remember to check the app for your schedules, but you already know that, right?"
povname "'The management portal?'"
lily "Yep, yep; that's right. See ya at the next shift."
povname "'Right, see ya then.'"
scene blank with dissolve
phone "At the end of each day, you will have an option to work at the library."
phone "Right now, you can come in to work whenever you're free. I guess that's called a flex hire?"
phone "Your payment depends on how well you do stacking the books."
phone "The higher your score, the more your pay!"
phone "So, make sure you try your best."
scene livingnight with dissolve
povname "'I'm back~'"
vic "Ah, look who's back, back again."
show vicNeutral with dissolve
vic "Have ya eaten? I ordered waaay too much. Feel free to take a plate and dig in."
povname "I looked at the whole smorgasbord on the table."
povname "There was half a cheesesteak, what was once some cheesy nachos and half a bowl of salad."
povname "I gave Vic a judgemental stare"
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
    vic "I see someone's on a diet. THere's extra dressing on the side."
    povname "'Ranch, really?'"
    vic "I mean it's just spicy mayonnaise"
    povname "Vic, no."

scene dorm night with dissolve

povname "I finished the rest of the food and settled into bed"
povname "Never thought stacking books would take so much out of me. Hopefully tomorrow will be better. "
scene blank with dissolve
$foo += 1

jump day4
