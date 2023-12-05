from tkinter import *
from datetime import date

import sqlite3

#connect to the DB and create a table
conn = sqlite3.connect('library.db')

add_library_table_c = conn.cursor()

#create tables
add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS PUBLISHER
                            (
                                Publisher_Name  VARCHAR     NOT NULL,
                                Phone           VARCHAR,
                                Address         VARCHAR,

                                PRIMARY KEY (Publisher_Name)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH
                            (
                                Branch_Id       INT             AUTO_INCREMENT,
                                Branch_Name     VARCHAR     NOT NULL,
                                Branch_Address  VARCHAR     NOT NULL,

                                PRIMARY KEY (Branch_Id)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BORROWER
                            (
                                Card_No         INT         AUTO_INCREMENT,
                                Name            VARCHAR     NOT NULL,
                                Address         VARCHAR     NOT NULL,
                                Phone           VARCHAR     NOT NULL,

                                PRIMARY KEY (Card_No)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXISTS BOOK
                            (
                                Book_Id         INT         AUTO_INCREMENT,
                                Title           VARCHAR     NOT NULL,
                                Publisher_Name  VARCHAR     NOT NULL,

                                PRIMARY KEY (Book_Id),
                                FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER (Publisher_Name)
                                ON UPDATE CASCADE
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
                                Book_Id         INT             NOT NULL,
                                Author_Name     VARCHAR         NOT NULL,

                                PRIMARY KEY (Book_Id, Author_Name),
                                FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE
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

root.mainloop()
