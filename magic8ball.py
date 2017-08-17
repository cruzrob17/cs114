from random import randint
print('Please enter your name')
name=input()
r = randint(1,9)
print(r, name)
if r == 1:
    print('Your future is foggy')
elif r ==2:
    print('Luck awaits around the corner')
elif r ==3:
    print('You are going to die')
elif r == 4:
    print('Be kind more often')
elif r == 5:
    print('Play the lottery')
elif r == 6:
    print('Leave me alone')
elif r == 7:
    print('Follow your instincts')
elif r == 8:
    print('Take chances')
elif r == 9:
    print('Screw it')
