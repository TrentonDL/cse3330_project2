from tkinter import *

import sqlite3

conn = sqlite3.connect('library.db')

add_library_table_c = conn.cursor()

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST PUBLISHER
                            (
                                Publisher_Name  VARCHAR(30)     NOT NULL,
                                Phone           CHAR(12),
                                Address         VARCHAR(60),

                                PRIMARY KEY (Publisher_Name)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST LIBRARY_BRANCH
                            (
                                Branch_Id       INT             AUTO_INCREMENT,
                                Branch_Name     VARCHAR(30)     NOT NULL,
                                Branch_Address  VARCHAR(60)     NOT NULL,

                                PRIMARY KEY (Branch_Id)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST BORROWER
                            (
                                Card_No         INT             AUTO_INCREMENT,
                                Name            VARCHAR(30)     NOT NULL,
                                Address         VARCHAR(60)     NOT NULL,
                                Phone           CHAR(12)        NOT NULL,

                                PRIMARY KEY (Card_No)
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST BOOK
                            (
                                Book_Id         INT             AUTO_INCREMENT,
                                Title           VARCHAR(50)     NOT NULL,
                                Publisher_Name  VARCHAR(30)     NOT NULL,

                                PRIMARY KEY (Book_Id),
                                FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER (Publisher_Name)
                                ON UPDATE CASCADE
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST BOOK_LOANS
                            (
                                Book_Id         INT             NOT NULL,
                                Branch_Id       INT             NOT NULL,
                                Card_No         INT             NOT NULL,
                                Date_Out        DATE            NOT NULL,
                                Due_Date        DATE            NOT NULL,
                                Returned_date   DATE,

                                PRIMARY KEY (Book_Id, Branch_Id, Card_No),

                                FOREIGN KEY (Card_No) REFERENCES BORROWER (Card_No)
                                ON DELETE CASCADE ON UPDATE CASCADE,

                                FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE,

                                FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST BOOK_COPIES
                            (
                                Book_Id         INT             NOT NULL,
                                Branch_Id       INT             NOT NULL,
                                No_Of_Copies    INT             NOT NULL,

                                PRIMARY KEY (Book_Id, Branch_Id),
                                FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id),
                                FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE
                            )''')

add_library_table_c.execute('''CREATE TABLE IF NOT EXIST BOOK_AUTHORS
                            (
                                Book_Id         INT             NOT NULL,
                                Author_Name     VARCHAR(30)     NOT NULL,

                                PRIMARY KEY (Book_Id, Author_Name),
                                FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
                                ON DELETE CASCADE ON UPDATE CASCADE
                            )''')

conn.commit()
conn.close()