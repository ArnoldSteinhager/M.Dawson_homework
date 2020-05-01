#zad 1 s 132

import random

print("\n\tWymyśl z jakiego zakresu losować liczby.\n")
poczatek = int(input("Podaj liczbę początkową: "))
koniec = int(input("Podaj liczbę końcową: "))
krok = int(input("Podaj wielkość odstępu między liczbami: "))

print("\nTwoja liczba to: ")
for i in range(poczatek,koniec,krok):
	print(i, end=" ")
input()