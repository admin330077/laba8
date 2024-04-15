from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


contry = ["Германия" , "США" ,"Россия","Франция"]
country_var =  Variable(value=contry)
contry_listbox = Listbox(listvariable=country_var)
contry_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)

def validate_input():
    selected_country = contry_listbox.get(ACTIVE)
    if selected_country == "США":
        add_item()
    else:
        messagebox.showerror('Ошибка', 'Пожалуйста, выберите страну')
Button(f, text="choose", command=validate_input ).pack(fill=X)

root.mainloop()