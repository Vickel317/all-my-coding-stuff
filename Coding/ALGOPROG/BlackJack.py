import random

decks = {
    "hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 1 or 11],
    "diamonds" : [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 1 or 11],
    "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 1 or 11],
    "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 1 or 11]
}
card= 0
dealercard= 0
flag = True

def startgame():
    print("Welcome to the Blackjack game!")
    loopgame()
def gameprogram():
    global card
    global dealercard
    card += random.choice(decks["hearts"])
    dealercard += random.choice(decks["spades"])
    print("You have drawn:", card)
    print("The dealer has drawn:", dealercard)
    winlosecondition()
def loopgame():
    global card, dealercard, flag
    while flag == True:
        user_input= input('Hit or stay?')
        if user_input.lower() == 'hit':
            gameprogram()
        elif user_input.lower() == 'stay':
            print(f"You have chosen to stay with a total of {card} ")
        else:
            print('Invalid input. Please try again.')
    if card<dealercard:
        print('You lose!')


def winlosecondition():
    global flag
    if card < 21 and dealercard < 21:
        loopgame()
        flag = True
    if card > 21 or dealercard == 21:
        print("You lose!")
        flag= False
    if card == 21 and dealercard== 21:
        print("Draw")
        flag= False
    if card == 21:
        print("You win!")
        flag= False
  
    return flag

startgame()