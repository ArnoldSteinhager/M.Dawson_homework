#Zadanie 1 str 97

import random

print("Przepowiednia z ciasteczka na dziś: ")
numer = random.randrange(1,5)
if numer == 1:
	print("Będzie padać")
elif numer == 2:
	print("Nie będzie padać")
elif numer == 3:
	print("Spotkasz szczęście")
elif numer == 4:
	print("Wdepniesz w kupę")
elif numer == 5:
	print("Zabraknie prądu")
else:
	print("\n\nCoś poszło nie tak...")
	
input("\n\nnaciśniJ ENTER...")