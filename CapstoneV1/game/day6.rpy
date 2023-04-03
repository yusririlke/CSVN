label day6:
show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop

povname "guh..."
povname "I roll over to my alarm clock and hit the stop button."
povname "'Guess I'm on time today.'"
povname "After trying my best impression of an annoyed cat stretching out of its nook, I start getting ready for the day."

hide clock with dissolve
scene bg dorm
play music "audio/dorm.wav" loop

povname "I should probably shower and refresh for today."
#TODO:fade in fade out, like time passing kinda deal
povname "You know, lamps in videogames use real elctricity. hmm"
povname "Putting on something vaguely acceptable I headed out to the common area."

scene living day with dissolve
vic "Hello there."
show vicNeutral with fade
povname "'Ah, Jenderal Kenobi...'"
vic "Heh."
vic "Well, are ya gonna be working late again today, or are ya gonna come back early?"

menu:
    extend''
    "I'll probably be working late":
        play sound "audio/confirm.wav"
        jump worklate
    "I'll be back early":
        play sound "audio/confirm.wav"
        jump comeback
    "We'll see...":
        play sound "audio/confirm.wav"
        jump indecisive

label worklate:
    povname "'I think they'll need me at the library. We just recieved a large order of the new textbooks.'"
    povname "'Somebody has to sort them out'"
    vic "I guess so, well go get that bread then."

label comeback:
    povname "'I have a long enough day ahead. Maybe we'll meet at lunch and —'"
    vic "Yo! that means you're gonna be around for — Oh wait."
    povname "Eh?"

label indecisive:
    povname "'I'm not too sure yet'"
    povname "'On the one hand, they would probably need my help at the library today'"
    povname "' On the other hand, I've done a good amount of work, I think."

vic "So, are we still on for lunch, then?"
povname "Oh, absolutely. I'll see you at lunch"
vic "okie doke."

scene outschool with dissolve
povname "Well, I heard today's class is going to be a little more complex."

scene classday with dissolve
povname "Class seems like it's a little more packed today."
povname  "I wonder if that has anything to do with the exam?"
povname "After a while, I notice Professor Array enter the class."

show prof with dissolve
profe "Good day, class."
profe "Wow, we have a sell out crowd today. Always nice to see some old faces around here"
profe "For those in the back, how goes it? Haven't seen you in a while."

povname "I glance over at them. I've seen those people before."
povname "They're usually very loud and on campus."
povname "Now, they jsut seem a little sheepish as they awkwardly look down at their notebooks."

profe "Anyway."
profe "On to today's topic, we're gonna have a little chat about signposts and arrows."
povname "Eh?"
povname  "Oh no, it's already confusing..."
profe "I'm talking of course, about pointers."
#TODO: Add and edit pointer1
show pointer1 with dissolve
profe "Now let's see if you can spot he pointer."
profe "Anything seem so familiar, yet so foreign?"

povname "Wait, why is that int on line 6, uh starry?"

profe "Alright, I see some co9nfused looks in here."
profe "For those of you yet to cotton on, look at line 6."
profe "That is how a pointer is initialised."
profe "The declaration int* means that it's a pointer and on top of that, a pointer to an int."
profe "Now, notice its not being assigned an int, not directly, anyway."
profe "The assignment..."

povname "Assignment? Oh, like assigning to a variable..."

profe "... is actually something we'll talk about soon."
profe "Now that you know what a pointer looks like, what is it exactly?"
profe "Well, a pointer is a special kind of variable that takes in an address of the matching data type."
profe "In other words, its a data type that holds an address to a different variable."
profe "You can think of it as a signboard that has the directions to another variable."
profe "Coming back to our example."
profe " Remember the weird &num assignment?"
profe "In C++ , the & operator returns the address of the object, allowing our pointer to, well, point to it."
profe "Here, we can see that it's given the address of the variable num."
profe "Any ideas what this would output when we print out *ptr?"

povname "Errr, I think it's..."

menu:
    extend''
    "The address of num?":
        play sound "audio/confirm.wav"
        jump wrongans
    "The value of num?":
        play sound "audio/confirm.wav"
        jump  rightans
    "AAAA, I'm not sure":
        play sound "audio/confirm.wav"
        jump panik

label wrongans:
    povname "I raise my hand."
    povname "'The address?'"
    profe "Of...?"
    povname "...num?"
    profe "Good guess but not quite."
    $ knowledge += 1

label rightans:
    povname "I raise my hand.The value of num should be..."
    povname "'5?'"
    profe "So just the integer, five?"
    povname "'I think so?'"
    profe "Well, you thought absolutely right. Good job."
    $ knowledge += 2

label panik:
    povname "I look down at my notes, well then I think.."
    profe "Well, then let me tell you."

profe "The output is  5."
profe "So what happens here is that cout looks at *ptr and goes"
profe "'Ah, that's a pointer. I should go to the address it's pointing to.'"
profe "And then it goes to the address, which is that of num"
profe "It then looks at num and goes"
profe "'This is what I need to print out'"
profe "And that's why it prints out 5."

povname "That's cool and all, but why?"

profe "Some of you may be thinking, what's the point of this?"
profe "Why are we passing the address, wouldn't it be easier for us to just pass the variable?"
profe "Well, there are a few advantages to being able to pass and manipulate an address."

profe "For example, somethign that you will learn later down the line is pass by value and pass by reference"
profe "The quick version of this is that say you want to process a copy of that value instead of the value itself."
profe "Pointers will allow you to do that."
profe "Another thing you will learn about is polymorphism and inheritance"
profe "To cut a long story short, pointers are used extensively in implementing those concepts."
povname "Alright so it seems fairly important then."

profe "Alright, before you leave, a reminder that our first exam is during our next session."
profe "It will take place here, and yes..."
profe "You are allowed stationery."

povname "Hilarious, professor. Hilarious."

profe "Now it wil cover all the topics that we've encountered so far, including today's."
profe "So remember to read through and understand all the core concepts."
profe "Remember, this exam will gauge your understanding so that we can see where we need to improve."
profe "Think of it like a celebration of knowledge."
profe "Alrighty, dismissed"

povname "Celebration of knowledge, huh?"
povname "Poring out with the masses, I headed for the cafeteria. All these pointers are pointing towards me getting lunch."

scene cafeteria with dissolve
povname "I queued up with the rest and picked out my food. I still think that the price hike is a little steep."
povname "Just when I get money, I lose it all again."
povname "I sit down at one of the tables"
povname "sigh~"

show vicNeutral with dissolve
vic "That was a loong sigh bud. All good?"
povname "'Yeah, all good. It's just about the exam tomorrow, I'm kinda nervous.'"
vic "Yeah I getcha. It's not like I'm making any progress on kmy assignment either."
vic "I'm just not inspired, y'know?"
povname "'Alright then, Picasso...'"

povname "I finished the rest of my meal as I listen to Vic talk about their assignment."

povname "Well, I must be leaving now. I'm headed to..."
menu:
    extend''
    "work":
        play sound "audio/confirm.wav"
        jump workC
    "study":
        play sound "audio/confirm.wav"
        jump studyC
    "the apartment":
        play sound "audio/confirm.wav"
        jump homeC

label workC:
    povname "'I need to help them arrange the new inventory after all.'"
    jump libWork

label studyC:
    povname "'Guess I'm headed to study, I need to work for that exam tomorrow.'"
    jump vicC

label homeC:
    povname "'I'm a little burnt out and I'm gonna need to recover for the exam tomorrow.'"
    jump vicC

label vicC:
    vic "Alright then, stay safe."
    vic "And don't push yoursel too hard."
    povname "I'll try not to. Thanks."
    jump homeward
label libWork:
    #TODO: Library_exterior show here
    povname "I'll work for a bit, I guess."
    #TODO: Show library interior here.
    show girl with dissolve
    lily "OH, thank goodness, you're here. We're quite busy right now so please lend us a hand."
    #TODO: Implement tetris here:p
    jump homeward

label homeward:
    povname "I slowly made my way home."
    scene bg dorm
    povname "'I have to study for tomorrow."
    #TODO: SHow passing time
    povname "Well, that was tiring."
    $ knowledge+=2
    povname "I changed and dove headfirst into my bed, narrowly missing the bedpost"
    povname "Tomorrow's a big day. I have to stay rested."
    povname "As I drifted off, I wondered, do robots REALLY dream of electric sheep."
    screen blank with dissolve
    #jump day7
