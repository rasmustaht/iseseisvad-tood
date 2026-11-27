def perfect_shuffle(cards):    
    half = len(cards) // 2
    first = cards[:half]
    second = cards[half:]
    shuffled = []
    for i in range(half):
        shuffled.append(first[i])
        shuffled.append(second[i])
    return shuffled
print(perfect_shuffle([1, 2, 3, 4, 5, 6]))