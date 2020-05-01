#zad 2 str 197

import random

def ask_number(question, low, high):
	"""Poproś o podanie liczby z odpowiedniego zakresu"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response




def main():
	print("\t\tWitaj w grze \"Jaka to liczba?\"\n")
	print("Zgadnij liczbe z zakresu od 1 do 100")

	liczba_prob = 0
	while liczba_prob < 10:
		losowa_liczba = random.randint(1,100)
		odpowiedz = ask_number("Wydaje mi się, że to: ",1,100)
		if losowa_liczba == odpowiedz:
			print("odgadłeś! wylosowałem: ",losowa_liczba, " liczba prób:", liczba_prob)
			break
		elif losowa_liczba < odpowiedz:
			print("za duża... wylosowałem: ",losowa_liczba)
		else:
			print("za mała... wylosowałem: ",losowa_liczba)
		liczba_prob += 1
	print("Nie udało Ci się odgadnąć w 10-u próbach! NUBIE!")
	
main()
input()