label intro:
#intro you wake up and greeted by roomate will have brief description who roomate is

show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop
alarm "beep beep beep beep"

me "I woke up feeling groggy as my eyes started adjusting to my new surrounds."

me "Another nightmare, hope they don't keep going even with me in college."
me "I turn off my alarm, and get up from my bed."
hide clock with dissolve
scene bg dorm
play music "audio/dorm.wav" loop


me "I got up out of bed, and started rushing to the restroom when I saw someone familar."

vic "'Seems like someone’s was hitting the snooze button a few times, after all…'"
show vicNeutral with dissolve
vic  "'Don’t sweat it, we got time, also made us some breakfast bagels. I’m gonna go save us some seats, don’t be late sleepyhead!'"

me "Vic short for Victor is a classic chill liberal arts major, ready to talk to anyone about anything and extend a friendly hand."

me "I just met him a week ago, but we quickly got along like we've known each other since elementary school."

me "I realize that while daydreaming Vic already left the bathroom."

me "I went back to my room and changed out of my pajamas and got ready to head out to new student orientation feeling a bit nervous."

#next segment you are at school you see school


#you walk to the desk see worker, player picks name
scene hall with dissolve
me "I walk into the auditorium."
me "In front of me was a crowd of people crowded over tables."
me "It seemed like they were all looking through pamphlets and talking to the workers about where they should go."
me "Maybe college isn't that different from high school I thought, starting to feel slightly less nervous."
me "But I still wasn't sure where to go, so I decided to ask the girl in front of me."
me "I walk up to the counter that had the least amount of people."
me "'Hey I am here for new student orientation, and I'm not sure where to go can you help me.'"


show girl with dissolve
worker "'Sure can I have your name?'"
python:
    povname = renpy.input("Enter your name?")
    povname = povname.strip()

    if not povname:
         povname = "Player"

worker "'Alright [povname] you're on the list feel free to follow the line to your right and sit anywhere except the first 3 rows.'"

povname "'Why not the first three rows?'"

worker "'Those are for professors and workers only.'"

povname "'Oh that makes sense, thanks for answering have a nice day.'"

scene aud with dissolve

#walking to aisle I was assigned in orientation

povname "When I started walking towards the bleachers I noticed Vic waving at me and started walking towards him."

povname "It made me thankful that despite the new environment I still had someone to sit next to."

show vicNeutral with dissolve

vic "'Glad to see you made it, I was getting bored sitting here doing nothing.'"

vic "'I don't mind crowds but I didn't feel like forcing other people to talk to me.'"

povname "'I get what you mean it's hard talking to people you don't know.'"

povname "'After a bit of down time I noticed an older looking lady walking onto the stage.'"

hide vicNeutral

#orientation starts
unknown "'Hello new students and welcome to the wonderful world of po-'"
#remember to change college name
conwell "'I mean welcome to “College name”, I am Dr. Conwell, the Dean of this campus.'"

povname "'I thought that this professor seemed very different than what I had initally thought the dean would be like.'"


conwell "'I just wanted to greet you all to our wonderful campus and will be handing off the rest of this orientation to Mr. Reena, head of student affairs.'"

povname "'I see a stout man get up from he seat, lightly trip on nothing, but manage to recover, and finally grab the microphone from Dr. Conwell.'"

show reena with dissolve
reena "'Thank you Dr. Conwell for the nice warm welcome and introduction. My name is Mr. Reena and I would like to go over some key locations on campus.'"

povname "'I hear a lot of whispering going around me.'"

vic "'Did ya see that?'"
vic  "'He has the foot-eye coordination of you on moving day.'"

povname "'Like you were any better carrying out your groceries from Jamie’s car…'"

vic "'Yeah yeah finee…'"

reena "'And that concludes our most prevalent campus locations that all incoming students should get to know.'"

reena "'Don’t worry if you forget the locations, you can always look at the pamphlets that were on your seats or just look online.'"

reena "'Feel free to explore around after this afternoon’s ice cream social!'"

povname "'Oh shoot Vic, you made us miss the entire orientation.'"

vic "'Eh. *shrugs* I wouldn’t sweat it too much, we can just go look at ‘em later tonight.'"

povname "'Sounds like a plan.'"

povname "'We decide to return home after the event to put all the goodies you recieved from the event.'"

scene bg dorm with dissolve

show vicNeutral with dissolve
vic "'That ice cream was great! We got to meet the other students, and everyone's so friendly here.'"

povname "'Yeah, everyone seemed pretty chill.'"

povname "'I still can't believe that school used to be a pickle farm.'"

vic "'You gotta get them sodium sticks somehow.'"

vic "'So, whatcha wanna do now anyways we're free untill the first day of class tomorrow? I think I'm gonna chill here and relax, ice cream doesn't sit well with me, but it's my weakness.'"

povname "'Ummm well... What am I going to do?'"

menu:
    "Go back to my room and relax":
        play sound "audio/confirm.wav"
        jump relax

    "Tour campus":
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
    povname "I go back to my room, lay on my bed and realize that tomorrow is my first day of class."
    $ stress -= 1
    povname "Both excited and nervous, I feel ready for my first day of CS to begin."
    scene blank with dissolve
    unknown "'Because you went to bed early you feel well rested and lost a point of stress.'"
    unknown "'On the top right of the screen you will be able to see your stat window and choices you make throughout the game will change them.'"
    unknown "'Make sure to keep that in mind as you make your choices!'"
    jump day1




label tour:
    povname "'I think I'm going to tour campus a bit more.'"
    povname "'I'm feeling a bit nervous and want to look around a bit more of campus before classes start.'"
    show vicNeutral with dissolve
    vic "'Alright sounds like a good idea, see you tomorrow then.'"
    hide vicNeutral
    scene hall with dissolve
    povname "I go back to campus and start touring the hall."
    povname "Upon exploring I look for the classrooms of my first day of class."
    povname "While most of them are easy to find, one of them was in a direction that made me get lost."
    povname "Feeling happy that I explored campus I return back to my dorm."
    scene bg dorm with dissolve
    povname "I go back to my room, lay on my bed and realize that tomorrow is my first day of class."
    povname "Both excited and nervous, I feel ready for my first day of CS to begin."
    scene blank with dissolve
    $ knowledge += 1
    unknown "'Because you decided to explore campus your knowledge of the area went up you gained a point of knowledge.'"
    unknown "'On the top right of the screen you will be able to see your stat window and choices you make throughout the game will change them.'"
    unknown "'Make sure to keep that in mind as you make your choices!'"
    jump day1



label unpack:
    povname "'I think I'm going to finish packing all my stuff.'"
    povname "'I think it's about time I actually unpack everything.'"
    show vicNeutral with dissolve
    vic "'Alright sounds like a good idea, see you tomorrow then.'"
    hide vicNeutral
    povname "While unpacking my stuff I found a 10 dollar bill!"
    povname "I added it to my wallet feeling happier."
    $ money += 10
    povname "I go back to my room, lay on my bed and realize that tomorrow is my first day of class."
    povname "Both excited and nervous, I feel ready for my first day of CS to begin."
    scene blank with dissolve
    unknown "'Because you decided to clean up your stuff you were able to find some money.'"
    unknown "'On the top right of the screen you will be able to see your stat window and choices you make throughout the game will change them.'"
    unknown "'Make sure to keep that in mind as you make your choices!'"
    jump day1










##day 1 begins
