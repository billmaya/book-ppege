# Exercise 26 - Handshakes

def printHandshakes(people):
    handshakes = 0

    print(people)

    for x in range(len(people) - 1):
        for y in range(x+1, len(people)):
            print(f'{people[x]} shakes hands with {people[y]}')
            handshakes += 1

    print()
    return handshakes



assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6


