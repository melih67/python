name = input('Entrez votre Prénom ?\n')
oui = "oui" or "Oui"

''''
if name = blank
  print("Veuillez entrer un prénom s'ils vous plait")
'''


ville = input('Entrez votre ville ? (Strasbourg par défault)\n')
if ville:
  print('Vous avez choisi la ville de ',ville)
else : 
  print('Vous avez pas choisi de ville donc le système à choisi automatiquement Strasbourg')
  ville = "Strasbourg"

age = input('Entrez votre age ? (18 par défault)\n')

if age:
  print('Vous avez choisi',age,'ans')
else : 
  print('Vous avez pas choisi d"age donc le système à choisi automatiquement 18')
  age = "18"



print('Bonjour, %s.' % name)





if input('Voulez-vous afficher votre ville ?\n') == oui :
  print(name,' ,voici la ville dont vous avez écrit ou celle par default : ',ville)


if input('Voulez-vous afficher votre age ?\n') == oui :
  print(name,' ,voici l"age dont vous avez écrit ou celle par default : ',age)