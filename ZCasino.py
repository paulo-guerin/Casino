#!/usr/local/bin/python3.10

import random

totalMoney = float(input("Quel montant total voulez vous mettre en jeu ?\n"))

checkParams = bool(False)
oddOrEven = "odd"
while checkParams == bool(False) :
  number = input("Quel est le nombre joué (entre 0 et 49)?\n")
  bet = input("Quelle est la somme misée pour ce tour?\n")
  if(number.isnumeric() and int(number) >= 0 and int(number) <= 49 and bet.isnumeric() and totalMoney >= float(bet)) :
    number = int(number)
    bet = int(bet)
    checkParams = bool(True)

    if (number % 2) == 0:
              oddOrEven = "even"
  else :
    print("\nVeuillez rentrer des nombres valides, le montant de votre mise ne doit pas dépasser le montant total qui est de " + str(totalMoney)  + "\n")

print("Vous avez parié " + str(bet) + "$ sur le " + str(number) +"\n")

winningNumber = random.randint(0, 49)
oddOrEvenWinningNumber = "odd"

if (winningNumber % 2) == 0:

              oddOrEvenWinningNumber = "even"

print("\nLe numéro gagnant est le " + str(winningNumber) + "\n")


gain = bet
if(number == winningNumber) :
  gain = gain * 3
  print("Le numéro sélectionné est correct, multiplication de la somme pariée par 3\n")
  totalMoney = totalMoney + gain 

else : 
  if(oddOrEven == oddOrEvenWinningNumber) :
    gain = float(gain) * 1.5 
    print("La couleur sélectionnée est correcte, multiplication de la somme pariée par 1,5\n")
    totalMoney = totalMoney + gain

if(gain == bet) :
  gain = 0
  totalMoney = totalMoney - bet


print("\nVous avez remporté " + str(gain) + "$, votre argent total est de " + str(totalMoney))
  
