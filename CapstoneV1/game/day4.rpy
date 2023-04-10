label day4:
show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop

povname "..."
povname "'Ugh, it's time to get up already.'"
povname "'I feel more tired than usual, guess working at the library got me tired.'"
povname "I get out of my bed give myself a big stretch and turn off the alarm blasting at my ears."

hide clock with dissolve
scene bg dorm
play music "audio/dorm.wav" loop

povname "After getting up I realized that while I still struggled getting up in the morning, I haven't had the reocurring nightmares from highschool."
povname "'Guess I've been too busy to think about them recently."
povname "I change into a new pair of clothes and head out to the common area."
povname "Walking into the common area I see no sign of Vic."
povname "'Well that's new did I wake up earlier than him today?"
povname "'Right on cue of me saying this I see a slightly disheveled looking Vic walk out of his room."

show vicNeutral with fade

povname "'Morning Vic, rare for you to get up later than me."
vic  "'Morning [povname], I know, I was super busy yesterday.'"
vic "'My professor assigned us our first big project.'"
vic "'Don't get me wrong I still prefer having projects over exams, but they are a lot of work."
povname "'I get what you mean, Still I think it's nice your major doesn't have any exams and it's replaced with projects."
vic "'Speaking of when is your first exam.'"
povname "'I doubt it's any time soon, classes just started."
povname "'Maybe in a few weeks?"
vic "'Ah I see, anyway let's eat some breakfast and start getting ready for class yeah?'"
povname "'Yeah, I'm starving work yesterday tired me out.'"
vic "'Ah that's right you're working at that library now right, how is that.'"
povname "'The pay is nice, but I feel like I'm going to have to do it a few more times before I get used to it.'"
vic "'Yeah that makes sense, sounds like any job.'"
vic "'Anyway which cereal you want.'"
povname "'Give me the usual, Kicks cereal is the best there is."
povname "After eating breakfast we got ready to leave and take the normal walk to school."
hide vicNeutral
scene outschool

povname "On the way walking to school, I saw a familar face."
show girl with dissolve
lily "'Hey [povname]! are you going to work today?'"
lily "'You were a huge help yesterday!'"
povname "'Oh uh, yeah I'll probably go.'"
lily "'Really that would be great!'"
lily "'I'll see you same time today then!'"
hide girl
povname "'I wasn't planning on going to work again today but... maybe I should go?'"
show vicNeutral
vic "'Was that your boss?'"
povname "'Nope, just another person working at the library.'"
vic "'Ah I see, well if you're going again good luck.'"
vic "'You looked dead tired after going last time.'"
povname "'Yeah well it should be easier today, I got a bit used to it after last time.'"
povname "I continued walking to CMPSC 111 and seperated with Vic when we got to his classroom."
hide vicNeutral
scene classday
povname "I arrived a minute before class was going to start."
povname "A bit later than I normally get in but still early."
povname "I noticed while looking around that the class had a few empty seats."
povname "Few people are skipping I guess."
povname "With those thoughts popping into my head I see professor Array walking in."
show prof with dissolve
profe "Alright everyone settle down, I have an announcement to make."
profe "Today marks the 4th day of class, at the start of day 7 there will be an exam covering everything I've taught so far as well as what I will teach on Days 4-6."
profe "This will be the first major grade for this class so prepare for it."
povname "There's an exam already!?"
povname "I was literally just talk to Vic about this, and I thought there wasn't going to be one for a few weeks!"
povname "Actually thinking about it again an exam this early means there's going to be less covered on the exam so it might not be that bad."
povname "I also thought that I felt bad for the people that skipped the announcement today."
povname "I thought to myself it might be a very bad idea to skip classes with professor Array..."
profe "'Alright enough grumbling I'm going to start to start today's lecture.'"
profe "'Last class we covered Data Types, don't forget that they're going to be important when we cover class today.'"
profe "'Today's class is going to cover loops.'"
profe "'The first question what is a loop?'"
profe "'A loop is a block of code who's purpose is to execute something as many times as you ask it to.'"
profe "'Let's take for example the code we showed back in day 2.'"
show hello with dissolve
profe "'Just as review the purpose of this code is to print Hello World one time.'"
profe "'But what if you wanted it to say Hello world two times, or maybe three times?"
profe "'Well that wouldn't be so hard it would be as simple as just copy and pasting the cout statement a few more times."
show hello2ce with dissolve
hide hello
profe "'Simple isn't it, it's just writing the same statement again."
profe "'But what if you wanted it to print Hello World 100 times?"
profe "'This would be doable if you copy pasted it 100 times, but what if you wanted to do it 1,000,000 times?'"
profe "You get the idea well loops is a great way to deal with that issue."
profe "I am going to show you the skeleton of a basic loop and explain each bit."
profe "This will be code to print Hello World five times."
show whilel with dissolve
hide hello
profe "'In this bit of code we are successfully printing Hello World five times.'"
profe "'First I'm going to be going over this int i = 0'"
show whilel2 with dissolve
hide whilel
profe "'This is similar to what we did last class."
profe "'This is simply stating that there is a variable named i with a value of 0."
show whilel3 with dissolve
hide whilel2
profe "'Next is this while statement'"
profe "'While is similar to an if statement.'"
profe "'The key difference is that a while statement will run through the condition an infinite amount of times untill the statement is false."
profe "'So here the condition is that i < 5.'"
show whilel4 with dissolve
hide whilel3
profe "'The next bit is obvious it is just saying to print Hello World."
show whilel5 with dissolve
hide whilel4
profe "'Finaly this i++ is saying to make i one value higher than it was before.'"
profe "'For our purpose i = 0, and now when i++ happends i = 1.'"
profe "'Now if this was an if statement it would be complete but because it is a while statement it will check the function again.'"
show whilel3 with dissolve
hide whilel4
profe "'Now here at while it will check if i is < 5 and and at the time i = 1 so it will run through the program again.'"
profe "'After it runs through the program i = 2 and go through it again untill i = 5.'"
profe "'At the time i = 5 the while statement will no longer be true therefore it will not print Hello World again."
profe "'Thus you have successfully printed Hello World 5 times."
profe "'You can do this with any number of iterations, which is what makes loops so useful."
profe "'That concludes this lesson, I'm going to be assigning some homework over what was taught today in class do it at home and return it tommorow."
hide whilel3
hide whilel2
hide whilel1
hide whilel
hide prof
scene classday

povname "I gathered my things and got ready to leave the classroom."
povname "After leaving the classroom I headed to all my other gen ed classes and finished class sometime in the afternoon."
povname "I also had lunc with Vic and lost some money."
$money -= 5
povname "Alright, I finished all my classes what should I do now?"
menu:
     "Go to work at the library":
        play sound "audio/confirm.wav"
        jump lib4
     "Go back home and rest":
        play sound "audio/confirm.wav"
        jump rest4





label rest4:
scene bg dorm
povname "I decided to get some rest, classes today were tiring."
povname "I started walking back home."
povname "When I got home I saw Vic using swetch to play some Werio Kart."
povname "I decided to join him and had a good time."
$stress -= 1
phone "You had a good time playing video games with your friend, and you lost a point of stress."
jump hw4


label lib4:
povname "I thought it was best I go to work, I did promise after all."
povname "I start walking to the library."
scene libraryCounter with dissolve
show girl with fade
lily "'You came to help, thank you!'"
lily "'Today is going to be more of the same from last time do your best!'"
hide library
hide girl
jump tetris


label continue4:
scene library with dissolve
show girl
play music "audio/dorm.wav" loop
show girl with fade
if dog >= 20:
    jump worst_ending
elif dog >= 50:
    jump medium_ending
elif dog >= 100:
    jump best_ending

label worst_ending:
    lily "'You got a score of [dog]!'"
    lily "'That means you earned $5'"
    $money += 5
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Well, that wasn't the best possible result, but I still got paid so guess I'll go home."
    povname "I then started walking home."
    jump hw4

label middle_ending:
    lily "'You got a score of [dog]!'"
    lily "'That means you earned $10'"
    $money += 10
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Well, that wasn't the best possible result, but I still got paid so guess I'll go home."
    povname "I then started walking home."
    jump hw4
label best_ending:
    lily "'You got a score of [dog]!'"
    lily "'That means you earned $20'"
    $money += 20
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Wow that was the best result, I got paid so I'll start going home."
    povname "I then started walking home."
    jump hw4



label hw4:
scene dorm night with dissolve

povname "After finishing everything from before. I returned to my desk."
povname "Guess it's time I started working on that homework."
#TODO:jump hw4
scene blank with dissolve
jump end4


label end4:
scene dorm night with dissolve
povname "Today felt like an even longer day than yesterday."
povname "I just want to get some sleep and get ready for tomorrow."
povname "Upon laying on my bed my eyes instantly start zoning out and I start going to bed."
scene blank with dissolve

jump day5
