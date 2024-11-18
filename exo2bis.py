
nb_max_spaceships = int(input('Nb de vaisseaux: '))
# spaceship creation
# collect input user
hangar = []
best_ratio = 0
best_vessel = None

# solution 1
for _ in range(nb_max_spaceships):
    color = input('couleur: ')
    nb_passengers = int(input('nb de passagers: '))
    nb_seats = int(input('nb de places: '))
    name = input('nom: ')

    spaceship = (name, color, nb_passengers, nb_seats, nb_passengers / nb_seats)
    hangar.append(spaceship)

    if best_ratio < spaceship[-1]:
        best_ratio = spaceship[-1]
        best_vessel = spaceship

print(f'V1: {best_vessel}')

# solution 2
def get_ratio_passenger(spaceship):
    return spaceship[-1]

result2 = max(hangar, key = get_ratio_passenger)

result1 = max(hangar, key = lambda spaceship : spaceship[-1])

# hangar[idx] ?? => 

print(f'V2: {result1}')
print(f'V3: {result2}')