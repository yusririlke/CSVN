label day7:
show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop
povname "I woke up with a clearer mind than usual."
povname "Guess my brain was ready for today's exam."
hide clock with dissolve
scene bg dorm
play music "audio/dorm.wav" loop
povname "I get a new pair of clothes out of my drawer, and start heading to the shower."
scene blank with fade
povname "I hope I do well today."
scene living day with dissolve
vic "'Hey, how are you doing."
show vicNeutral with fade
povname "'Well I have an exam today in CMPSC 111 class.'"
vic "'Oh how are you feeling about that?'"
povname "'Well...'"
menu:
    extend''
    "Feeling Confident!":
        povname "I think I'm good, I've done everything I could."
        play sound "audio/confirm.wav"
        jump day7c
    "I think I'll be fine?":
        povname "Not feeling the most confident, but I think it'll be okay."
        play sound "audio/confirm.wav"
        jump day7c
    "We'll see...":
        povname "I'm not feeling the most confident, but we'll see..."
        play sound "audio/confirm.wav"
        jump day7c

label day7c:
    vic "'Ah I see, well good luck with that."
    vic "'In other news what you want for breakfast?'"
    povname "'The usual not like we got many other choices, pass me the cereal.'"
    povname "We wasted a bit of the morning talking about nothing of a particular importance."
    povname "After using up the last of our cereal we packed out bags and got ready for school."
    scene outschool with dissolve
    vic "'What you gonna do after classes today?'"
    show vicNeutral with fade
    povname "'I don't know yet, I am feeling kind of tired so maybe I'll head home early.'"
    vic "'Sounds viable I was going to do the same thing.'"
    povname "I got to the usual spot where Vic and I split up."
    vic "'Well see you after classes for lunch, you only have the one class today right?'"
    povname "'Yeah my second gen ed got cancelled, professor said he had a personal emergency.'"
    vic "'Yeah that's something you only see in college, well see you later!'"
    hide vicNeutral with fade
    povname "I watched as vic went to his classroom, and I started looking at my phone doing some last minute review."
    scene classday with dissolve
    povname "I wanted to arrive earlier to the classrom than usual just in the professor hands out the exam early."
    povname "With that thought I walked slightly faster than normal, when entering the classroom I noticed a more tense environment than usual."
    povname "There were very few people talking, and people either glued to to their textbook or their phones."
    povname "'Yeah this is what I imaged the classroom before an exam would be like.'"
    povname "I sat down at my usual seat, and started taking out my usual supplies when the professor walked."

    show prof with dissolve
    profe "'Good morning class today is exam day put away everything that isn't a writing utensil, eraser, or water.'"
    profe "'If I see a phone out for any reason during the exam I'll automatically be giving you a 0 so make sure they're turned off and in your bag.'"
    povname "The professor started hanging out sheets of paper one by one to everyone in the classroom."
    povname "After completing the first few rows I got my sheet of paper."
    profe "'The front page is for you to put your name and section number, this is section 1.'"
    profe "'Do not turn to the exam untill I tell you to.'"
    povname "I put my name down as well as Section Number 1 into the correct boxes."
    povname "Then I watched as professor Array continued to hand out the exams."
    povname "Wouldn't it be better for him to just pass a stack of papers and let the students pass it around I thought."
    profe "'Alright the exam has been passed to everyone, whenever you're ready turn the page and start.'"
    povname "I flip to the first page of the exam."
    povname "The first question says: Given the following code what would the output be?"
    show final1 with dissolve
    povname "Hmm, this looks like a normal cout << code"
    povname "If it works it would just print What is your favorite animal."
    povname "But I feel like something is wrong what is it."

    menu:
        extend''
        "They forgot to include semi colons!":
            povname "That's right there's no semi colons so the compiler would just say there's a syntax error."
            $finals += 1
            play sound "audio/confirm.wav"
            jump day7q2
        "The cin should be a part of the cout":
            povname "I think the cin statement is wrong?"
            povname "Not feeling confident I enter what I think is the correct answer."
            play sound "audio/confirm.wav"
            jump day7q2
        "Why am I here":
            povname "Why did I ever pick this major..."
            povname "Wait I'm wasting time I need to go to the next question"
            play sound "audio/confirm.wav"
            jump day7q2

label day7q2:
    hide final1
    povname "Ok next question, it seems like a simple multiple choice question."
    povname "Which of these data types are not real?"
    menu:
        extend''
        "bool":
            povname "I don't remember ever seeing this one."
            play sound "audio/confirm.wav"
            jump Question3
        "character":
            povname "This is clearly the wrong answer it should be char"
            $finals += 1
            play sound "audio/confirm.wav"
            jump Question3
        "double":
            povname "I think double is wrong most people use int right?"
            povname "Wait I'm wasting time I need to go to the next question"
            play sound "audio/confirm.wav"
            jump Question3


label Question3:
    povname "Alright next question."
    povname "Looks like this question is about loops"
    show final3 with dissolve
    povname "Given the code below what will the output be"
    povname "It looks like a simple while loop."
    povname "The variable i starts at 0 and increments itself untill 5 so the out would be something like?"
    menu:
        extend''
        "5":
            povname "It would print 5 because that's where it stops."
            play sound "audio/confirm.wav"
            jump day7q4
        "4":
            povname "It would print 4 because that's where it stops."
            play sound "audio/confirm.wav"
            jump day7q4
        "0 1 2 3 4":
            povname "It prints every number untill it reaches 5 so this is the only correct solution!"
            $finals += 1
            play sound "audio/confirm.wav"
            jump day7q4

label day7q4:
    hide final3
    $ zero = 0
    $ one = 1
    povname "Next is a question on arrays."
    povname "Let's see this might be harder than the other questions."
    povname "Can you finish the code below to print Car 1"
    show final4 with dissolve
    povname "Ok so this is a question about printing the correct entry of an array."
    povname "It looks like the part missing is after cout so I just finish what's there."
    menu:
        extend''
        "I think it is cout << cars\[0\]\;":
            povname "When printing arrays the first entry is 0 so this is the correct option."
            $finals += 1
            play sound "audio/confirm.wav"
            jump day7f
        "I think its cout << cars\[1\]\;":
            povname "I think when printing arrays the first entry is 1 so this is the correct option."
            play sound "audio/confirm.wav"
            jump day7f
        "I think its cout << cars":
            povname "I think this is the correct way to print it?"
            play sound "audio/confirm.wav"
            jump day7f


label day7f:
    hide final4
    povname "Ok finally, this looks like the last question."
    povname "Ah, it's the part I felt least confident in pointers."
    povname "Ok, it says Write a function which will take pointer and display the number on screen. Take number from user and print it on screen using that function."
    povname "Hmm, I got a start on writing it but how can I finish this?"
    show final5 with dissolve
    povname "I'm not sure what to put in this cout, what was it again?"
    menu:
        extend''
        "&x":
            povname "That's right I'm trying to call the memory address so it should be &x"
            $finals += 1
            play sound "audio/confirm.wav"
            jump day7end
        "*x":
            povname "I wasn't sure so I put the second options"
            play sound "audio/confirm.wav"
            jump day7end
        "$x":
            povname "I wasn't sure so I put the final option"
            play sound "audio/confirm.wav"
            jump day7end


label day7end:
    hide final5
    povname "With that I finished every question and turned in my exam."
    povname "I was surprised by the fact that I was one of the earlier people turning it in."
    profe "'Wait before you go I can check your grade.'"
    profe "'You got a score of [finals] out of 5'."
    if finals < 1:
        jump day7a
    if finals < 2:
        jump day7b
    if finals < 3:
        jump day7c
    if finals <4:
        jump day740
    if finals < 5:
        jump day7e
    if finals < 6:
        jump day7100


    label day7a:
        profe "'That means you got a 0 percent did you even try to pay attention?'"
        jump day7post
    label day7b:
        profe "'That means you got a 20 percent were you skipping a few days?'"
        jump day7post
    label day740:
        profe "'That means you got a 40 percent try harder on the next exam.'"
        jump day7post
    label day7d:
        profe "'That means you got a 60 percent acceptable but try harder.'"
        jump day7post
    label day7e:
        profe "'That means you got a 80 percent, good job keep paying attention.'"
        jump day7post
    label day7100:
        profe "'That means you got a 100 percent, keep up the good work.'"
        jump day7post

    label day7post:
        povname "I started walking outside the classroom"
        hide prof
        povname "With my finished exam, I was just glad it was over with."
        povname "I went to go meet Vic at the cafeteria."
        scene cafeteria with dissolve
        povname "I headed to the register."
        povname "The price of lunch went back to 5 so I was glad to pay less"
        $ money -=5
        vic "'Hey how'd your test go?'"
        show vicNeutral with fade
        povname "'Don't want to think about it anymore.'"
        vic "Ah I see well I got a story to tell you."
        povname "Vic kept telling his story about how someone in his class roleplayed as a lion for 30 minutes."
        povname "I thought it was funny, and since I didn't have my second class I decided to hang out with Vic after class."
        povname "We wasted a few hours walking around the city and went back home."
        jump day7home

    label day7home:
        scene dorm night with dissolve
        povname "When I got back home it was already the evening."
        povname "I went back to my room, and layed on my bed"
        povname "Wow already finished my first CMPSC exam."
        povname "The material I learned was interesting, I wonder what other concepts they could teach though."
        povname "I layed me head on my pillow thinking that I wanted to learn more."
        scene blank with dissolve

        povname "And soon sleep embraced me in her arms, and I felt my consciousness fading."
