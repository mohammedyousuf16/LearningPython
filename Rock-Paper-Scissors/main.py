import random
def getChoices():
    playerChoice=input('enter your choice ')
    options=['rock', 'paper', 'scissors']
    computerChoice=random.choice(options)
    choices={'player': playerChoice, 'computer': computerChoice}
    return choices

def checkWin(player,computer):
    return [player,computer]