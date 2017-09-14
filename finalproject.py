import time
import sys
def main():
    """this fucntion sets up the story"""
    print("It's a brisk autumn day and a tall slender man named Sam and a scruff looking teenager named Alex enter the First Eagle Bank in Downtown Chicago.")
    print()
    time.sleep(5)
    print("Sam finds himself at the bank in order to take out a loan in order to help pay for his mistress's house as he plans to leave his wife.")
    print()
    time.sleep(5)
    print("Alex finds himself at the bank in order to rob the bank to help pay for his dying friend's hospital treatment.")
    print()
    time.sleep(5)
    print("Now enters a broadset man with a hockey mask and a mysterious black bag.")
    print("Attempting to rob the bank, the broadset man grabs the nearest two people next to him and holds them hostage. Those two people just happen to be Sam and Alex.")
    print("Eventually the cops show up and a stand off begins with them and the boad set man.")
    print()
    time.sleep(6)
    print("With tensions growing, the broadset man points a gun at the Sam and Alex while moving shakenly between them.")
    CharacterChoice()

def CharacterChoice():
    """this function contains the different character selection"""
    choice1=''
    print("So now you're presented with a choice.")
    while choice1 != 'Sam' and choice1 != 'Alex':#make Sam and Alex the only possible responses or else the next print statement repeats itself
        time.sleep(3)
        choice1=str(input("Which character would you like to survive and then subsequently experience their story? (Type Sam or Alex):"))
    if choice1=='Sam':
        print("Boom! The scruff looking teenager drops dead next to you as well as the broadset man behind you.")
        SamStart()
    elif choice1=='Alex':
        print("Boom! The tall slender man drops dead next to you as well as the broadset man behind you.")
        AlexStart()
    return CharacterChoice()

def SamStart():
    """this function contains Sam's first choice branch"""
    time.sleep(5)
    print()
    print("You see the cops beckon you toward them as you hear a constant ringing in your left ear.")
    print("You're visibly shaken by the whole ordeal but you can't stop thinking about the whole reason why you came to the bank in the first place.")
    print("You wake up the next morning to an email from the CPD offering you free counsling for patients with ptsd.")
    time.sleep(6)
    choice2=''
    while choice2 !='Work' and choice2 !='Appointment':
        choice2=str(input("Unfortunatley though, you have a very important day at work ahead of you so you have to make a choice (Type Work or Appointment):"))
    print()
    if choice2=='Work':
        print("You choose against your better judgement to go to work.")
        SamWork()
    elif choice2=='Appointment':
        print("You decide that you'll be better off with fixing your issues now than dealing with the concequences later so you go to the appointment later in the day.")
        SamAppoint()
    return SamStart()

def SamAppoint():
    """this function contains Sam's choice to go to the appointment"""
    print("On your way to the appointment you find that everything you're going through was caused by your shellfishness.")
    print()
    print("You didn't need to put your life at risk if you didn't want to abandon your wife")
    print()
    print("You didnt't need to see that kid drop dead next to you and you can't help but feel responsable for everything.")
    choice5=''
    while choice5 != 'Walk' and choice5 != 'Family':
        choice5=str(input("Walk or Family:"))
    if choice5=='Walk':
        print("chill out")
        GameEnd()
    elif choice5=='Family':
        print("help")
        SamFamily()
    return SamAppoint()

def SamFamily():
    """this function contains Sam's choice to visit Alex's family"""
    print("Family")
    choice6=''
    while choice6 != 'Pay' and choice!= 'Home':
        choice6=str(input("Pay or Home:"))
    if choice6=='Pay':
        print("Good person")
        GameEnd()
    elif choice6=='Home':
        print("Kinda selish")
        GameEnd()
    return SamFamily()

def SamWork():
    """this function contains Sam's choice to go to work"""
    print("work")
    choice3=''
    while choice3 !='Home' and choice3 !='End':
        choice3=str(input("Home or End:"))
    if choice3=='Home':
        print("Dad's home")
        SamHome()
    elif choice3=='End':
        print("sucks")
        GameEnd()
    return SamWork()

def SamHome():
    """this function contains Sam's choice to go home"""
    print("Home")
    choice4=''
    while choice4 !='Wife' and choice4 !='BF':
        choice4=str(input("Wife of BF:"))
    if choice4=='Wife':
        print("happy life")
        GameEnd()
    elif choice4=='BF':
        print("sad life")
        GameEnd()
    return SamHome()

def AlexStart():
    """this function contains Alex's first choice branch"""
    print("fan")
    choiceB=''
    while choiceB  !='Run' and choiceB !='Talk':
        choiceB=str(input("Run or Talk:"))
    if choiceB=='Run':
        print("how high?")
        AlexRun()
    elif choiceB=='Talk':
        print("not now")
        AlexTalk()
    return AlexTalk()

def AlexRun():
    """this function contains Alex's choice to run"""
    print("caught")
    GameEnd()
    return AlexRun()

def AlexTalk():
    """this function contains Alex's choice to talk to the police"""
    print("Talk")
    choiceC=''
    while choiceC !='Fundraiser' and choiceC !='Steal':
        choiceC=str(input("Fundraiser or Steal:"))
    if choiceC=='Fundraiser':
        print("good person")
        GameEnd()
    elif choiceC=='Steal':
        print("sketchy")
        AlexSteal()
    return AlexTalk()

def AlexSteal():
    """this function contains Alex's choice to steal the cure"""
    print("Steal")
    choiceD=''
    while choiceD !='Day' and choiceD !='Night':
        choiceD=str(input("Day or Night:"))
    if choiceD=='Day':
        print("bad choice")
        GameEnd()
    elif choiceD=='Night':
        print("good choice")
        GameEnd()
    return AlexSteal()

def GameEnd():
    """this function ends the game"""
    print("game over")
    sys.exit()


main()
