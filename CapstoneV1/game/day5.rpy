label day5:
show clock with dissolve
play music "audio/alarm.mp3" volume 8 loop

povname "..."
povname "I turn off my alarm feeling decently refreshed."
hide clock with dissolve
scene bg dorm
play music "audio/dorm.wav" loop
povname "I check my phone and notice there's a new notification from the school."
povname "Well that's rare, I wonder what it's about."
phone "Good morning students, I hope you are having a great start to classes."
phone "We regret to inform you that due to the amount of orders, lunch prices will be going up."
phone "This is a tempoary fix, at the end of the week prices will go back to normal."
povname "Seriously, I'm already barely able to pay for lunch how much is it going to cost now."
povname "I look through what my usual order would be."
povname "It went from the usual $5 to $7."
povname "I guess that's not the worst, I'm only going to be spending extra the rest of this week."
povname "Maybe I should go to work more often?"
povname "With that thought I change out of my loungewear into my outside clothes and head the the dorm common area."
show vicNeutral with fade

vic "'Morning how was your sleep.'"
povname "'Better than normal how about you.'"
vic "'I slept well too, I finished a lot of my project the day before so I was just chilling yesterday.'"
povname "'That's nice, oh I just remembered did you see the e-mail we got from school?'"
vic "'No, what was it?'"
povname "'They're raising the food prices at the cafeteria, our usual order is going to cost like $7 now.'"
vic "'.... You serious?'"
vic "I'm already barely able to pay it off everyday."
povname "'Yeah it sucks, apparently it's only going to be for the rest of this week though, it's weird."
vic "'I guess that's not the worst still wish they didn't do that.'"
povname "'Yeah anyway let's get breakfast and get ready for class."
vic "'Yep same as usual, come on I don't want to be late today.'"
povname "After breakfast I go to class."
hide vicNeutral

scene classday
povname "On the way to class I overhear two people from my class talking."
student "'Do you feel ready for the exam?'"
student2 "'No clue man, I don't feel ready but that's mainly because I don't know what to expect.'"
student "'Same, but I'm sure if you payed attention at the previous lectures, today, and tomorrow we'll be fine."
student2 "I hope so, the exam is two days from now right?'"
student "'Yep, I hope the homework today is as easy as it was yesterday.'"
povname "'The exam is only two days away... maybe I should study.'"
povname "'With that thought, I see professor Array walk in.'"
show prof with dissolve
profe "'Alright class, as a reminder the exam is two days away make sure you feel ready for it.'"
profe "'Today in class we're going to be covering arrays.'"
profe "'An array is a collection of similar data items stored in different memory locations.'"
profe "'The most common reasoning for using an array is when we want to store a large amount of instances.'"
profe "'For example we could do x1 = 10; x2 = 20; x3 = 30;.... up to 10 but an array makes that easier.'"
profe "'Look at this example.'"
show array1 with dissolve
profe "'You'll see a lot of things that look familar in this code.'"
profe "'The most important thing to look at is here.'"
show array2 with dissolve
profe "'This underlined piece of code is the array.'"
profe "'Arrays are like any other variable, you have to initialize it for our purposed we labeled as an int.'"
profe "'Then you must write the name of the array for our purposes we named it array.'"
profe "'Then you have to equate it to something like the following'"
profe "'This might sound complicated but writing it in this format is more or less the same as writing x1 = 10; x2 = 20; x3 = 30;, with the only difference being how you call it.'"
show array3 with dissolve
profe "'Here we are trying to output the array.'"
profe "'It is as simple as writing cout  the array's name and position in array you want to call.'"
profe "'Arrays are 0 based so the very first position array 0 is the same as calling 10.'"
profe "'If you wanted to output 20 you would write cout << array 1;'"
profe "'And if you wanted to output 30 you would write cout <<array 2;'"
profe "'The nice things about arrays are they can take any data types int, string, doubles etc."
profe "'Heres an example of an array using Strings.'"
show arrays with dissolve
profe "'In this example you can see that the only things that were changed are the arrays data type to string."
profe "'And having the inside of the array being text.'"
hide array1
hide array2
hide array3
hide arrays
profe "'Alright that concludes today's lecture.'"
profe "'I'll be handing out hw again today make sure to finish it at home.'"
povname "After professor array finished lecture, I saw everyone leaving the class at more or less the same time."
povname "I followed after them and headed towards my next gen ed."
hide prof
povname "After finishing all my gen eds I felt exhausted."
povname "It's weird I'm technically spending less time at school in college compared to high school, but why do I feel more exhausted when it's done?"
povname "With that thought I went to the usual food place and begrudgingly spent the $7 I needed for lunch."
$money -= 7

povname "Alright, I finished all my classes what should I do now?"
menu:
     "Go to work at the library":
        play sound "audio/confirm.wav"
        jump lib5
     "Go back home and study for the exam":
        play sound "audio/confirm.wav"
        jump study5



label study5:
scene dorm night with dissolve

povname "I decided to do some studying because the exam was coming up"
povname "I started walking back home."
povname "When I got home I went to my desk and looked through some of the textbook."
povname "After finishing my study session, I feel satisfied with the results."
$stress -= 1
$knowledge += 2
phone "You had a good study session and gained two knowledge."
phone "You also felt satisfied with your session and lost a point of stress."

jump hw5


label lib5:
povname "I thought it was best I go to work, I did spend more money than usual after all."
povname "I start walking to the library."
scene library with dissolve
show girl with fade
lily "'You came to help, thank you!'"
lily "'Today is going to be more of the same from last time do your best!'"
hide library
hide girl
jump tetris5

label continue5:
scene library with dissolve
show girl
play music "audio/dorm.wav" loop
show girl with fade
if dog5 >= 20:
    jump worst_ending5
elif dog5 >= 50:
    jump medium_ending5
elif dog5 >= 100:
    jump best_ending5

label worst_ending5:
    lily "'You got a score of [dog5]!'"
    lily "'That means you earned $5'"
    $money += 5
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Well, that wasn't the best possible result, but I still got payed so guess I'll go home."
    povname "I then started walking home."
    jump hw5

label middle_ending5:
    lily "'You got a score of [dog5]!'"
    lily "'That means you earned $10'"
    $money += 10
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Well, that wasn't the best possible result, but I still got payed so guess I'll go home."
    povname "I then started walking home."
    jump hw5
label best_ending5:
    lily "'You got a score of [dog5]!'"
    lily "'That means you earned $20'"
    $money += 20
    lily "'Here is your reward for today.'"
    lily "'I'll see you tomorrow!'"
    povname "Wow that was the best result, I got payed so I'll start going home."
    povname "I then started walking home."
    jump hw5

label hw5:
scene dorm night with dissolve

povname "After finishing everything from before. I returned to my desk."
povname "Guess it's time I started working on that homework."
povname "Let's see today we learned about array's what will the homework be like."
povname "I open my book and go the assigned question."
show hw5 with dissolve
book "In the following code the goal is to print 5, but we're not getting the desired output why?"
menu:
    "Arrays are 0 based so it would print 10 instead of 5":
        play sound "audio/confirm.wav"
        jump correct5
    "You need quotation marks between each entry":
        play sound "audio/confirm.wav"
        jump wrong5
    "The commas between each entry is not necessary":
        play sound "audio/confirm.wav"
        jump wrong5

label correct5:
    book "That's correct"
    book "Arrays are 0 based it's important they start at 0 not 1"
    $knowledge += 1
    phone "You got a point of knowledge for that."
    jump end5


label wrong5:
    book "Incorrect"
    book "The correct answer was A arrays are 0 based."
    book "The other options do not work because you only need quotation marks when it's a string and the commas are necessary."
    jump end5


label end5:
    scene dorm night with dissolve

    povname "After finishing my homework I put all my stuff back in my bag."
    povname "I had a light snack of prangles cause I got the munchies after studying."
    povname "I went on my bed and scrolled through memes on my phone that made me chuckle."
    povname "Before I knew it I was drifting to sleep."
    scene blank with dissolve
    jump day6
