#zad 4 s 132

import random

#sekwencja do słów wyboru
WORDS = ("kupa","jabłko","piłka","rower","czapka","syfon")
wybrane_slowo = random.choice(WORDS)

	
#rozpoczęcie gry
print(
"""
			Witaj w grze 'Zgadnij słowo'!
			
	Wymyśliłem słowo, spróbuj je odgadnąć.
(Aby zakończyć zgadywanie, naciśnij ENTER bez podawania odpowiedzi.)
"""
)
print("\nSłowo zawiera :", len(wybrane_slowo), "liter.")
print("Teraz możesz pięć razy zapytać, czy dana litera jest w wyrazie.")
for i in range(5):
	pytanie = input("Czy ta litera jest w wyrazie? [podaj literę] ")
	if pytanie.lower() in wybrane_slowo:
		print("\tTAK")
	else:
		print("\tNIE")
print("*"*40)
odpowiedz = input("Czas na odpowiedz, więc jakie to słowo? ")
if odpowiedz.lower() == wybrane_slowo:
	print("UDAŁO SIĘ!\a")
else:
	print("nie udało Ci się :( to słowo to: ", wybrane_slowo)

input()