import random
player_choise_valid=False
options=['rock', 'paper', 'scissors']
def getChoices():
    playerChoice=input('enter your choice - [rock, paper, scissors]')
    options=['rock', 'paper', 'scissors']
    computerChoice=random.choice(options)
    choice={'player': playerChoice, 'computer': computerChoice}
    return choice, playerChoice
getChoiceResult= getChoices()
if getChoiceResult[1] in options:
    player_choise_valid=True
else:
    print(f" select one of the option")
def checkWin(player,computer):
    print(f"you choce {player}, and computer choce {computer}")
    if player==computer:
        return 'its a tie'
    elif player=='rock':
        if computer=='scissors':
            return 'rock crushes scissors! you win'
        else:
            return 'paper covers rock. You loose'
        
    elif player=='paper':
        if computer=='rock':
            return 'paper covers rock! you win'
        else:
            return 'scissors cut paper. You loose'
        
    elif player=='scissors':
        if computer=='paper':
            return 'scissors cut paper! you win'
        else:
            return 'rock crushes scissors. You loose'
    


choices = getChoiceResult[0]
if (player_choise_valid == True):
    result=checkWin(choices['player'],choices['computer'])
    print(result)