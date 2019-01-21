"""
This module demo of Blackjack game.
"""

import random
from pyfiglet import Figlet
from collections import namedtuple

SUITS = {'HEARTS', 'CLUBS', 'DIAMONDS', 'SPADES'}

NUMBERS = {'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6,
           'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10, 'JACK': 10,
           'QUEEN': 10, 'KING': 10, 'ACE': 11}


def ascii_blackjack():
    """ Just for fun """
    figlet = Figlet(font='big')
    print(figlet.renderText('I  WANT  TO  PLAY  A  GAME'))
    print('-'*100)
    print(figlet.renderText('BLACKJACK'))


def cut_cards():
    """
    This function creating and shuffling the deck
    :return: shuffle decks
    """
    cards = namedtuple('Cards', 'value suit')
    cut_decks = []
    for suit in SUITS:
        for value in NUMBERS:
            decks = cards(*(value, suit))
            cut_decks.append(decks)

    random.shuffle(cut_decks)
    return cut_decks


def hit_cards(cut_decks):
    """
    This function pull the card from the deck
    :return: Card(value and suit)
    :param cut_decks: It's a shuffle decks
    """
    cards = [cut_decks.pop(), cut_decks.pop()]
    return cards


def score(score1, score2=0):
    """
    This function score calculator
    :param score1, score2: Card scores. score2 default value '0'
    """
    total = 0
    for item in NUMBERS.items():
        if (item[0] == score1 or item[0] == score2) and (score1 == score2):
            total += 2*item[1]
        elif item[0] == score1 or item[0] == score2:
            total += item[1]
    return total


def play_player(cut_decks):
    """
    This function played player
    :param cut_decks: It's a shuffle decks
    """
    ace_flag = True
    cards = hit_cards(cut_decks)
    scores = [cards[0].value, cards[1].value]
    total_player = score(scores[0], scores[1])
    print('YOUR CARDS')
    print('-'*20)
    print(cards[0].value, '-', cards[0].suit, '//',
          cards[1].value, '-', cards[1].suit)
    if (cards[0].suit == cards[1].suit) and cards[0].suit == 'ACE':
        total_player -= 10
        print(total_player)
    else:
        print(total_player)
        while True:
            if total_player == 21:
                print('WOW BLACKJACK!!! YOU WIN')
                break
            elif total_player < 21:
                choice = input("Hit or stand ? Make your choice (h/s).. -> ")

                if choice == 's':
                    print('BENİM KUMARIM BURDA BİTER')
                    play_dealer(cut_decks, total_player)
                    break
                elif choice == 'h':
                    card3 = cut_decks.pop()
                    score3 = card3.value
                    total_player += score(score3)
                    print(card3.value, '-', card3.suit)
                    if (total_player > 21) and (cards[0].value == 'ACE' or
                                                cards[1].value == 'ACE') \
                                                and ace_flag:
                        total_player -= 10
                        ace_flag = False
                        print(total_player)
                    elif (total_player > 21) and (card3.value == 'ACE'):
                        total_player -= 10
                        print(total_player)
                    else:
                        print(total_player)
            else:
                print('İki zara 100lük oldun')
                break


def play_dealer(cut_decks, total_player):
    """
    This function played dealer
    :param cut_decks: It's a shuffle decks
     """
    ace_flag = True
    cards = hit_cards(cut_decks)
    scores = [cards[0].value, cards[1].value]
    total_dealer = score(scores[0], scores[1])
    print('\nDEALER CARDS')
    print("-"*20)
    print(cards[0].value, '-', cards[0].suit, '//',
          cards[1].value, '-', cards[1].suit)
    if (cards[0].suit == cards[1].suit) and cards[0].suit == 'ACE':
        total_dealer -= 10
        print(total_dealer)
    else:
        print(total_dealer)
        while True:
            if total_player == total_dealer and total_dealer > 17:
                print('PUSH')
                break
            elif total_player < total_dealer <= 21:
                print('KASA HER ZAMAN KAZANIR')
                break
            elif total_dealer < 17:
                card5 = cut_decks.pop()
                score5 = card5.value
                total_dealer += score(score5)
                print(card5.value, '-', card5.suit)
                if (total_dealer > 21) and (cards[0].value == 'ACE' or
                                            cards[1].value == 'ACE') \
                                            and ace_flag:
                    total_dealer -= 10
                    ace_flag = False
                    print(total_dealer)
                elif (total_dealer > 21) and (card5.value == 'ACE'):
                    total_dealer -= 10
                    print(total_dealer)
                else:
                    print(total_dealer)
            else:
                print('BARİ ZARDAN DÜŞSEYDİK')
                break


ascii_blackjack()
cut_decks = cut_cards()
play_player(cut_decks)
