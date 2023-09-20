import random

playing_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J",  "Q", "K"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

class Blackjack:
    def __init__(self):
        self.dealer = []
        self.player = []
        self.cards = []

        for suit in suits:
            for card in playing_cards:
                self.cards.append(card + " of " + suit)

    def pick_card(self):
        card_index = random.randint(0, len(self.cards) - 1)
        card = self.cards[card_index]

        self.cards.remove(card)

        return card
    
    def count_hand(self, hand: list[str]):
        total = 0

        for card in hand:
            if card[0] == 'A':
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            elif card[0] in ['J', 'Q', 'K']:
                total += 10
            else:
                total += int(card[0])

        return total
    
    def print_hands(self):
        print(f"\nDealer hand: {self.count_hand(self.dealer)}")
        print(f"Player hand: {self.count_hand(self.player)}\n")

    def player_turn(self):
        player_count = self.count_hand(self.player)
        player_choice = input(f"\nDo you want to hit or stand? (h/s)\n")

        while player_choice == 'h':
            self.player.append(self.pick_card())

            player_count = self.count_hand(self.player)

            if player_count > 21:
                player_choice = 's'

                return 22
            elif player_count == 21:
                player_choice = 's'

                return 21
            else:
                player_choice = input(f"Player hand: {player_count}\nDo you want to hit or stand? (h/s)\n")

        return player_count
     
    def dealer_turn(self):
        dealer_count = self.count_hand(self.dealer)

        while dealer_count < 17:
            self.dealer.append(self.pick_card())

            dealer_count = self.count_hand(self.dealer)

        return dealer_count

    def reset_match(self):
        self.cards = []
        self.player = []
        self.dealer = []

        for suit in suits:
            for card in playing_cards:
                self.cards.append(card + " of " + suit)

    def start_match(self):
        self.dealer.append(self.pick_card())
        self.dealer.append(self.pick_card())

        self.player.append(self.pick_card())
        self.player.append(self.pick_card())

        self.print_hands()

        player_count = self.count_hand(self.player)

        if player_count > 21:
            self.print_hands()
            return "Dealer wins"
        elif player_count == 21:
            dealer_count = self.dealer_turn()

            if dealer_count == 21:
                self.print_hands()
                return "Draw"
            else:
                self.print_hands()
                return "Player wins"
        else: 
            player_count = self.player_turn()
            dealer_count = self.dealer_turn()

            if player_count > dealer_count and player_count <= 21:
                self.print_hands()
                return "Player wins"
            elif player_count == dealer_count:
                self.print_hands()
                return "Draw"
            elif dealer_count > 21:
                self.print_hands()
                return "Player wins"
            else:
                self.print_hands()
                return "Dealer wins"
    
blackjack = Blackjack()

playing = True

while playing:
    playing = input(f"Do you want to play? (y/n)\n")

    if playing == 'n':
        playing = False
        break
    elif playing == 'y':
        playing = True
    else:
        playing = True
        print("Incorrect input")
        break

    result = blackjack.start_match()

    print(result)

    blackjack.reset_match()

