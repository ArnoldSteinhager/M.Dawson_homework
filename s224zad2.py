#Zad 2 str 224
#gra "Turniej Wiedzy"

import sys, pickle

def open_file(file_name, mode):
	"""Otwórz plik"""
	try:
		the_file = open(file_name, mode)
	except IOError as e:
		print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
		input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
		sys.exit()
	else:
		return the_file
		
def next_line(the_file):
	"""Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
	line = the_file.readline()
	line = line.replace("/","\n")
	return line
	
def next_block(the_file):
	"""Zwróć kolejny blok danych z pliku kwiz."""
	category = next_line(the_file)
	question = next_line(the_file)
	
	answers = []
	for i in range(4):
		answers.append(next_line(the_file))
	
	correct = next_line(the_file)
	if correct:
		correct = correct[0]
	
	explanation = next_line(the_file)
	
	return category, question, answers, correct, explanation

def welcome(title):
	"""Przywitaj gracza i pobierz jego nazwe."""
	print("\t\t Witaj w turnieju wiedzy!\n")
	print("\t\t", title, "\n")
	
def save_scores(name_and_scores): #Treść zadania 2
	"""Zapisz wyniki do pliku."""
	score_file = open_file("kwiz_scores.dat", "ab")
	pickle.dump(name_and_scores,score_file)
	score_file.close()
	
def load_scores():
	score_file = open_file("kwiz_scores.dat","rb")
	i = 0
	all_scores = []
	all_scores.append(pickle.load(score_file))
	for z in range(10):
		try:
			all_scores.append(pickle.load(score_file))
		except EOFError:
			break
		i += 1
	score_file.close()
	print("\n\t******* LISTA GRACZY **********")
	for j in range(len(all_scores)):
		print(all_scores[j][0], end=" ")
		k = 1
		while k < len(all_scores[j]):
			print("quiz nr.", end=" ")
			print(k,end=" ")
			print(": ",end=" ")
			print(all_scores[j][k],end=" ")
			print(", ", end=" ")	
			k += 1
		print("\n")	
			
def main():
	trivia_file = open_file("kwiz.txt","r")
	title = next_line(trivia_file)
	welcome(title)
	name_and_scores = []
	name_and_scores.append(input("Podaj swoje imię: "))

	category, question, answers, correct, explanation = next_block(trivia_file)
	j = 1
	while category:
		#zadaj pytanie
		print(category)
		print(question)
		for i in range(4):
			print("\t", i+1, "-", answers[i])
		#uzyskaj odpowiedź
		answer = input("Jaka jest Twoja odpowiedź?: ")
		#sprawdź odpowiedź
		if answer == correct:
			print("\nOdpowiedź prawidłowa!", end=" ")
			name_and_scores.append(1)
		else:
			print("\nOdpowiedź niepoprawna.", end=" ")
			name_and_scores.append(0)
		print(explanation)
		print("Wynik:", name_and_scores[j], "\n\n")
		j += 1
		#pobierz kolejny blok
		category, question, answers, correct, explanation = next_block(trivia_file)
	trivia_file.close()
	#zapisz wyniku do pliku
	save_scores(name_and_scores)
	#wyświetl wyniki
	answer = None
	print("\nTo było ostatnie pytanie! Czy chcesz zobaczyć tabelę wyników?")
	while answer not in ("t","n"):
		answer = input().lower()
	if answer == "t":
		load_scores()
	
main()
input("\nAby zakończyć program, naciśnij klawisz Enter.")