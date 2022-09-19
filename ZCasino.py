#!/usr/local/bin/python3.10

import random

colorList = ["rouge", "noir"]

checkParams = bool(False)

while checkParams == bool(False) :
  number = input("Quelle est le nombre joué (entre 0 et 49)?\n")
  color = input("Quelle est la couleur choisie (rouge ou noir)?\n")
  bet = input("Quelle est la somme misée?\n")
  if(number.isnumeric() and int(number) >= 0 and int(number) <= 49 and bet.isnumeric() and color in colorList) :
    number = int(number)
    bet = int(bet)
    checkParams = bool(True)
  else :
    print("\nVeuillez rentrer des nombres ou des couleurs valides\n")

print("Vous avez parié " + str(bet) + "$ sur le " + str(number) + " " + color + "\n")

winningNumber = random.randint(0, 49)

winningColor = random.choice(colorList)

print("\nLe numéro gagnant est le " + str(winningNumber) + " " + winningColor + "\n")


gain = bet
if(number == winningNumber) :
  gain = gain * 3
  print("Le numéro sélectionné est correct, multiplication de la somme pariée par 3\n")

if(color == winningColor) :
  gain = float(gain) * 1.5 
  print("La couleur sélectionnée est correcte, multiplication de la somme pariée par 1,5\n")

if(gain == bet) :
  gain = 0

print("\nVous avez remporté " + str(gain) + "$")
  
