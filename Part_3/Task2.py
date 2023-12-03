from tkinter import *
from datetime import date

import sqlite3

#connect to the DB and create a table
conn = sqlite3.connect('library.db')

add_library_table_c = conn.cursor()

#create tables
add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS PUBLISHER
                            (
<<<<<<< HEAD
                                Publisher_Name  VARCHAR     NOT NULL,
                                Phone           VARCHAR,
                                Address         VARCHAR,

                                PRIMARY KEY (Publisher_Name)
=======
                                Publisher_Name  text,
                                Phone           text,
                                Address         text
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH
                            (
<<<<<<< HEAD
                                Branch_Id       INT             AUTO_INCREMENT,
                                Branch_Name     VARCHAR     NOT NULL,
                                Branch_Address  VARCHAR     NOT NULL,

                                PRIMARY KEY (Branch_Id)
=======
                                Branch_Id       integer,
                                Branch_Name     text,
                                Branch_Address  text
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BORROWER
                            (
<<<<<<< HEAD
                                Card_No         INT         AUTO_INCREMENT,
                                Name            VARCHAR     NOT NULL,
                                Address         VARCHAR     NOT NULL,
                                Phone           VARCHAR     NOT NULL,

                                PRIMARY KEY (Card_No)
=======
                                Card_No         integer,
                                Name            text,
                                Address         text,
                                Phone           text
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BOOK
                            (
<<<<<<< HEAD
                                Book_Id         INT         AUTO_INCREMENT,
                                Title           VARCHAR     NOT NULL,
                                Publisher_Name  VARCHAR     NOT NULL,

                                PRIMARY KEY (Book_Id),
                                FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER (Publisher_Name)
                                ON UPDATE CASCADE
=======
                                Book_Id         integer,
                                Title           text,
                                Publisher_Name  text
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BOOK_LOANS
                            (
                                Book_Id         integer,
                                Branch_Id       integer,
                                Card_No         integer,
                                Date_Out        date,
                                Due_Date        date,
                                Returned_date   date
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BOOK_COPIES
                            (
                                Book_Id         integer,
                                Branch_Id       integer,
                                No_Of_Copies    integer
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BOOK_AUTHORS
                            (
<<<<<<< HEAD
                                Book_Id         INT             NOT NULL,
                                Author_Name     VARCHAR         NOT NULL,

                                PRIMARY KEY (Book_Id, Author_Name),
                                FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE
=======
                                Book_Id         integer,
                                Author_Name     text
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
                            )''')

#commit any changes to DB if any other connections are open
conn.commit()
conn.close()

def checkout():
    sq_conn = sqlite3.connect('library.db')
    sq_cur = sq_conn.cursor()

    sq_cur.execute("INSERT INTO BOOK_LOANS VALUES(:Book_Id, :Branch_Id, :Card_No, :Date_Out, Due_Date)",
                   {
                       'Book_Id': book_id.get(),
                       'Branch_Id': branch_id.get(),
                       'Card_No': card_no.get(),
                       'Due_Date': due_date.get(),
                       'Date_Out': date.today()
                   })
    
    sq_cur.execute("SELECT Title FROM BOOK WHERE Book_Id = ?",(book_id.get))
    record = sq_cur.fetchall()
    

    sq_conn.commit()
    sq_conn.close()
    
#create Tkinter Window
root = Tk()
root.title('Library Main Menu')
root.geometry("400x400")

<<<<<<< HEAD
root.mainloop()












=======
card_no = Entry(root, width = 30)
card_no.grid(row=0,column=1, padx=20)

book_id = Entry(root, width=30)
book_id.grid(row=1,column=1,padx=20)

branch_id = Entry(root, width=30)
branch_id.grid(row=2,column=1)

due_date = Entry(root, width=30)
due_date.grid(row=3, column=1)

card_no_label = Label(root, text='Card Number: ')
card_no_label.grid(row=0, column=0)

book_id_label = Label(root, text='Checkout Book ID: ')
book_id_label.grid(row=1,column=0)

branch_id_label = Label(root, text='Library ID: ')
branch_id_label.grid(row=2,column=0)

due_date_label = Label(root, text='Due Date: ')
due_date_label.grid(row=3, column=0)

loan_btn = Button(root, text='Checkout', command=checkout)
loan_btn.grid(row = 9, column=0, columnspan=2, padx=10, ipadx=100)

root.mainloop()
>>>>>>> 81d43974cd095466c502380ea94e73ab5bb02e2b
