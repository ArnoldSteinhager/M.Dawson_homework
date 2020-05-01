# zad 2 s 132

wyraz = input("\nPodaj jakiś wyraz: ")
print("\ntwój wyraz normalnie: ", wyraz)
print("twój wyraz od tyłu: ", end=" ")
print(wyraz[::-1])

print("twój wyraz od tyłu (pętla for): ", end=" ")
for i in range(1, len(wyraz)+1,1):
	print(wyraz[-i], end="")
	
input()
