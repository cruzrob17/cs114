import time
import sys
def main():
    """this fucntion sets up the story"""
    print("asfsdafsdf")
    print()
    CharacterChoice()

def CharacterChoice():
    """this function contains the different character selection"""
    choice1=''
    print("So now you're presented with a choice.")
    while choice1 != 'Sam' and choice1 != 'Alex':#make Sam and Alex the only possible responses or else the next print statement repeats itself
        time.sleep(3)
        choice1=str(input("Which character's story would you like to experience first? (Sam or Alex):"))
    if choice1=='Sam':
        print("happy")
        SamStart()
    elif choice1=='Alex':
        print("sad")
        AlexStart()
    return CharacterChoice()

def SamStart():
    """this function contains Sam's first choice branch"""
    print("family")
    choice2=''
    while choice2 !='Work' and choice2 !='Appointment':
        choice2=str(input("Work or Appointment:"))
    if choice2=='Work':
        print('too slow')
        SamWork()
    elif choice2=='Appointment':
        print('too bad')
        SamAppoint()
    return SamStart()

def SamAppoint():
    """this function contains Sam's choice to go to the appointment"""
    print("appointment")
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
