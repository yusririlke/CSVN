label day2:

show clock with dissolve
alarm "'beep beep beep beep'"
play music "audio/alarm.mp3" volume 8 loop
povname "'Ugh, couldn't beat the alarm today.'"
scene bg dorm with dissolve
play music "audio/dorm.wav"
povname "'Must have been that study session last night made me oversleep."
povname "I leave my room and see Vic in the common area."

show vicNeutral with dissolve
vic "'You're up late again as per usual.''"
vic "'Guess yesterday was the exception, you already feeling comfortable after day one already?"
povname "'Yeah to be honest yesterday I felt nervous yesterday but I feel a lot more confident now.'"
vic "'That's good to hear, hey what time is your last class?'"
povname "'Uh let me check my schedule.'"
povname "'My last class should be around 5pm, I end later tonight.'"
vic "'Oh that sounds good, you want to get dinner after class today?'"
povname "'Oh that sounds good, where you want to eat though?'"
vic "'I was just thinking same place as last time, it's on campus so it's convient.'"
povname "'That place again, the food there is really mid but you're right at least it is nearby.'"
povname "'Fine, dinner after class sounds good I'll meet you then.'"
hide vicNeutral

povname "I then walk out the door and start walking to class."
scene classday with dissolve
povname "I walk into my CMPSC 111 class just on time today."
povname "Despite walking into the classroom at the exact time class is supposed to start I noticed a lot of the chairs were still empty."
povname "Maybe comp*uter science students are lazy about getting into class at the correct time?"
povname "A little after sitting down I see professor Array walk in."
show prof with dissolve
profe "'Welcome to class today we're going to begin our lecture.'"
profe "'We're going to start with what every beginner programmer does, as their first program hello world program.'"
povname "I realized that what he was talking about is what I studied yesterday for!"
profe "He did a basic explanation of his example hello world program"
profe "'Ok can anyone finish this example what should be put in the blank.'"
show hellop with dissolve
profe "'How about you [povname] you think you can answer this?'"
povname "I realized he was calling on me to answer this"
povname "Now what was it again, this is a hello world program so the inside of the main should be saying hello world"

menu:
    "cout << 'Hello World!'":
        play sound "audio/confirm.wav"
        jump cout
    "cin >> 'Hello World!'":
        play sound "audio/confirm.wav"
        jump cin
    "printf('Hello World!')":
        play sound "audio/confirm.wav"
        jump printf

label cout:
    hide hellop
    profe "Perfect answer it seems you were paying attention."
    profe "The c stands for character and out stands for output meaning that it is saying to print Hello World!"
    povname "I got the answer right!"
    phone "You feel confident after getting that answer right."
    phone "'You gained 5 knowledge, and -1 stress.'"
    $ stress -= 1
    $ knowledge += 5
    povname "I pay attention to the rest of the lesson he gives and feel like I learned a lot."
    phone "'You gained +1 knowledge for attending lecture.'"
    $ knowledge += 1
    jump day2c



label cin:
    hide hellop
    profe "'Close answer it seems you weren't paying attention.'"
    profe "'cin is for taking in characters from user output you are looking for cout.'"
    povname "I got the answer wrong"
    phone "'You feel down for getting the answer wrong even though you studied you lost 1 knowledge, and gained 1 stress.'"
    $ stress += 1
    $ knowledge -= 1
    povname "I pay attention to the rest of the lesson he gives and feel like I learned a lot."
    phone "'You gained +1 knowledge for attending lecture.'"
    $ knowledge += 1
    jump day2c



label printf:
    hide hellop
    profe "'Close answer it seems you weren't paying attention.'"
    profe "'Your answer doesn't follow C++ syntax try to pay closer attention next time.'"
    povname "I got the answer wrong."
    phone "'You feel down for getting the answer wrong even though you studied you lost 1 knowledge, and gained 1 stress."
    $ stress += 1
    $ knowledge -= 1
    povname "I pay attention to the rest of the lesson he gives and feel like I learned a lot."
    phone "'You gained +1 knowledge for attending lecture.'"
    $ knowledge += 1
    jump day2c


label day2c:
    hide prof with fade
    povname "After CMPSC 111 finished, I attended the rest of my gen eds and finished class at 5."
    povname "I promised vic to get dinner with him."
    povname "I walked out of my classroom and into the cafeteria."
    show cafeteria with dissolve
    povname "I see vic at the usual table and walk up to him."
    show vicNeutral with dissolve
    vic "'Yo, how was class.'"
    povname "'I think it went alright how about you.'"
    vic "'More of the same feels like classes haven't even actually begun.'"
    povname "'Yeah I get it anyway let's get food.'"
    povname "I walk up to the same counter as yesterday and get a pizza.'"
    vic "'How are you doing on money by the way, getting food every day has to be piling up.'"
    povname "'Now that you mention it, I am getting kind of low on funds.'"
    vic "'You have to be careful [povname], low money is a big cause of stress.'"
    vic "'I heard from a friend that their friend's finanical issues went into the negatives and eventually the stress from it caused them to drop out of school.'"
    povname "'That's awful, I'll keep that in mind.'"
    phone "'As your friend Vic said, be careful with your money.'"
    phone "'You're going to lose $5 every day from lunch and every day where you are not able to buy food is a big cause of stress.'"
    phone "'If stress gets too high you will drop out, and it is an instant game over.'"
