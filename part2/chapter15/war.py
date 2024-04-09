from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [
        None,
        None,
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, v, s) -> None:
        """スート(マーク)も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self) -> str:
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


# card1 = Card(10, 2)
# card2 = Card(11, 3)
# print(card1 < card2)
# card = Card(3, 2)
# print(card)


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self) -> Card:
        return self.cards.pop()


# deck = Deck()
# for card in deck.cards:
#     print(card)


class Player:
    def __init__(self, name) -> None:
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self) -> None:
        name1 = input("プレイヤー1の名前 ")
        name2 = input("プレイヤー2の名前 ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"このラウンドは {winner} が勝ちました"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f"{p1n} は {p1c}、 {p2n} は {p2c} を引きました"
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("紛争を開始")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 15
                self.wins(self.p2.name)

        self.winner(self.p1, self.p2)

    def winner(self, p1, p2):
        msg = ""
        if p1.wins > p2.wins:
            msg = f"ゲーム終了、{p1.name}の勝利です！"
        if p1.wins < p2.wins:
            msg = f"ゲーム終了、{p2.name}の勝利です！"
        else:
            msg = "ゲーム終了、引き分け！"

        print(msg)


game = Game()
game.play_game()
