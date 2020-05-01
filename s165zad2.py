# Zad 2 str 165

import os #dla "cls" w konsoli

punkty = 30
atrybuty = {"SIŁA":0, "ZDROWIE":0, "MĄDROŚĆ":0, "ZRĘCZNOŚĆ":0}
tytul_progr = "\t\t\tKreator postaci z podziałem na role\n\n"
menu = " punktów aby rozdzielić je pomiędzy atrybuty."
menu_pytanie = ("[0]Wyjście z programu","[1]Rozwijamy atrybut","[2]Zmniejszamy atrybut")


#Główne menu
print(tytul_progr)
print("Masz ",punkty,menu,"\n",atrybuty,"\n\t",menu_pytanie[1],"\n\t",menu_pytanie[2],"\n\t",menu_pytanie[0],"\n")

#Główna pętla programu
wybor_menu = ""
atr_szukany = ""
#dopóki punkty są >0 lub "wyjście z programu"
while punkty or wybor_menu == "0":
	wybor_menu = input()
	if wybor_menu == "1" or wybor_menu == "2":
		atr_szukany = input("\tktóry? ")
		atr_szukany = atr_szukany.upper()
		#jeśli taki klucz zawiera się w słowniku
		if atr_szukany in atrybuty:
			wartosc = int(input("\to ile zmieniamy? "))
			#zwiekszamy atrybut
			if wybor_menu == "1":
				punkty = punkty - wartosc
				atrybuty[atr_szukany] += wartosc
			#zmniejszamy atrybut	
			elif wybor_menu == "2":
				if atrybuty[atr_szukany] >= wartosc:
					atrybuty[atr_szukany] -= wartosc
					punkty = punkty + wartosc
				elif atrybuty[atr_szukany] == 0:
					input("\todjąłeś zbyt dużo,atrybut musi być >= 0.")
				else:
					input("\todjąłeś zbyt dużo,atrybut musi być >= 0 ...zwracam różnicę pkt.")
					wartosc = wartosc - atrybuty[atr_szukany]
					punkty = punkty + wartosc
					atrybuty[atr_szukany] = 0
		else:
			input("\tnie ma takiego atrybutu, spróbuj jeszcze raz.")
		
		os.system("cls") #czyszczenie ekranu
		print(tytul_progr,"\nMasz ",punkty,menu,"\n",atrybuty,"\n\t",menu_pytanie[1],"\n\t",menu_pytanie[2],"\n\t",menu_pytanie[0],"\n")
	elif wybor_menu == "0":
		break
	else:
		input("nieprawidłowy wybór, spróbuj jeszcze raz.")
	if punkty == 0:
		print("\nWykorzystałeś wszystkie punkty!")
#Wyjście z programu
print("\nDo widzenia!")
input()