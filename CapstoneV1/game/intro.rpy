label intro:
#intro you wake up and greeted by roomate will have brief description who roomate is

show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop
#alarm "beep beep beep beep"

me "I woke up feeling groggy as my eyes started adjusting to my new surroundings."

me "Another nightmare, hope they don't keep happening even with me in college."
me "I turn off my alarm, and get up from my bed."

scene bg dorm with dissolve
play music "audio/dorm.wav" loop


me "I got up out of bed and started rushing to the restroom..."
me "..when I saw someone familar."

vic "'Seems like someone was hitting the snooze button a few times after all…'"
show vicNeutral with dissolve
#yeah nah yeah yah nah, no
#me "oh, it's Vic"
vic  "'Don’t sweat it, we got time.'"
vic  "'I made us some breakfast bagels. I’m gonna go save us some seats so don’t be late, sleepyhead!'"

me "Vic, short for Victor, is a classic chill liberal arts major, ready to talk to anyone about anything and extend a friendly hand."

me "I just met him a week ago, but we quickly got along like we've known each other since elementary school."

me "While I was daydreaming, Vic already left the bathroom."

me "I went back to my room, changed out of my pajamas and got ready to head out to new student orientation."



#next segment you are at school you see school

scene outschool with dissolve
me "I have to admit, I'm feeling a bit nervous."

#you walk to the desk see worker, player picks name
scene hall with dissolve
me "I enter the auditorium."
me "In front of me was a crowd of people crowded over tables."
me "It seemed like they were all looking through pamphlets and asking the volunteers about where they should go."
me "Maybe college isn't that different from high school I thought, starting to feel slightly less nervous."
me "But I still wasn't sure where to go, so I decided to ask one of the volunteers."
me "I walk up to the least crowded counter."
me "'Hey I'm here for new student orientation, and uhhh...'"
me " 'I'm not sure where to go?'"


show girl with dissolve
worker "'Sure, can I have your name please?'"
python:
    povname = renpy.input("Enter your name?")
    povname = povname.strip()

    if not povname:
         povname = "Player"

worker "'Let's see... this list, no, that one?'"
worker "'[povname] huh, hmm...'"
worker "'Alright [povname] you're in. Feel free to follow the line to your right and sit anywhere but the first three rows.'"

povname "'Why not the first three rows?'"

worker "'Those are for the professors and volunteers only.'"

povname "'Ah, alright then. Thank you.'"

scene aud with dissolve

#walking to aisle I was assigned in orientation

povname "As I was walking towards the seats I noticed Vic waving at me so I headed that way."

povname "It made me thankful that even in this strange new place I had someone to sit next to."

show vicNeutral with dissolve

vic "'Hey! you made it, I was getting bored sitting here twiddling thumbs.'"

vic "'I don't mind crowds but I didn't feel like forcing other people to talk, y'know?'"

povname "'I get what you mean, it's hard talking to people you barely even know.'"

povname "The hubbub subsided as I noticed an older looking person walking onto the stage."

hide vicNeutral

#orientation starts
unknown "'Hello new students and welcome to the wonderful world of po-'"
#TODO: change college name
conwell "'I mean welcome to “College name”, I am Dr. Conwell, the Dean of this campus.'"

povname "'This professor seemed very different than what I thought the dean would look like.'"


conwell "'I just wanted to welcome you all to our wonderful campus and will be handing off the rest of this orientation to Mr. Reena, head of student affairs.'"

povname "'I see a stout man get up from the seat, lightly trip on nothing, but manage to recover, and finally grab the microphone from Dr. Conwell.'"

show reena with dissolve
reena "'Thank you Dr. Conwell for the warm welcome and introduction. My name is Mr. Reena and I would like to go over some key locations on campus.'"

povname "'I hear a lot of whispering going around me.'"

vic "'Did ya see that?'"
vic  "'He reminds me of you on move-in day.'"

povname "'Oi! Like you were any better carrying your groceries from Jamie’s car…'"

vic "'Yeah, yeah fine~'"

# Hey, Maybe show time passing here?

reena "'And that concludes the most important campus locations that all you students should get to know.'"

reena "'Don’t worry if you forget the locations, you can always look at the given pamphlets or just look online.'"

reena "'Feel free to explore our lovely campus after this afternoon’s ice cream social!'"

povname "'Oh shoot Vic, you made us miss the whole thing'"

vic "'Eh. *shrugs* I wouldn’t sweat it too much, we can just go look at ‘em later tonight.'"

povname "'Sounds like a plan.'"
scene blank with dissolve
povname "'We decide to return home after and put all the goodies we recieved from the event.'"

scene living day with dissolve

show vicNeutral with dissolve
vic "'That ice cream was great! We got to meet the other students, and everyone's so friendly here.'"

povname "'Yeah, everyone seemed pretty chill.'"

povname "'I still can't believe that the school used to be a pickle farm.'"

vic "'You gotta get them sodium sticks somehow.'"

#following exchange seems contrived
vic "'So, whatcha wanna do now since we're free until the first day of class tomorrow? '"
vic "'I think I'm gonna chill here and relax, ice cream doesn't sit well with me, but I just can't resist~'"

povname "'Ummm well... What do I do now?'"

menu:
    extend''
    "Go back to my room and relax":
        play sound "audio/confirm.wav"
        jump relax

    "Explore campus":
        play sound "audio/confirm.wav"
        jump tour

    "Finish unpacking your stuff":
        play sound "audio/confirm.wav"
        jump unpack


label relax:
    povname "'I think I'm going to go back to my room and just relax.'"
    povname "'I want to be at full energy for day 1 of class.'"
    show vicNeutral with dissolve
    vic "'Alright sounds like a good idea, see you tomorrow then.'"
    hide vicNeutral
    scene dorm night with dissolve
    povname "I go back to my room, lay on my bed and realize that tomorrow is my first day of class."

    $ stress -= 1
    povname "Both excited and nervous, I feel ready for my first day of CS to begin."
    scene blank with dissolve
    unknown "'Because you went to bed early you feel well rested and lost a point of stress.'"
    jump stattuto



label tour:
    povname "'I think I'm going to explore campus a bit more.'"
    povname "'I'm feeling a bit nervous and want to see a little more of campus before classes start.'"
    povname "'I mean, it wouldn't hurt to see where things are, right?'"
    show vicNeutral with dissolve
    vic "'Alright sounds like a good idea, see you tomorrow then.'"
    hide vicNeutral
    scene hall with dissolve
    povname "I go back to campus and start wandering the halls."
    povname "Upon exploring I look for the classrooms for my first day of class."
    povname "While most of them are easy to find, one of them was in an awkward hallway that had me lost."
    povname "Feeling happy that I explored campus I return back to my dorm."
    scene dorm night with dissolve
    povname "I return to my room, lay on my bed and realize that tomorrow is my first day of class."
    povname "Both excited and nervous, I feel ready for my first day of CS to begin."
    scene blank with dissolve
    $ knowledge += 1
    unknown "'Because you decided to explore campus your knowledge of the area went up you gained a point of knowledge.'"
    jump stattuto



label unpack:
    povname "'I think I'm going to finish unpacking all my stuff.'"
    povname "'I think it's about time I actually unpack everything.'"
    show vicNeutral with dissolve
    vic "'Alright sounds like a good idea, see you tomorrow then.'"
    hide vicNeutral
    povname "A place for everything and everything in it's place, or something. At least it's not in boxes anymore."
    scene dorm night with dissolve
    povname "While unpacking my stuff I found a 10 dollar bill!"

    povname "I added it to my wallet feeling happier."
    $ money += 10
    unknown "'Because you decided to clean up your stuff you were able to find some money.'"
    jump stattuto

label stattuto:
    scene blank with dissolve

    unknown "'On the top right of the screen you will find the STATS button. Click it and it will show your current stats.'"
    unknown "'The choices you make throughout the game will affect them.'"
    unknown "'Make sure to keep that in mind as you make your choices!'"
    jump day1

##day 1 begins
