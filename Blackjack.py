from random import randint

numbers = ["ace", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "jack", "queen", "king"]
suits = ["spades", "clubs", "diamonds", "hearts"]


class Player:
    """class for each player that contains their point total and their cards"""

    def __init__(self):
        self.cards = []
        self.points = 0

    def get_points(self):
        return self.points

    def get_last_card_name(self):
        """grabs the last card in the array for output"""
        return self.cards[-1].get_card_name()

    def make_turn(self, cards_drawn):
        """draws a random card and adds it to the player's array"""
        not_unique = True
        while not_unique:
            # Picks a random number and suit
            number = numbers[randint(0, 12)]
            suit = suits[randint(0, 3)]
            this_card = Card(number, suit)
            not_unique = False
            for card in cards_drawn:
                if this_card == card:
                    not_unique = True

        cards_drawn.append(this_card)
        self.cards.append(this_card)
        return this_card

    def set_points(self):
        """calculates the player's blackjack score"""
        total = 0
        num_aces = 0
        for card in self.cards:
            value = card.get_points()
            if not value:
                num_aces += 1
                continue
            total += value
        if not num_aces:  # total if no aces are present
            self.points = total
        else:  # highest points under 21 if aces are present
            if total + 10 + num_aces > 21:
                self.points = total + num_aces
            else:
                self.points = total + 10 + num_aces


class Card:
    """class for each card drawn, includes number and suit"""

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_number(self):
        return self.number

    def get_card_name(self):
        """outputs the name of the card in the form of 'the NUM of SUIT'"""
        return 'the ' + self.number + ' of ' + self.suit

    def get_points(self):
        if self.number == "ace":
            return 0  # returns 0 to process later
        elif self.number == "jack" or self.number == "queen" or self.number == "king":
            return 10
        else:
            return int(self.number)

    def __eq__(self, other):
        if self.number == other.number and self.suit == other.suit:
            return True
        else:
            return False


class BlackjackGame:
    """Class for the game of blackjack to store game variables"""

    def __init__(self):
        self.cards_dealt = []
        self.dealer = Player()
        self.human = Player()

    def play_game(self):
        # COMPUTER TURN, Computer is dealt 1 card
        self.dealer.make_turn(self.cards_dealt)
        print("\nThe dealer was dealt " + self.dealer.get_last_card_name())

        # PLAYER TURN, Player is dealt 2 cards
        self.human.make_turn(self.cards_dealt)
        print("You are dealt " + self.human.get_last_card_name(), end=" ")
        self.human.make_turn(self.cards_dealt)
        print("and " + self.human.get_last_card_name())

        self.human.set_points()
        choice = ""
        self.dealer.set_points()
        while self.human.get_points() < 21 and choice != "s":  # hit or stand loop
            choice = str(input("Would you like to hit or stand? (h,s): "))
            if not choice:
                continue
            choice = choice[0].lower()
            if choice != "s":
                self.human.make_turn(self.cards_dealt)
                print("You are dealt " + self.human.get_last_card_name())
                self.human.set_points()

        if self.human.get_points() > 21:
            print("\nYa busted, buster")
        elif choice == "s":  # stand, computer draws
            print("You wimp\n\n")

            self.dealer.make_turn(self.cards_dealt)
            print("The dealer flips over " + self.dealer.get_last_card_name())
            self.dealer.set_points()

            # sees if computer should draw another card
            while self.dealer.get_points() < 17:
                self.dealer.make_turn(self.cards_dealt)
                print("The dealer hits and is dealt " +
                      self.dealer.get_last_card_name())
                self.dealer.set_points()

            if self.dealer.get_points() > 21:
                print("\nWell done, I guess a blind squirrel sometimes finds a nut...")
            elif self.dealer.get_points() < self.human.get_points():
                print("\nCongratulations, you won I guess")
            else:  # if the computer goes higher than the player without busting
                print("\nMuahaha just as I expected...YOU LOST!!!")

        else:  # if the player gets 21
            print("\nCongrats! You got a blackjack...beginner's luck I guess")


game = BlackjackGame()
game.play_game()
