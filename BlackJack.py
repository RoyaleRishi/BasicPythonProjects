import random
import re

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append("{} of {}".format(rank,suit))

    def __str__(self):
        deck_composition = ""
        for card in self.deck:
            deck_composition += "{}\n".format(card)
        return deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand(Deck):

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        listed_card = card.split()
        self.value += values[listed_card[0]]
        if re.search("Ace",card) == True:
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self,cash):
        self.total = cash
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet: '))
        except:
            print("Oops, seems like that wasn't an integer, please try again!")
            continue
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips, you have {} chips".format(chips.total))
            else:
                break


def hit(deck,hand):
    if hand.value < 21:
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        try:
            choice = int(input("do you want to stand or hit (0 or 1)"))
        except:
            print("Invalid input, Please try again!")
            continue
        else:
            if choice == 0:
                playing = False
            elif choice == 1:
                hit(deck,hand)
            break

def show_some(player,dealer):
    print("Player's cards")
    print("")
    for card in player.cards:
        print(card)
    print("")
    print("Dealer's cards")
    print("")
    for i in range(1,len(dealer.cards)):
        print(dealer.cards[i])
    print("")
def show_all(player,dealer):
    print("Player's cards")
    print("")
    for card in player.cards:
        print(card)
    print("")
    print("Dealer's cards")
    print("")
    for i in range(0,len(dealer.cards)):
        print(dealer.cards[i])
    print("")

def player_busts():
    print("Player BUSTS!")
    chips.lose_bet()
def player_wins():
    print("Player Wins!")
    chips.win_bet()
def dealer_busts():
    print("Dealer BUSTS!")
    chips.win_bet()
def dealer_wins():
    print("Dealer Wins!")
    chips.lose_bet()
def push():
    print("Dealer and player tie, PUSH!")



while True:
    print("Welcome to a new round of BlackJack, lets start")
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()

    for i in range(2):
        card = deck.deal()
        player.add_card(card)
        card = deck.deal()
        dealer.add_card(card)

    while True:
        try:
            chips_available = int(input("Enter the number of chips you have: "))
        except:
            print("The input wan't an integer, please try again!")
        else:
            chips = Chips(chips_available)
            break

    take_bet(chips)

    show_some(player,dealer)

    playing = True
    while playing:

        hit_or_stand(deck,player)
        show_some(player,dealer)

        if player.value > 21:
            player_busts()
            break

        else:
            while dealer.value < 17:
                hit(deck,dealer)

        show_all(player,dealer)

        if player.value > 21:
            player_busts()
            break
        elif player.value > dealer.value:
            player_wins()
            break
        elif dealer.value > player.value:
            dealer_wins()
            break
        elif dealer.value > 21:
            dealer_busts()
            break
        else:
            push()
            break

    print("\nChips available to you are: {}\n".format(chips.total))

    want_to_play = input("Do you want to play again? (y or n): ")
    if want_to_play.lower() == "y":
        continue
    elif want_to_play.lower() == "n":
        print("Thank you for playing")
        break
