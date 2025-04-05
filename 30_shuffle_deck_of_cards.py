import itertools,random

deck=list(itertools.product(range(1,14),["Heart","Spade","Diamond","Club"]))

random.shuffle(deck)

for i in range(5):
    print(f"{deck[i][0]} of {deck[i][1]}")
