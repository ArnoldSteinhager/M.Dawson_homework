#Zadanie 2 str 253
# Klasa telewizor

import time, os

class Telewizor(object):
	"""Wirtualny tylywizor"""
	
	
	def __init__(self, brand = "Noname", res = "1920x1080"):
		#private:
		self.__PROD_DATE = time.strftime("%Y-%m-%d", time.localtime()) 
		self.__BRAND = brand
		self.__RESOLUTION = res
		MAX_VOL = 100
		MIN_VOL = 0
		self.__canal_list = ["***", "TVP1", "TVN", "TV4"]
		self.__no_of_canals = len(self.__canal_list)
		self.__actually_screen = []
		
		#public
		self.volume_lvl = 1
		self.channel_now = 0
		self.powered_on = False

	def show_empty_screen(self):
		ekw = []
		ekw.append("="*45 + "\t\t" + "="*15)
		for i in range(10):
			ekw.append("||" + (" "*115) + "||" + "\t\t" + "||")
		ekw.append("="*45 + "\t\t" + "||")
		ekw.append(" \\"*2 + (" "*112) + "// " + "\t\t" + "||")
		ekw.append(" "*3 + ("="*43) + "\t\t" + "||")
		ekw.append(" "*45 + "||" + " "*20 + "||" + "\t\t\t\t\t" + "||")
		ekw.append(" "*44 + "//" + " "*22 + "\\"*2 + "\t\t\t\t\t" + "||")
		ekw.append(" "*31 + "="*20 + "\t\t\t\t" + "="*15)
		#przyciski na pilocie
		ekw[1] += " "*7 + "___" + " "*7 + "  ___" + " "*7 + "||"
		ekw[3] += " "*6 + "|__ |" + " "*6 + " |___|" + " "*6 + "||"
		ekw[4] += " "*7 + "___" + " "*7 + "  ___" + " "*7 + "||"
		ekw[6] += " "*6 + "|__ |" + " "*6 + " |___|" + " "*6 + "||"
		ekw[7] += " "*7 + "___" + " "*7 + "  ___" + " "*7 + "||"
		ekw[11] += " "*6 + "|__ |" + " "*6 + " |___|" + " "*6 + "||"
		ekw[12] += " "*7 + "___" + " "*7 + "  ___" + " "*7 + "||"
		ekw[14] += " "*6 + "|__ |" + " "*6 + " |off |" + " "*6 + "||"
		#etykiety na przyciskach
		ekw[2] += " "*6 + "|" + " "*1 + "1" + " "*2 + "|" + " "*7 + "|" + " " + " "*1 + "2" + " "*2 + "|" + " "*6 + "||"
		ekw[5] += " "*6 + "|" + " "*1 + "3" + " "*2 + "|" + " "*7 + "|" + " " + " "*1 + "0" + " "*2 + "|" + " "*6 + "||"
		ekw[8] += " "*6 + "|" + " V+" + "|" + " "*7 + "|" + " P+" + "|" + " "*6 + "||"
		ekw[9] += " "*6 + "|" + " "*1 + "   " + " " + "|" + " "*7 + "|" + " " + "    " + " " + "|" + " "*6 + "||"
		ekw[10] += " "*6 + "|" + " V- " + "|" + " "*7 + "|" + " P- " + "|" + " "*6 + "||"
		ekw[13] += " "*6 + "|" + " "*2 + "i" + " "*2 + "|" + " "*7 + "|" + " on " + "|" + " "*6 + "||"
		ekw[15] += " "*35 + "||"

		#dodanie marki tv
		if self.__actually_screen:
			temp = self.__actually_screen[12][:50]
			temp += self.__BRAND
			temp += self.__actually_screen[12][len(temp)+len(text):]
			self.__actually_screen[12] = temp		
		
		return ekw
	
	def __edit_screen(self, line=0, text=""):
		if self.__actually_screen:
			if line is 1: #jeśli to nazwa kanału
				temp = self.__actually_screen[line][:117-((len(text))*4)]
				temp += text
				temp += self.__actually_screen[line][len(temp)+len(text):]
				self.__actually_screen[line] = temp
			elif line in range(2,12):
				temp = self.__actually_screen[line][:5]
				temp += text
				temp += self.__actually_screen[line][len(temp)+(len(text)//2)+2:]
				self.__actually_screen[line] = temp
				
	def show_updated_screen(self):
		#dodanie nazwy kanału
		self.__edit_screen(1, self.__canal_list[self.channel_now])
		#dodanie poz. głośności
		self.__edit_screen(10, ("vol. lvl: " + str(self.volume_lvl)))
		for line in self.__actually_screen:	
			print(line)
	
	def __str__(self):
		technical_info = ("*"*40) + "/"
		technical_info += "Techniczne informacje o produkcie: /"
		technical_info += "Data produkcji: " + self.__PROD_DATE + "/"
		technical_info += "Producent: " + self.__BRAND + "/"
		technical_info += "Rozdzielczość ekranu: " + self.__RESOLUTION + "/"
		technical_info += "Liczba kanałów: " + str(self.__no_of_canals) + "/"
		technical_info += "Dostępne kanały: " + str(self.__canal_list) + "/"
		technical_info += ("*"*40) + "/"
		return technical_info
		
	def __change_ch(self, how_much):
		"""przeskocz kanał o jeden"""
		if 0 <= self.channel_now <= (self.__no_of_canals-1): 
			if how_much < 0 and self.channel_now > 0: #zmniejszanie kanału
				self.channel_now += (how_much)
			if how_much > 0 and self.channel_now < (self.__no_of_canals-1): #zwiększanie kanału
				self.channel_now += (how_much)

	def __change_vol(self, how_much):
		"""zmień głośność o jeden stopień"""
		if MIN_VOL <= self.volume_lvl <= MAX_VOL:
			if how_much < 0 and self.volume_lvl > MIN_VOL: #zmniejszanie głośności
				self.volume_lvl += (how_much)
			if how_much > 0 and self.volume_lvl < MAX_VOL: #zwiększanie głośności
				self.volume_lvl += (how_much)

	def __power_off(self):
		"""czyść ekran - wyłącz tv"""
		self.__actually_screen = self.show_empty_screen()
		self.powered_on = False
		
	def __power_on(self):
		"""czyść ekran - włącz tv"""
		self.__actually_screen = self.show_empty_screen()
		self.show_updated_screen()
		self.powered_on = True
		
	def pilot(self, some_button):
		"""Uzyj pilota do TV"""
		available_buttons = ("0","1","2","3","v+","v-","p+","p-", "off", "on", "inf")
		if self.powered_on == True:
			if some_button == "0" or "1" or "2" or "3":
				self.channel_now = some_button
			elif some_button == "v+":
				self.__change_vol(1)
			elif some_button == "v-":
				self.__change_vol(-1)
			elif some_button == "p+":
				self.__change_ch(1)
			elif some_button == "p-":
				self.__change_ch(-1)
			elif some_button == "off":
				self.__power_off()
			elif some_button == "inf":
				#zamiana stringu z __str__() na listę
				temp_str = []
				temp_str = self.__str__(self)
				technical_info = []
				while temp_str:
					position = temp_str.find("/")
					technical_info.append(temp_str[:position])
					temp_str = temp_str[position+1:]
				i = 2
				for line in technical_info:
					__edit_screen(j, line)
					j += 1
				show_updated_screen()
		else:
			if some_button == "on":	
				self.__power_on()
				
			
#//////////////////////////////////////////////////////////////////////////////////
# głowna część programu		
AVAILABLE_BUTTONS = ("0","1","2","3","v+","v-","p+","p-", "off", "on", "inf")
print("\tWitaj w programie \"Klasa telewizor\". (aby wyjść naciśnij ENTER...)")
marka = input("Jakiej marki TV chcesz utworzyć? ")
res = input("Jakiej rozdzielczości? ")
tv = Telewizor(marka,res)
pierwszy_ekran = tv.show_empty_screen()
for line in pierwszy_ekran:
	print(line)
#przycisk = None
przycisk = input().lower()

while(przycisk not in AVAILABLE_BUTTONS):
	przycisk = input().lower()
os.system("cls")
tv.pilot(przycisk)

input("Do widzenia!")
			