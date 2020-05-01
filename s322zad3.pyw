#Zadanie 3 str. 322
# "Złóż zamówienie"

from tkinter import *

class Application(Frame):
	"""Aplikacja 'złóż zamówienie'"""
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		Label(self, text = "Witaj w programie \"Złóż zamówienie\".").grid(row = 0, column = 0, columnspan = 2, sticky = W)
		Label(self, text = "Menu:").grid(row = 2, column = 0, columnspan = 2, sticky = W)
		#utwórz zmienne i pola wyboru
		self.salatka = BooleanVar()
		Checkbutton(self, text = "Sałatka - 5 zł", variable = self.salatka, command = self.update_bill
					).grid(row = 3, column = 0, sticky = W)
		self.kotlet = BooleanVar()
		Checkbutton(self, text = "Kotlet - 10 zł", variable = self.kotlet, command = self.update_bill
					).grid(row = 4, column = 0, sticky = W)		
		self.kartofle = BooleanVar()
		Checkbutton(self, text = "Kartofle - 7 zł", variable = self.kartofle, command = self.update_bill
					).grid(row = 5, column = 0, sticky = W)
		#utwórz pole tekstowe do wyświetlenia bieżącego rachunku
		self.actual_bill = Text(self, width = 30, height = 3, wrap = WORD)
		self.actual_bill.grid(row = 7, column = 0, columnspan = 3)
	
	def update_bill(self):
		"""zaktualizuj bieżący rachunek klienta"""
		total_prise = 0
		if self.salatka.get():
			total_prise += 5
		if self.kotlet.get():
			total_prise += 10
		if self.kartofle.get():
			total_prise += 7
			
		self.actual_bill.delete(0.0, END)
		self.actual_bill.insert(0.0, "Twój aktualny rachunek:\n")
		self.actual_bill.insert(3.0, str(total_prise)+" PLN")
		
#część główna programu
root = Tk()
root.title("Zamówienie klienta")
app = Application(root)
root.mainloop()

		