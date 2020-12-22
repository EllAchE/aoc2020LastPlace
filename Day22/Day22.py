# Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.
#
# For example, consider the following starting decks:
#
# Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10
# This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.
#
# The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:
#
# -- Round 1 --
# Player 1's deck: 9, 2, 6, 3, 1
# Player 2's deck: 5, 8, 4, 7, 10
# Player 1 plays: 9
# Player 2 plays: 5
# Player 1 wins the round!
#
# -- Round 2 --
# Player 1's deck: 2, 6, 3, 1, 9, 5
# Player 2's deck: 8, 4, 7, 10
# Player 1 plays: 2
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 3 --
# Player 1's deck: 6, 3, 1, 9, 5
# Player 2's deck: 4, 7, 10, 8, 2
# Player 1 plays: 6
# Player 2 plays: 4
# Player 1 wins the round!
#
# -- Round 4 --
# Player 1's deck: 3, 1, 9, 5, 6, 4
# Player 2's deck: 7, 10, 8, 2
# Player 1 plays: 3
# Player 2 plays: 7
# Player 2 wins the round!
#
# -- Round 5 --
# Player 1's deck: 1, 9, 5, 6, 4
# Player 2's deck: 10, 8, 2, 7, 3
# Player 1 plays: 1
# Player 2 plays: 10
# Player 2 wins the round!
#
# ...several more rounds pass...
#
# -- Round 27 --
# Player 1's deck: 5, 4, 1
# Player 2's deck: 8, 9, 7, 3, 2, 10, 6
# Player 1 plays: 5
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 28 --
# Player 1's deck: 4, 1
# Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
# Player 1 plays: 4
# Player 2 plays: 9
# Player 2 wins the round!
#
# -- Round 29 --
# Player 1's deck: 1
# Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
# Player 1 plays: 1
# Player 2 plays: 7
# Player 2 wins the round!
#
#
# == Post-game results ==
# Player 1's deck:
# Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
# Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:
#
#    3 * 10
# +  2 *  9
# + 10 *  8
# +  6 *  7
# +  8 *  6
# +  5 *  5
# +  9 *  4
# +  4 *  3
# +  7 *  2
# +  1 *  1
# = 306
# So, once the game ends, the winning player's score is 306.
#
# Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?

data = open("input.txt", "r")
# copy the data to a list
lst = data.read().split("\n")[:-1]

p1 = [int(i) for i in lst[1:26]]
p2 = [int(i) for i in lst[28:]]

while len(p1) > 0 and len(p2) > 0:
    if p1[0] > p2[0]:
        p1.append(p1[0])
        p1.append(p2[0])
        p1.pop(0)
        p2.pop(0)
    elif p1[0] < p2[0]:
        p2.append(p2[0])
        p2.append(p1[0])
        p1.pop(0)
        p2.pop(0)

winner = []
if len(p1) > 0:
    winner = p1
else:
    winner = p2

ans = 0
for i in range(1, len(winner) + 1):
    ans += (winner[-i] * i)
print("Part 1:", ans)



# --- Part Two ---
# You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.
#
# Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:
#
# Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
# Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
# If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
# Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
# As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.
#
# Here is an example of a small game that would loop forever without the infinite game prevention rule:
#
# Player 1:
# 43
# 19
#
# Player 2:
# 2
# 29
# 14
# During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the 3 and 7 cards that were drawn.)
#
# To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)

p1 = [int(i) for i in lst[1:26]]
p2 = [int(i) for i in lst[28:]]

# p1 = [9, 2, 6, 3, 1]
# p2 = [5, 8, 4, 7, 10]


def game(deck1, deck2):
    played = []
    while len(deck1) > 0 and len(deck2) > 0:
        win = 1
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if [deck1, deck2] in played:
            return 1, deck1
        else:
            played.append([deck1[:], deck2[:]])
            if len(deck1) >= card1 and len(deck2) >= card2:
                # Recurse
                win = game(deck1[:card1], deck2[:card2])[0]
            else:
                if card1 > card2:
                    # Player 1
                    win = 1
                elif card1 < card2:
                    # Player 2
                    win = 2
        if win == 1:
            deck1.append(card1)
            deck1.append(card2)
        elif win == 2:
            deck2.append(card2)
            deck2.append(card1)
    if len(deck1) > 0:
        return 1, deck1
    else:
        return 2, deck2


winner = game(p1, p2)[1]
ans = 0
for i in range(1, len(winner) + 1):
    ans += (winner[-i] * i)
print("Part 2:", ans)
