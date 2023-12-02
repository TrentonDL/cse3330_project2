#PyQt5 -- pipinstall PyQt5

#Tkinter -- pip3 install tkinter

#Kivy -- pip3 install kivy

from tkinter import *

import sqlite3

#connect to the DB and create a table

conn = sqlite3.connect('address_book.db')

add_book_table_c = conn.cursor()

#create table
add_book_table_c.execute('''CREATE TABLE IF NOT EXISTS ADDRESS(
                            first_name text,
                            last_name text,
                            address text,
                            city text,
                            state text,
                            zipcode integer)''')

#commit any changes to DB if any other connections are open

conn.commit()
conn.close()

def submit():
    submit_conn = sqlite3.connect('address_book.db')
    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO ADDRESS VALUES(:fname, :lname, :street, :city, :state, :zipcode)",
                       {
                           'fname': f_name.get(),
                           'lname': l_name.get(),
                           'street': street.get(),
                           'city': city.get(),
                           'state': state.get(),
                           'zipcode': zcode.get()
                       })
    
    submit_conn.commit()
    submit_conn.close()

def search_query():
    sq_conn = sqlite3.connect('address_book.db')
    sq_cur = sq_conn.cursor()

    sq_cur.execute("SELECT first_name, last_name FROM ADDRESS WHERE city = ? AND state = ?",
                   (city.get(),state.get(),))
    
    records = sq_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record[0] + " " + record[1] + "\n")

    #create label to show records
    search_output = Label(root, text = print_records)
    search_output.grid(row=9, column=0, columnspan=2)

    #sq_conn.commit()
    sq_conn.close()

#create Tkinter Window
root = Tk()

root.title('Address Book')

root.geometry("400x400")

#define components (Widgets) for the Tkinter window

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

street = Entry(root, width = 30)
street.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zcode = Entry(root, width = 30)
zcode.grid(row = 5, column = 1)
#define Labels
f_name_label = Label(root, text='First Name: ')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='Last Name: ')
l_name_label.grid(row=1,column=0)

street_label = Label(root, text='Street: ')
street_label.grid(row=2, column=0)

city_label = Label(root, text='City: ')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State: ')
state_label.grid(row=4, column=0)

zcode_label =Label(root, text='Zip Code: ')
zcode_label.grid(row=5, column=0)

submit_btn = Button(root, text = 'Insert Address', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)

search_btn = Button(root, text = 'Show Records', command= search_query)
search_btn.grid(row=7, column=0, columnspan=2, padx=10, ipadx=100)

#execute the GUI
root.mainloop()