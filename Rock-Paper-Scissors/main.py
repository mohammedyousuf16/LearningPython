def getChoices():
    playerChoice=input('enter your choice ')
    computerChoice='paper'
    choices={'player': playerChoice, 'computer': computerChoice}
    return choices
choices=getChoices()
print(choices)
