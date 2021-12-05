import inspect
import os.path

numbers = []
cards = []
winners = []


class BingoCard:
    winning_number = 0
    winner = False

    def __init__(self, r1, r2, r3, r4, r5):
        self.card = [r1, r2, r3, r4, r5]

    def check_rows(self):
        for row in self.card:
            winner = True
            for element in row:
                if element != -1:
                    winner = False
            if winner:
                return winner

    def check_cols(self):
        for i in range(len(self.card[0])):
            winner = True
            for row in self.card:
                if row[i] != -1:
                    winner = False
            if winner:
                return winner


def load_bingo_cards(file):
    file.seek(0)
    global numbers
    global cards
    numbers = [int(i) for i in file.readline().split(",")]
    card = None
    row = -1

    for line in file.readlines():
        if line == "\n":
            card = BingoCard(None, None, None, None, None)
            row = 0
        else:
            card.card[row] = [int(i) for i in line.strip().split(None)]
            if row == 4:
                cards.append(card)
            row += 1


def play_bingo():
    # for all numbers called
    for number in numbers:
        # mark each card
        for card in cards:
            for i in range(len(card.card)):
                for j in range(len(card.card[i])):
                    if card.card[i][j] == number:
                        card.card[i][j] = -1
        # check for winners and move card to winners list
        # needs to be a separate iteration over cards because indices shift when card moved
        # alternative: don't move cards - requires keeping track of winners in place
        for card in cards:
            if card.check_rows() or card.check_cols():
                card.winning_number = number
                winners.append(card)
                cards.remove(card)


def print_winner_scores():
    for idx, winner in enumerate(winners):
        sum = 0
        for row in winners[idx].card:
            for element in row:
                if element != -1:
                    sum += element
        print(f"winners[{idx}]: {sum * winner.winning_number}")


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            load_bingo_cards(file)
            play_bingo()
            print_winner_scores()
    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
