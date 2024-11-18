
nb_max_spaceships = int(input('Nb de vaisseaux: '))
# spaceship creation
# collect input user
for _ in range(nb_max_spaceships):
    color = input('couleur: ')
    nb_passengers = int(input('nb de passagers: '))
    nb_seats = int(input('nb de places: '))
    name = input('nom: ')

    spaceship = {
        'name': name,
        'color': color,
        'nb_passengers': nb_passengers,
        'nb_seats': nb_seats}
    print(spaceship)
