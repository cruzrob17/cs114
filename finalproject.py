import time
import sys
def main():
    """this fucntion sets up the story"""
    print("It's a brisk autumn day and a tall slender man named Sam and a scruff looking teenager named Alex enter the First Eagle Bank in Downtown Chicago.")
    print()
    time.sleep(7)
    print("Sam finds himself at the bank in order to take out a loan in order to help pay for his mistress's house as he plans to leave his wife.")
    print()
    time.sleep(7)
    print("Alex finds himself at the bank in order to rob the bank to help pay for his dying friend's hospital treatment.")
    print()
    time.sleep(5)
    print("Now enters a broadset man with a hockey mask and a mysterious black bag.")
    print("Attempting to rob the bank, the broadset man grabs the nearest two people next to him and holds them hostage. Those two people just happen to be Sam and Alex.")
    print("Eventually the cops show up and a stand off begins with them and the boadset man.")
    print()
    time.sleep(6)
    print("With tensions rising, the broadset man points a gun at Sam and Alex while moving shakenly between them.")
    CharacterChoice()

def CharacterChoice():
    """this function contains the different character selection"""
    choice1=''
    print("So now you're presented with a choice.")
    while choice1 != 'Sam' and choice1 != 'Alex':#make Sam and Alex the only possible responses or else the next print statement repeats itself
        time.sleep(3)
        choice1=str(input("Which character would you like to survive and then subsequently experience their story? (Type Sam or Alex):"))
    if choice1=='Sam':
        print("BANG! The scruff looking teenager drops dead next to you as well as the broadset man behind you.")
        SamStart()
    elif choice1=='Alex':
        print("BANG! The tall slender man drops dead next to you as well as the broadset man behind you.")
        AlexStart()
    return CharacterChoice()

def SamStart():
    """this function contains Sam's first choice branch"""
    time.sleep(6)
    print()
    print("You see the cops beckon you toward them as you hear a constant ringing in your left ear.")
    print("You're visibly shaken by the whole ordeal but you can't stop thinking about the whole reason why you came to the bank in the first place.")
    print()
    print("You wake up the next morning to an email from the CPD offering you free counsling for patients with ptsd.")
    time.sleep(6)
    choice2=''
    while choice2 !='Work' and choice2 !='Appointment':
        choice2=str(input("Unfortunatley though, you have a very important day at work ahead of you so you have to make a choice (Type Work or Appointment):"))
    if choice2=='Work':
        print("You choose against your better judgement to go to work.")
        SamWork()
    elif choice2=='Appointment':
        print("You decide that you'll be better off with fixing your issues now than dealing with the concequences later so you go to the appointment later in the day.")
        SamAppoint()
    return SamStart()

def SamAppoint():
    """this function contains Sam's choice to go to the appointment"""
    time.sleep(6)
    print("On your way to the appointment you find that everything you're going through was caused by your shellfishness.")
    print()
    print("You didn't need to put your life at risk if you didn't want to abandon your wife")
    print()
    time.sleep(6)
    print("You didnt't need to see that kid drop dead next to you and you can't help but feel responsable for everything.")
    print("The thearapist walks you through the many ways you can go about treating your condition and one of those options include talking to the scruff looking teenager's family.")
    print("Your not sure if it's a good idea to meet with the family. You don't know if it will only make your feelings worse.")
    choice5=''
    while choice5 != 'Walk' and choice5 != 'Family':
        choice5=str(input("Go on a walk to think things through or bight the bullet and find the family of the dead teenager.(Type Walk or Family):"))
    if choice5=='Walk':
        print("You choose to take a moment and go for a walk")
        print("During your walk, you think that maybe infidelity wasn't worth it but then again neither was your life with Lilly, your wife.")
        print("Why did you have to survive instead of that other kid that undoubtly had so much potential?")
        print("You find that it'll make sense for you to move far away from Chicago in order to not hurt anybody anymore.")
        GameEnd()
    elif choice5=='Family':
        print("You choose to contact the family of the teenager and the therapist gives you their number.")
        SamFamily()
    return SamAppoint()

def SamFamily():
    """this function contains Sam's choice to visit Alex's family"""
    time.sleep(6)
    print("You choose to put on a brave face and go meet the family of the killed boy.")
    print("While with the family, you're overeraught with guilt and and it's unbearable to look at them.")
    print()
    print("Though you may not be fiancialy stable enough to do so, you consider the thought of maybe paying for the familie's funeral expenses.")
    print("You think that it'll help you be at ease after the traumatic events that had just transpired")
    choice6=''
    while choice6 != 'Pay' and choice6!= 'Home':
        choice6=str(input("Now you have to choose whether or not to pay the family's bills(Type Pay or Home):"))
    if choice6=='Pay':
        print("You choose to offer the family some miney in order for them to pay the funeral cost.")
        print("However they refuse yet ask that you attend the service the following week and you oblige.")
        print("")
        GameEnd()
    elif choice6=='Home':
        print("You choose to go home and forgo the funeral because you believe that it'll be too hard on you to go.")
        print("You hope to muddle things over with yourslef and drown your worries in drink. A pretty bad idea but it'll do for now.")
        GameEnd()
    return SamFamily()

def SamWork():
    """this function contains Sam's choice to go to work"""
    time.sleep(6)
    print("You brush off your conflicted emotions in order to impress this major client at work.")
    print()
    print("As you await your important meeting, your leg can't stop shaking and you find yourself out of breath due to your overacctive nervs.")
    print("The meeeting starts and your big payday lies in the hands of a burly middle aged man with a brown mustache.")
    time.sleep(6)
    print()
    print("While giving the mustached man a well rehearsed pitch on a fantastic new cardboard line that your company can provide, your brain goes on autopilot.")
    print("Just like you never left the bank, you start to hear yelling and the sound peircing bang of a gunshot.")
    time.sleep(6)
    print()
    print("Your speech patterns start to blur together and you find yourself on the ground.")
    print("Struggling to get to your feet, you find no better option than to escape your embarrassment by crawling to the door.")
    print("Once outside, you can hear the confused murmers of your co-workers and client and give yourslef two options.")
    choice3=''
    while choice3 !='Home' and choice3 !='Roof':
        choice3=str(input("Go home and pretty much quit your job or go up to the roof and gather your thoughts (Type Home or Roof):"))
    if choice3=='Home':
        print("You quickly gather your things and begin heading home.")
        SamHome()
    elif choice3=='Roof':
        print("You make a mad dash to the roof through way of the many flights of stairs.")
        print("The door to the roof is slamed open by you and you're greeted by the twinkling of the cityscape.")
        print("You wipe the sweat from your brow and move to the waist high edge of the bulding. ")
        time.sleep(6)
        print()
        print("Your heart tells you to jump but your brain tells you to call Lilly, your wife.")
        print("You see the disapointed faces of those you love and the scruff looking teenager flash in your eyes.")
        print("Like most things in your life, you fail to listen to your brain and your heart got the better of you")
        GameEnd()
    return SamWork()

def SamHome():
    """this function contains Sam's choice to go home"""
    time.sleep(6)
    print("You choose to go home to be with your family in order to get you through your breakdown.")
    print("You're unfortunately greeted by an enraged Lilly, your wife.")
    print("At the same time though, you could't be happier to see her.")
    print()
    print("So you sit her down and explain to her everything that's happend these past couple days because you haven't yet.")
    print("While explaining your story to her, see your kids running from their rooms to embrace you.")
    print("You feel you're at a crossroads in your lives and need to make a decisions.")
    choice4=''
    while choice4 !='Wife' and choice4 !='GF':
        choice4=str(input("Choose to stay with your wife in order to stay in contact with your kids or choose your girlfriend in order to be happy(Type Wife or GF):"))
    if choice4=='Wife':
        print("You choose to work things out with your wife for the sake of your children.")
        print("You still have nightmares of taht day but things start to feel normal again.")
        print("You even begin to think that maybe things will start to be ok.")
        GameEnd()
    elif choice4=='GF':
        print("You choose to make the hard decision of moving out to be with your girlfriend.")
        print("It's not an easy transition but deep down you think that in the long run, you'll be happier.")
        GameEnd()
    return SamHome()

def AlexStart():
    """this function contains Alex's first choice branch"""
    time.sleep(6)
    print("You start to shake conpulsively as you try to get yourself to your feet.")
    print("One of the officers helps you to your feet by lifting your arm and subsequently asks if you could answer a few questions.")
    choiceB=''
    while choiceB  !='Run' and choiceB !='Talk':
        choiceB=str(input("Your thoughts freeze as you think about the contents of your bag. You have two options (Type Run or Talk):"))
    if choiceB=='Run':
        print("You choose to run from the cops in hopes of them not finding the gun and ski mask in your bag.")
        AlexRun()
    elif choiceB=='Talk':
        print("You choose to take the chance and talk to the police")
        AlexTalk()
    return AlexTalk()

def AlexRun():
    """this function contains Alex's choice to run"""
    time.sleep(6)
    print("Your legs moved faster than your brain and you make a bee line towards the doors.")
    print("Unfortunately, the cumbersome weight of the bag made it hard to run and the cops easily caught up to you.")
    print()
    print("Being extreamly suspicious of why you ran, the cops search your bag and find the gun and you are taken under arrest.")
    print("You feel a perfound amount of guilt as you unable to save your friend from inside the walls of a penitentiary.")
    GameEnd()
    return AlexRun()

def AlexTalk():
    """this function contains Alex's choice to talk to the police"""
    time.sleep(6)
    print("You choose to stay calm and talk to the police and answer a few questions.")
    print("After the interagation, the cops choose to let you go with the option of attending a therapy appointment for patients with ptsd.")
    print("You say you'll think about of in actuallity you have no intention of going.")
    time.sleep(6)
    print()
    print("At the moment you're too concerned with getting the medicine that your friend Ellie can't afford.")
    print("You fear time is running out for Ellie so you have to come up for some options.")
    time.sleep(6)
    print()
    print("You look into running a fundraiser and with the right marketing, it might be a success.")
    print("However, you don't know if you'll even have enough time left to even get the medicine so think about steeling it.")
    choiceC=''
    while choiceC !='Fundraiser' and choiceC !='Steal':
        choiceC=str(input("Weigh your options and decide whether to raise the money for the medicine or steal it (Type Fundraiser or Steal):"))
    if choiceC=='Fundraiser':
        print("So you think that running a fundraiser will be a safer option.")
        print("You get the word out by posting on social media and putting up banners all over town with the help of your family.")
        print()
        print("The fundraiser goes extreamly well and you're able to buy the medicine in order to save Ellie.")
        print("All is well.")
        GameEnd()
    elif choiceC=='Steal':
        print("You feel time is against you so you choose to try and steal the medicine.")
        AlexSteal()
    return AlexTalk()

def AlexSteal():
    """this function contains Alex's choice to steal the cure"""
    time.sleep(6)
    print("Stealing the medicine won't be easy but you see it as the only real option.")
    print("You stake out the facility where the medicine is being produced and you notice different things about night and day shifts.")
    print(6)
    print()
    print("At night there is higher security but more places where you can't be seen.")
    print("During the day though, you notice that there is fewer security but less places to hide.")
    choiceD=''
    while choiceD !='Day' and choiceD !='Night':
        choiceD=str(input("Decide to go at night or during the day (Day or Night):"))
    if choiceD=='Day':
        print("Unfortunately, you're caught and all hopes for saving Ellie are gone.")
        print("You've failed")
        GameEnd()
    elif choiceD=='Night':
        print("Somehow you mange to escape the facility with the meicine and make a mad dash to Ellie.")
        print("While giving her the medicine, you think to yourself that everything that happenned was worth it now that you saved her.")
        GameEnd()
    return AlexSteal()

def GameEnd():
    """this function ends the game"""
    print("game over")
    print("You've made it to the end of the journey for this chapter in your character's life.")
    sys.exit()


main()
