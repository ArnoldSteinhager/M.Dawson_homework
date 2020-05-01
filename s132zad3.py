#zad 3 s 132

import random

#sekwencja do słów wyboru
WORDS = ("python","anagram","łatwy","skomplikowany","odpowiedź","ksylofon")
#sekwencja podpowiedzi
PODPOWIEDZ = ("jęz.programowania","poprzestawiany wyraz","easy po polsku","trudny","prawidłowa lub nie","instrument klawiszowy")
#maksymalna ilość punktów za odpowiedzi
MAX_PTS = 100
#wybierz losowo jedno słowo z sekwencji
#word = random.choice(WORDS) <--- tak było oryginalnie
nr_word = random.randint(0,5)
#zmienna przechowuje poprawną odpowiedź
correct = WORDS[nr_word]
word = WORDS[nr_word]
#zmienna przechowująca pomieszaną wersję słowa
jumble = ""

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position+1):]
	
#rozpoczęcie gry
print(
"""
			Witaj w grze 'Wymieszane litery'!
			
	Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij ENTER bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)
guess = input("\nTwoja odpowiedź: ")

i = 1
uzyte_podpowiedzi = 0
while guess != correct and guess != "":
	print("Niestety, to nie to słowo.")
	if not i%3:
		print("\tTo twoja ", i, " niepoprawna odpowiedź. Potrzebujesz podpowiedź? [t/n]")
		odp = input()
		if "t" in odp:
			print("\tOto podpowiedź: ",PODPOWIEDZ[nr_word])
			uzyte_podpowiedzi += 1
		else:
			print("\t...okej lecimy dalej")
	guess = input("Twoja odpowiedź: ")
	i += 1
if guess == correct:
	if i == 1:
		print("\notrzymałeś max ilość punktów: ", MAX_PTS, "pts!")
	else:
		if uzyte_podpowiedzi:
			print("\n ponieważ używałeś podpowiedzi, otrzymałeś: ", MAX_PTS//((3 * uzyte_podpowiedzi)+i), "pts.")
		else:
			print("\n nie używałeś podpowiedzi więc otrzymałeś: ", MAX_PTS//i, "pts.")
	
	print("\nUdało się! Dziękuję za udział w grze.\a")
input()