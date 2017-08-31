
def getfortune():
    fortunelist=[
    'Your future is foggy',
    'Luck awaits around the corner',
    'You are going to die',
    'Be kind more often',
    'Play the lottery',
    'Leave me alone',
    'Follow your instincts',
    'Take chances',
    'Screw it']
    return getfortune

def main():
    from random import randint
    r=randint(0,8)
    getfortune()
    fortunelist[r]
main()
