import sqlite3
from tkinter import *
import tkinter as tk

program = tk.Tk()
program.title("AUTO NOVA INVENTAR")
program.geometry("1280x720")
storeName = "AUTO NOVA"

# ------- Icon imagine -------

icon_image = tk.PhotoImage(file="AUTONOVA logo.png")
program.iconphoto(False, icon_image)

# --------- Background AUTO NOVA --------- #

program.configure(background ="GRAY")

# bgimg= tk.PhotoImage(file = "AUTONOVA logo.png")
# #Specify the file name present in the same directory or else
# #specify the proper path for retrieving the image to set it as background image.
# limg=tk.Label(program, i=bgimg)
# limg.pack()



# --------- FUNCTIONS --------- #


# def reverse(tuples):
#     new_tup = tuples[::-1]
#     return new_tup


def insert( id, nume, pret, cantitate):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemId TEXT, itemNume TEXT, itemPret TEXT, itemCantitate TEXT)""")

    cursor.execute("INSERT INTO inventory VALUES ('" + str(id) + "','" + str(nume) + "','" + str(pret) + "','" +
                   str(cantitate) + "')")
    conn.commit()

def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemNume TEXT, itemPret TEXT, itemCantitate TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()


def update(id, nume, pret, cantitate,  idNume):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemNume TEXT, itemPret TEXT, itemCantitate TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = '" + str(id) + "', itemNume = '" + str(nume) + "', itemPret = '" + str(pret) + "', itemCantitate = '" +
                   str(cantitate) + "' WHERE itemId='"+str(idNume)+"'")
    conn.commit()


def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemNume TEXT, itemPret TEXT, itemCantitate TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results



# --------- LABELs --------- #

titleLabel = Label(program, text=storeName, font=('Calibri bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(program, text="ID", font=('Calibri bold', 12))
numeLabel = Label(program, text="Nume", font=('Calibri bold', 12))
pretLabel = Label(program, text="Pret", font=('Calibri bold', 12))
cantitateLabel = Label(program, text="Cantitate", font=('Calibri bold', 12))
idLabel.grid(row=1, column=0, padx=10, pady=10)
numeLabel.grid(row=2, column=0, padx=10, pady=10)
pretLabel.grid(row=3, column=0, padx=10, pady=10)
cantitateLabel.grid(row=4, column=0, padx=10, pady=10)

entryId = Entry(program, width=25, bd=5, font=('Calibri bold', 12))
entryNume = Entry(program, width=25, bd=5, font=('Calibri bold', 12))
entryPret = Entry(program, width=25, bd=5, font=('Calibri bold', 12))
entryCantitate = Entry(program, width=25, bd=5, font=('Calibri bold', 12))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryNume.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryPret.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryCantitate.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

# --------- BUTTONs --------- #

buttonEnter = Button(
    program, text="Creeaza", padx=5, pady=5, width=6,
    bd=3, font=('Arial', 12), bg="Cadet Blue",)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    program, text="Update", padx=5, pady=5, width=6,
    bd=3, font=('Arial', 12), bg="Cadet Blue", )
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    program, text="Sterge", padx=5, pady=5, width=6,
    bd=3, font=('Arial', 12), bg="Cadet Blue",)
buttonDelete.grid(row=5, column=3, columnspan=1)


program.mainloop()