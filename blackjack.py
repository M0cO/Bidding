import random

game_start = input("Lets play a game of Blackjack? Press 'y' to Start")

logo = """
    .------.         _     _            _    _            _
    |A_  _ |        | |   | |          | |  (_)          | |
    |( \/ ).-----.  | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |  | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |  | |_) | | (_| | (__|   <| | (_| | (__|   <
    '-----| \  / |  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
          |  \/ K|                         _/ |
          '------'                        |__/
 """
if game_start == 'y':
    print(logo)


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # The user and computer should each get 2 random cards.
    dealer = random.sample(cards, 2)
    player = random.sample(cards, 2)

    # Add up the user's and the computer's scores
    dealer_total = sum(dealer)
    player_total = sum(player)

    print(f"Dealers first card: {dealer[0]} \nYour cards are {player}")
        # Determine the winner which one is closest to 21
        
    def closest_number(target, num1, num2):
        # Calculate the absolute difference between the target and each number
        diff1 = abs(target - num1)
        diff2 = abs(target - num2)

        # Compare the differences
        if diff1 == target:
            return f"You win! The sum of your cards: {num1}"
        elif diff2 == target:
            return f"You Lose: The sum of the dealers cards: {num2} are closer to {target}"
        elif diff1 < diff2:
            return f"you Win! The sum of your cards: {num1} is closer to {target}"
        elif diff2 < diff1:
            return f"You Lose: The sum of the dealers cards: {num2} are closer to {target}"
        else:
            return f"It's a Tie! Both {num1} and {num2} are equally close to {target}"
        
    # Does the user or computer have a blackjack?(ace + 10)
    if player_total == 21:
        print("Blackjack! You win!")
        return
    elif dealer_total == 21:
        print(f"Dealer has Blackjack!{dealer} You lose.")
        return
            # Is user's score over 21?
        
    if player_total >= 21:
        if 11 in player:
            one_or_eleven = input("count ace as '1' or '11'?")  # Do they have an "Ace"?

            if one_or_eleven == '1':
                player = [1 if x == 11 else x for x in player]  # If the ace counts as a 1 instead of 11, are they still over 21?
                total = sum(player)
                    
                if sum(player) > 21:
                    return "You bust! Game over."
  

    # draws card
    while player_total < 21:
        deal_or_no_deal = input("Type 'y' to draw another card or 'n' to stand: ").lower()
        if deal_or_no_deal == 'y':
            new_card = random.choice(cards)
            player.append(new_card)
            player_total = sum(player)
            print(f"You drew a {new_card}. Your cards are now {player}, current total: {player_total}")
        elif player_total > 21:
            winner = closest_number(target=21, num1=player_total, num2=dealer_total)
            print(f"and the winner is: {winner}")
        else:
            return
            
    # Dealer draws cards
    while dealer_total < 21:
        new_card = random.choice(cards)
        dealer.append(new_card)
        dealer_total = sum(dealer)
        print(f"Dealer draws a {new_card}. Dealer's cards are now {dealer}, current total: {dealer_total}")
        winner = closest_number(target=21, num1=player_total, num2=dealer_total)
    print(winner)

    
blackjack()
