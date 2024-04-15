from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

contry = ["Германия" , "США" ,"Россия","Франция"]
country_var =  Variable(value=contry)
contry_listbox = Listbox(listvariable=country_var)

contry_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
root.mainloop()