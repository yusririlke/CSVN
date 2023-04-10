label day1:
scene bg dorm with dissolve
povname "I woke up feeling a bit groggy, but quickly jolted awake as I realized what day it was. Surprisingly, I didn’t feel all too nervous, mainly just excited for the day to come."
povname "Huh, looks like I woke up before my alarm. I probably shouldn’t go back to sleep buuuuut…"

menu:
    extend''
    "Wake up":
       play sound "audio/confirm.wav"
       jump upuwu
    "Go back to sleep":
       play sound "audio/confirm.wav"
       jump sleepyuwu

label upuwu:
    povname "Knowing myself going back to sleep will probably just make me feel worse, no matter how tempting…"
    jump cont1


label sleepyuwu:
    alarm "Beep Beep Beep Beep.."
    povname "Ughhh that was not a good idea, I feel even more tired now…"
    phone "Stress +1"
    $ stress += 1
    jump cont1

label cont1:
    povname "So I got up and prepped for class."
    scene living day with dissolve
    povname "'Vic? Vic wake up, sleepyhead~'"
    povname "VIC!"
    #TODO: Make shake
    show vicNeutral with dissolve
    vic "mmngh..."
    vic "Mommy?"
    povname "N-no. You should get going for class though."
    vic "maybe later~"
    scene outschool with dissolve
    povname "I’ve never been a morning person, but being here on my actual first day fills me with excitement."
    povname "I decide to go now, not wanting to be late."
    povname "I look at the school that I saw yesterday and wonder what my first day at comp sci is going to be like."
    povname "And with that thought I take my first step into the school as a freshman."
    scene classday with dissolve
    povname "When I came into the classroom, I was surprised to see that I was 15 minutes early, and there was no one there."
    povname "I got a little worried I may have entered the wrong room, but people soon began filtering in."
    povname "'Phew... I guess people were just tired from the early class.'"
    povname "I eventually choose a seat near the back left corner."
    povname "Eventually I see an older looking man walk into the classroom."
    show prof with dissolve
    profe "'Hello, I am Professor Ziparu Array.'"
    profe "'Please call me Professor Array, and welcome to computer science 111, introduction to programming.'"
    profe "'In this course we will be going over the basics of c++.'"
    profe "'Today we will be going over the syllabus and a basic question sheet to check your prior programming experience.'"
    povname "Aproximately 20 minutes go by of professor array explaining the syllabus, nothing interesting really."
    povname "The only thing that caught my eye was that attendence was mandatory and the grading scale was heavy towards homework."
    profe "'I am now going to be handing out a basic question sheet.'"
    profe "'Just answer what you can it won't be graded.'"
    povname "I see the professor passing out a stack of papers to everyone in the first row untill one eventually gets passed to me."
    hide prof with dissolve
    povname "Alright let's see if I can answer these questions."


    jump qEasy


    ##MC comes homes after lunch




label cont2:
        povname "Welp, I think that went as well as I think as it could've gone, guessing and all..."

        povname "Time for lunch! I promised Vic we'd meet up after class, and I am sooooo hungryyyyyy."

        scene cafeteria with dissolve

        povname "Wow there's a lot more people here than on the weekend... I hope I can find Vic."

        show vicNeutral with dissolve

        vic "'[povname]! I'm over here!'"

        vic "'I guess you're as shocked as I am about the amount of people there are here today, aren't ya?'"

        povname "Yeah, seems a bit odd that it's that stacked in here, but also makes sense since it's around mid-day."

        stomach "*grumble grrrr angy noise*"
        #TODO: Put actual whale call/ grumbling noises

        vic "'Hahaha! Couldn't have said it better myself! Lets go get some food!'"

        povname "So we went and got something to eat. I got a pizza and Vic got some the philly cheese steak, daily meal."

        povname "We managed to find a nice booth area to sit in the back at the cafeteria and just began chatting about our days."

        vic "So lemme get this straight, you didn't do anything except go over your syllabus?"

        vic "'Dang, that's lucky! We already got homework in my art history class!'"

        povname "'Not to cut you off or anything, but this pizza is insanely greasey...'"

        vic "'Oh I guess it's not just my cheese steak then. It's hella greesy.'"

        vic "'I think that settles it then! I'll be packing lunch from this day forwards!!!'"

        povname "'Same, it's cheaper and tastes better anyways.'"

        phone "You spent $5 for getting lunch with Vic."

        $ money -=5





        hide vicNeutral

        scene blank with dissolve

        povname "Yeah... this arrangement won't last long when things pick up, but it's a good idea for now."

        povname "After that we went out seperate ways for the day."

        povname "Classes after the computer science one in the morning were all pretty boring, reading a syllabus, and talking about some stuff that I frankly don't understant the use for my degree."



        scene dorm night with dissolve

        play music "audio/study.wav" loop
        povname "After coming back home from lunch with Vic I started thinking about class."
        povname "Those intro programming questions were harder than I initially thought..."
        povname "I should probably do a little bit of self studying."
        povname "I decide to go back to my room and look through the textbook I was given in class."
        scene ibook with dissolve
        povname "This textbook better be useful given the crazy cost of it."
        povname "I bring the book named 'Intro to C++' over to my desk and open it up."
        book "Welcome to the world of C++!"
        book "C++ is a programming language created by Bjarne Stroustrup and his team in the year 1979."
        book "It remains as one of the worlds most popular coding languages to this day."
        book "As the name would imply C++ is derived from the language C, a language that is also respected."
        book "To get more information on why learn C++ go to page 1, for practical examples go to page 3."

menu:
    extend''
    "Learn more about why C++":
        play sound "audio/confirm.wav"
        jump whyC
    "Learn practical examples":
        play sound "audio/confirm.wav"
        jump practical


label whyC:
    povname "I think it's best if I know why I should learn C++ first."
    povname "I flip the book to the first page."
    book "'C++ is a great choice as your first coding language.'"
    book "'C++ allows you to learn programming from the ground up, meaning you will have to explain everything you do.'"
    book "'But C++ is also a intermediate level language, meaning it is neither a high level or low level language.'"
    book "'A high level language is a language that is user oriented, meaning that it may not be the most efficent but it is easier for the user to use.'"
    book "'Therefore in contrast a low level language is a language that is harder for the user but more efficent for the machine.'"
    book "'All of this makes C++ a useful language that every programmer should know, and a great first one to learn.'"
    povname "I then flip the page to the practical learning section."
    jump practical

label practical:
    book "'This section will teach you your very first program every programmer has ever done.'"
    book "'You will now learn how to write your first hello world program.'"
    book "'First we will show you how to write it.'"
    show hello with dissolve
    book "'We will now be dissecting every part of this program make sure to pay attention.'"
    book "'In programming making sure you don't mess up syntax is very important.'"
    book "'Especially in college where you will often be forced to write code on paper, it will be helpful to memorize the syntax.'"
    show hello1 with dissolve
    book "'The first part to discuss is this int main().'"
    book "'Main is a function that exists in every single C or C++ code you will ever write so get used to seeing it'"
    book "'A function is a chunk of code that you can use over and over again instead of writing it multiple times'"
    book "'The next part is int, meaning that main will return a value of type integer.'"
    book "'You can also write as void main() but for this example we choose to write it as int.'"
    book "'Also do not mess up the syntax for this after every main should be an open and closed parentheses (), and an open and closed bracket.'"
    show hello2 with dissolve
    book "'The next part to remember is cout <<.'"
    book "'In C++ cout is a part of the standard library, where c stands for character and out stands for output.'"
    book "'Its basically in normal english 'say this'.'"
    book "'The next part '<<' is an insertion operator that will display a stream of characters.'"
    book "'Then you put what you want to say in double quotes and in our example that is Hello World!'"
    book "'The \n is saying the next we type should be printed in the next line.'"
    book "'Finally don't forget your semi colon a classic beginner mistake.'"
    book "'A semicolon is mandatory after every declaration in programming soon it will be second nature to include them.'"
    book "'Close all of that off with a right bracket saying your main function is done and you have completed your first main function!'"
    book "'Now if you were to run the console would print Hello World!'"
    book "'It's simpler than you probably thought right, well it is our first program it will only get more complicated.'"
    book "'The most important part of beginning CS is just understanding what all the parts in a program is doing, practice makes perfect!'"
    hide hello2
    hide hello1
    hide hello
    povname "'Wow, I think that was a productive use of my time I wonder how long I studied.'"
    povname "'It's already 1AM, time flew by so fast!'"
    povname "I decided that it's about time I went to bed."
    scene blank with dissolve
    povname "I lay down, excited for what my second day of college would be like."
    phone "'Becaause of the study session you had today you feel more confident going to class tomorrow.'"
    $ knowledge += 5
    phone "'You have gained +5 knowledge points.'"

    jump day2
