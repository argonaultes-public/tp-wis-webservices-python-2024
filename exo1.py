# Afficher le message de bienvenue : "Bienvenue ici" (print)
print('Bienvenue ici')
# Puis afficher un message demandant de saisir le nombre de points de vie (input)
# Stocker cette valeur saisie par l'utilisateur dans une variable (opérateur = )
life = input('Nombre de points de vie: ')
print(type(life)) # [0-9] <=> \d
# Afficher un nouveau message demandant de saisir le nombre de dégâts reçus (input)
life = int(life)
print(type(life))
# Stocker cette valeur saisie par l'utilisateur dans une autre variable (opérateur =)
damages = int(input('Dommages : '))
# Afficher ensuite à l'utilisateur le nombre de points de vie restants
print(f"Vie {life}, Dégâts {damages}, Points de vie restants : {life - damages}")
print(("Points de vie restants : ") + str(life - damages))