#zad 1 str 165

import random

word_list1 = ["lampa","nos","stolik","ucho","piórnik","palec"]
word_list2 = []
item_of_list2 = ""

while len(word_list1) != len(word_list2):
	item_of_list2 = random.choice(word_list1)
	if item_of_list2 in word_list2:
		item_of_list2 = random.choice(word_list1)
	else:
		word_list2.append(item_of_list2)

print(word_list2)
#input()