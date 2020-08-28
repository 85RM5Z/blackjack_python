from random import choice, sample
import sys


cartes = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
print("\n")
print("**Bienvenu dans le jeu de BlackJack**\n")
print("Voici les valeur de chaque cartes: \n")

for carte, valeur in cartes.items():
    print("la carte {} vaut {}".format(carte, valeur))

print("\nLet the game begin!\n")
liste_cartes = list(cartes)

print("Vous avez reçu : ", end=" ")
carte = choice(liste_cartes)
score = cartes[carte]
print(carte, end=" ")
carte = choice(liste_cartes)
score += cartes[carte]
print(carte, end="\n")
print("Score actuelle: {}".format(score))
if(score == 21):
    print("*BLACK JACK*")
    print("Victoire, vous avez battu la banque!")

while(True):
    hitOrStand = input("Voulais vous Tirer or Rester:")
    hitOrStand = str(hitOrStand)
    if(hitOrStand == "Tirer" or hitOrStand == "tirer"):
        carte = choice(liste_cartes)
        score += cartes[carte]
        print(carte, end=" ")
        print(" >>> votre nouveau score est de", score)
        if(score>21):
            print("Defaite,la banque vous a battu :(")
            sys.exit()
    elif(hitOrStand == "Rester" or hitOrStand == "rester"):
        print(" >>> votre score finale est de", score)
        break

main_banque = sample(liste_cartes, 2)
score_banque = sum(cartes[carte] for carte in main_banque)
print("La banque a: {} {}  >> son score est de {}".format(main_banque[0],
                                                          main_banque[1],
                                                          score_banque))
if score>score_banque and score_banque<=21:
    print("Victoire, vous avez battu la banque!")
elif score>21:
    print("Defaite,la banque vous a battu :(")
else : print("Defaite,la banque vous a battu :(")
