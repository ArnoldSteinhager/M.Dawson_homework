# Gra w wisielca

import random
import os


HANGMAN = (
"""
        
        
       
       
        
        
       
       
  ░░░░░░░░░░░░░░
"""
,
"""
        
        
       
       
     ║       
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
        
     ║/        
     ║         
     ║         
     ║       
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/        
     ║         
     ║         
     ║       
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║        
     ║       
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║       
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║      █  
     ║        
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║      █\  
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║     /█\  
     ║       
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║     /█\  
     ║     /   
     ║             
    /║\           
  ░░░░░░░░░░░░░░
"""
,
"""
     ╔══════┬   
     ║/     |   
     ║      |   
     ║      ☺   
     ║     /█\  
     ║     / \  
     ║             
    /║\           
  ░░░░░░░░░░░░░░""")


MAX_FAILS = len(HANGMAN)-1	#przechowuje maksymalną ilość mozliwych błędów
#dostępne wyrazy
WORDS = ("KUBEK","WIADRO","ROWER","PUSZKA","CZAPKA","OGON","BUTY","HULAJNOGA","RAKIETKA","TALERZ","SZAFKA",
"SZALIK","MONITOR","KLAWIATURA","MIODEK","PIESEK","LAPTOP","OKULARY","KOSZULA","SPODNIE","KLAPKI","TRAWNIK",
"BUDYNEK","PIASKOWNICA","ONOMATOPEJA","KAMERDYNER","SZUBIENICA","WIATRACZEK","WIERTARKA","KAMYK","KARTOFEL")

drawn_word = random.choice(WORDS)	#wylosowane słowo
said_letters = ""					#zgadywane (wypowiedziane) litery
hidden_word = "-" * len(drawn_word)	#ukryte słowo, zasłonięte myślnikami
current_letter = " "				#przechowuje aktualnie wciśniętą literę w głównej pętli 
mistakes = 0						#liczba błędnych odpowiedzi

#Główna pętla programu
while drawn_word != hidden_word and mistakes < MAX_FAILS:
	print("""\n			WITAJ W GRZE "WISIELEC"!
\n\tWymyśliłem dla Ciebie wyraz, odgadnij go wprowadzając litery
\tlub wyjdź z gry naciskając ENTER\n\n""")
	print(HANGMAN[mistakes])
	print("\n\tOdgadywane litery: ",said_letters)
	print("\n\n\tWylosowane słowo: [",hidden_word,"]\n")
	current_letter = input("\tJaką literę chcesz sprawdzić? ")
	current_letter = current_letter.upper()
	if current_letter == "":
		break
	elif current_letter in drawn_word:
		input("\a\nDoskonale! ta litera znajduje się w wyrazie.")
		temp_hidden_word = "" #tymczasowa zmienna potrzebna do przepisywania ukrytego wyrazu z odkrytymi literami
		for i in range(len(drawn_word)):
			if current_letter in drawn_word[i]:
				temp_hidden_word += drawn_word[i]
			else:
				temp_hidden_word += hidden_word[i]
		hidden_word = temp_hidden_word
	else:
		mistakes += 1
		said_letters += (current_letter + ",")
		input("\nWyraz nie zawiera takiej litery.")
	if hidden_word == drawn_word:
		input("\n\n\tUdało Ci się odgadnąć wyraz. Gratuluję!")
	os.system("cls") #czyszczenie ekranu
	#opcje pożegnania
if current_letter == "":
	input("\n\n\tDo zobaczenia!")
elif mistakes == MAX_FAILS:
	print(HANGMAN[MAX_FAILS])
	print("\n\n\tNie udało Ci się odgadnąć. Zostałeś powieszony!")
	print("\tWylosowany wyraz to: ",drawn_word, " Spróbuj następnym razem.")
	input()