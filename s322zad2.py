#Zadanie 2 str 322

from tkinter import *

class Application(Frame):
	"""Aplikacja 'jak to liczba' oparta na GUI"""
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.num_tries = 0 #liczba prób
		self.create_widgets()
		
	def create_widgets(self):
		Label(self, text = "Witaj w grze \"Jaka to liczba\".").grid(row = 0, column = 0, columnspan = 2, sticky = W)
		Label(self, text = "Zgadnij liczbe z zakresu od 1 do 100.").grid(row = 1, column = 0, columnspan = 2, sticky = W)
		#utwórz pole do wpisywania zgadywanej liczby
		self.answ_entry = Entry(self)
		self.answ_entry.grid(row = 3, column = 0, sticky = W)
		#utwórz przycisk zatwierdzający odpowiedź
		self.submit_bttn = Button(self, text = "Sprawdź", command = self.reveal)
		self.submit_bttn.grid(row = 3, column = 3, sticky = W)
		#utwórz Label informujący o rezultacie gry
		self.gameresult_lbl = Label(self, text = "...")
		self.gameresult_lbl.grid(row = 4, column = 0, columnspan = 3, sticky = W)
	
	def reveal(self):
		"""Sprawdź czy odpowiedź jest poprawna"""
		self.num_tries += 1
		import random
		number = random.randint(1,100)
		contents = int(self.answ_entry.get())
		if contents == number:
			self.gameresult_lbl["text"] = "Odgadłeś! wylosowałem: " +str(number)+ " liczba prób:" + str(self.num_tries)
			self.num_tries = 0
		elif contents < number:
			self.gameresult_lbl["text"] = "za mała... wylosowałem: " +str(number)
		else:
			self.gameresult_lbl["text"] = "za duża... wylosowałem: " +str(number)



#************* CZĘŚĆ GŁÓWNA *********************
root = Tk()
root.title("Jaka to liczba")
root.geometry("350x100")
app = Application(root)
root.mainloop()