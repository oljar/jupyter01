from tkinter import messagebox
class Errors:
    def err_lack_of_file_or_bad_data(self):
        messagebox.showerror('Error','Nie załadowano danych - brak pliku lub błędne dane ')

    def err_lack_of_file(self):
        messagebox.showerror('Error', 'brak pliku')

    def err_bad_data(self):
        messagebox.showerror('Error', 'Coś poszło nie tak. Sprawdź plik i nazwy kolum')