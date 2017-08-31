#make a text based adventure game with between 2 main characters
#set up sleep for a bit of suspense

import time
"""this fucntion sets up the story"""
def intro():
    print("asfsdafsdf")
    print()
    return intro

"""this function contains the different character selection"""
def CharacterChoice():
    choice=''
    print("So now you're presented with a choice.")
    while choice != 'Sam' and choice != 'Alex':#make Sam and Alex the only possible responses or else the next print statement repeats itself
        time.sleep(3)
        choice=str(input("Which character's story would you like to experience first? (Sam or Alex)"))
    return CharacterChoice

"""this function starts the branching story paths"""

def CharacterPath(choice):
    choice=input()
    if choice=='Sam':
        return print("happy")
    elif choice=='Alex':
        return print("sad")










def main():
    import time
    intro()
    CharacterChoice()
    CharacterPath(choice)
main()
