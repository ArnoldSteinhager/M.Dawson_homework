#zad 4 str 98

import random

print("\n\t\tWitaj w grze \"Jaka to liczba?\"\n")
print("Pomyśl liczbe z zakresu od 1 do 100, sprawdzimy czy ją odgadnę.")

liczba_prob = 0
odpowiedz = ""
while liczba_prob < 10:
	print("\nCzy pomyślałeś o: ", random.randint(1,100))
	odpowiedz = input()
	if odpowiedz == "tak":
		print("ODGADŁEM!")
		break
	elif odpowiedz == "nie":
		print("...hmm spróbuję jeszcze raz")
	else:
		print("...postaraj się odpowiadać tak lub nie")
	liczba_prob += 1
	
if liczba_prob < 10:
	input("bye bye")
else:
	input("Nie udało mi się :(")