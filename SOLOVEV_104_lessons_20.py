###Домашнее задание № 1 ###
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'В', 'Д', 'К', 'А']
suit = ['пик', 'креста', 'бубна', 'черва']


class CardDeck:
    def __init__(self, vel):
        self.vel = vel
        self.step = 0

    def __next__(self):
        if self.step <= self.vel:
            self.step += 1
            for x in deck:
                for y in suit:
                    print(x, y)
            return 'Карт больше нет'
        else:
            raise StopIteration


newcard = CardDeck(53)
print(next(newcard))

