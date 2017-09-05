import time
def main():
    """this fucntion sets up the story"""
    print("asfsdafsdf")
    print()
    CharacterChoice()


def CharacterChoice():
    """this function contains the different character selection"""
    choice=''
    print("So now you're presented with a choice.")
    while choice != 'Sam' and choice != 'Alex':#make Sam and Alex the only possible responses or else the next print statement repeats itself
        time.sleep(3)
        choice=str(input("Which character's story would you like to experience first? (Sam or Alex)"))
    if choice=='Sam':
        print("happy")
        SamStart()
    elif choice=='Alex':
        print("sad")
        AlexStart()
    return CharacterChoice()

def SamStart():
    """this function contains Sam's first choice branch"""
    print("family")
    choice2=''
    while choice2 !='run' and choice2 !='fight':
        choice2=str(input("run or fight"))
    if choice2=='run':
        print('too slow')
        SamRun()
    elif choice2=='fight':
        print('too bad')
        SamFight()
    return SamStart()



def AlexStart():
    print("fan")

main()
