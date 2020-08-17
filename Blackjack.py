from random import randint


class Player:
    """class for each player that contains their point total and their cards"""

    def __init__(self):
        self.cards = []
        self.points = 0

    def getPoints(self):
        """gets the blackjack point total for the player"""
        return self.points

    def setPoints(self):
        """calculates the player's maximum blackjack score"""
        total = 0
        numAces = 0
        for card in self.cards:
            value = card.getPoints()
            if not value:
                numAces += 1
                continue
            total += value
        if not numAces:  # total if no aces are present
            self.points = total
        else:  # highest points under 21 if aces are present
            if total + 10 + numAces > 21:
                self.points = total + numAces  # aces are counted as 1 point
            else:
                self.points = total + 10 + numAces  # one ace is 11 and the rest are 1

    def getLastCardName(self):
        """grabs the last card in the array for output"""
        return self.cards[-1].getCardName()

    def makeTurn(self, cardsDrawn):
        """draws a random card and adds it to the player's array"""
        cardIsCopy = True
        while cardIsCopy:
            # Picks a random card
            newCard = Card()
            cardIsCopy = False
            for card in cardsDrawn:
                if newCard == card:
                    cardIsCopy = True
                    break

        cardsDrawn.append(newCard)
        self.cards.append(newCard)
        return newCard


class Card:
    """class for each card drawn, includes number and suit"""

    NUMBERS = ["ace", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "jack", "queen", "king"]
    SUITS = ["spades", "clubs", "diamonds", "hearts"]

    def __init__(self):
        self.number = Card.NUMBERS[randint(0, 12)]
        self.suit = Card.SUITS[randint(0, 3)]

    def getSuit(self):
        """gets the suit from the card"""
        return self.suit

    def getNumber(self):
        """gets the number from the card"""
        return self.number

    def getCardName(self):
        """outputs the name of the card in the form of 'the NUM of SUIT'"""
        return 'the ' + self.number + ' of ' + self.suit

    def getPoints(self):
        """gets the point number for the card in blackjack. If the card is an ace, it will return 0"""
        if self.number == "ace":
            return 0  # returns 0 to process later
        elif self.number == "jack" or self.number == "queen" or self.number == "king":
            return 10
        else:
            return int(self.number)

    def __eq__(self, other):
        """figure out if two cards are equal"""
        if self.number == other.number and self.suit == other.suit:
            return True
        else:
            return False


class BlackjackGame:
    """Class for the game of Blackjack to store game variables"""

    def __init__(self):
        self.cardsDealt = []  # used to draw new cards that haven't been played yet
        self.dealer = Player()
        self.human = Player()

    def playGame(self):
        """plays the blackjack game"""
        # COMPUTER TURN, Computer is dealt 1 card
        self.dealer.makeTurn(self.cardsDealt)
        print("\nThe dealer was dealt " + self.dealer.getLastCardName())

        # PLAYER TURN, Player is dealt 2 cards
        self.human.makeTurn(self.cardsDealt)
        print("You are dealt " + self.human.getLastCardName(), end=" ")
        self.human.makeTurn(self.cardsDealt)
        print("and " + self.human.getLastCardName())

        choice = ""
        self.human.setPoints()
        self.dealer.setPoints()
        while self.human.getPoints() < 21 and choice != "s":  # hit or stand loop
            choice = str(input("Would you like to hit or stand? (h,s): "))
            if not choice:
                continue
            choice = choice[0].lower()
            if choice != "s":
                self.human.makeTurn(self.cardsDealt)
                print("You are dealt " + self.human.getLastCardName())
                self.human.setPoints()

        if self.human.getPoints() > 21:
            print("\nYa busted, buster")
        elif choice == "s":  # stand, computer draws
            print("You wimp\n\n")

            self.dealer.makeTurn(self.cardsDealt)
            print("The dealer flips over " + self.dealer.getLastCardName())
            self.dealer.setPoints()

            # sees if computer should draw another card
            while self.dealer.getPoints() < 17:
                self.dealer.makeTurn(self.cardsDealt)
                print("The dealer hits and is dealt " +
                      self.dealer.getLastCardName())
                self.dealer.setPoints()

            if self.dealer.getPoints() > 21:
                print("\nWell done, I guess a blind squirrel sometimes finds a nut...")
            elif self.dealer.getPoints() < self.human.getPoints():
                print("\nCongratulations, you won I guess")
            else:  # if the computer goes higher than the player without busting
                print("\nMuahaha just as I expected...YOU LOST!!!")

        else:  # if the player gets 21
            print("\nCongrats! You got a blackjack...beginner's luck I guess")


game = BlackjackGame()
game.playGame()
