#zad 3 str 98

import random

print("\t\tWitaj w grze \"Jaka to liczba?\"\n")
print("Zgadnij liczbe z zakresu od 1 do 100")

liczba_prob = 0
while liczba_prob < 10:
	losowa_liczba = random.randint(1,100)
	odpowiedz = int(input("\nTa liczba to: "))
	if losowa_liczba == odpowiedz:
		print("odgadłeś! wylosowałem: ",losowa_liczba, " liczba prób:", liczba_prob)
		break
	elif losowa_liczba < odpowiedz:
		print("za duża... wylosowałem: ",losowa_liczba)
	else:
		print("za mała... wylosowałem: ",losowa_liczba)
	liczba_prob += 1
print("Nie udało Ci się odgadnąć w 10-u próbach! NUBIE!")