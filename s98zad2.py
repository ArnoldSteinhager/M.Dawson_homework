#zad 2 str 98

import random

orzel = 0
reszka = 0
i = 0

while i < 100:
	cyfra = random.randint(0,1)
	if cyfra:
		orzel += 1
	else:
		reszka += 1
	i += 1
		
print("Podczas 100-u rzutów monetą wyszło: orzeł ",orzel, "x ,reszka ",reszka,"x.")
input("\n\nnaciśnij ENTER...")