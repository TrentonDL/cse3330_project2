from tkinter import *
from datetime import date, timedelta
import prettytable

import sqlite3


# THIS IS A PLACEHOLDER FUNCTION

def button_click():
    # Add the functionality you want when a button is clicked
    print("Button clicked!")

def checkout_book():
    def finalize_checkout():

        selected_title = selected_book.get()
    
        # Execute the query for Book_Id after the user has made a selection
        book_id_query = "SELECT Book_Id FROM BOOK WHERE Title = ?"
        curs.execute(book_id_query, (selected_title,))
        book_number = curs.fetchone()  # Use fetchone() instead of fetchall() if expecting one result

        selected_libr = selected_branch.get()

        # Execute the query for Book_Id after the user has made a selection
        branch_id_query = "SELECT Branch_Id FROM LIBRARY_BRANCH WHERE Branch_Name = ?"
        curs.execute(branch_id_query, (selected_libr,))
        branch_number = curs.fetchone()  # Use fetchone() instead of fetchall() if expecting one result

        curs.execute("INSERT INTO BOOK_LOANS VALUES(:Book_Id, :Branch_Id, :Card_No, :Date_Out, :Due_Date, :Returned_Date, :Late)",
            {
                'Book_Id': book_number[0],
                'Branch_Id': branch_number[0],
                'Card_No': card_No.get(),
                'Date_Out': formatted_date,
                'Due_Date': formatted_due_date,
                'Returned_Date': None,
                'Late': 0
            })
        conn.commit()
        conn.close()
        checkout_window.destroy()

        updated_copies_window = Toplevel(root)
        updated_copies_window.title("Updated Books Copies")
        updated_copies_window.geometry("720x360")

        conne = sqlite3.connect('LMS.db')
        cursor = conne.cursor()


        select_query = "SELECT B.Book_Id, B.Title, BC.Branch_Id, LB.Branch_Name, BC.No_Of_Copies FROM BOOK AS B, BOOK_COPIES AS BC, LIBRARY_BRANCH AS LB WHERE B.Book_Id=BC.Book_Id AND BC.Branch_Id=LB.Branch_Id"
        cursor.execute(select_query)
        results = cursor.fetchall()

        table = prettytable.PrettyTable(['Book ID', 'Book Title', 'Branch ID', 'Library Branch', 'Copies Available'])

        for row in results:
            table.add_row(row)

        text_widget = Text(updated_copies_window, wrap=NONE, width=600, height=80)
        text_widget.insert(END, table.get_string())
        text_widget.pack(padx=10, pady=10)


        conne.close()

    # Create a new window
    checkout_window = Toplevel(root)
    checkout_window.title("Check-Out a Book!")
    checkout_window.geometry("300x325")

    conn = sqlite3.connect('LMS.db')
    curs = conn.cursor()

    curs.execute("SELECT Title FROM BOOK")
    books = [row[0] for row in curs.fetchall()]

    label1 = Label(checkout_window, text="Select a book to checkout: ")
    label1.pack(pady=10)

    selected_book = StringVar(checkout_window)
    selected_book.set("Select Book")

    book_dropdown = OptionMenu(checkout_window, selected_book, *books)
    book_dropdown.config(width = 26)
    book_dropdown.pack(pady=10)


    curs.execute("SELECT Branch_Name FROM LIBRARY_BRANCH")
    branches = [row[0] for row in curs.fetchall()]

    label2 = Label(checkout_window, text="Select a library branch to checkout from: ")
    label2.pack(pady=10)

    selected_branch = StringVar(checkout_window)
    selected_branch.set("Select a Branch")

    branch_dropdown = OptionMenu(checkout_window, selected_branch, *branches)
    branch_dropdown.config(width = 26)
    branch_dropdown.pack(pady=10)

    label3 = Label(checkout_window, text="Please enter the borrower card number: ")
    label3.pack(pady=10)

    card_No = Entry(checkout_window, width = 30)
    card_No.pack(pady=10)

    today_date = date.today()
    formatted_date = today_date.strftime('%Y-%m-%d')

    due_date = today_date + timedelta(days=30)
    formatted_due_date = due_date.strftime('%Y-%m-%d')


    confirm_button = Button(checkout_window, text="Check-Out", command=finalize_checkout)
    confirm_button.pack(pady=10)

    checkout_window.grab_set()
    root.wait_window(checkout_window)  # Wait for the checkout window to be closed before continuing

def add_new_user():

    def insert_new_user():
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        new_name = full_name.get()
        new_number = phone.get()

        cursor.execute("INSERT INTO BORROWER VALUES(:Card_No, :Name, :Address, :Phone)",
            {
                'Card_No': None,
                'Name': full_name.get(),
                'Address': address.get(),
                'Phone': phone.get()
            })

        conn.commit()

        new_user_window.destroy()

        new_card_window = Toplevel(root)
        new_card_window.title("New Library Card Number")
        new_card_window.geometry("300x80")

        cursor.execute("SELECT Card_No FROM BORROWER WHERE Name = ? AND Phone = ?", (new_name, new_number, ))
        card_number = cursor.fetchone()

        label1 = Label(new_card_window, text=f"Your New Card Number: {card_number[0]}")
        label1.pack(pady=10)


        conn.close()


    new_user_window = Toplevel(root)
    new_user_window.title("Add A New User")
    new_user_window.geometry("425x150")

    full_name = Entry(new_user_window, width = 30)
    full_name.grid(row = 0, column = 1, padx = 20)

    address = Entry(new_user_window, width = 30)
    address.grid(row = 1, column = 1)

    phone = Entry(new_user_window, width = 30)
    phone.grid(row = 2, column = 1)

    fname_label = Label(new_user_window, text = 'Full Name: ')
    fname_label.grid(row = 0, column = 0)

    address_label = Label(new_user_window, text = 'Address: ')
    address_label.grid(row = 1, column = 0)

    phone_label = Label(new_user_window, text = 'Phone Number: ')
    phone_label.grid(row = 2, column = 0)

    confirm_button = Button(new_user_window, text="Check-Out", command=insert_new_user)
    confirm_button.grid(row = 3, column = 1, padx=10, pady=20)

    new_user_window.grab_set()
    root.wait_window(new_user_window)

def add_books():

    def insert_book():
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        new_book = book_title.get()
        new_author = author_name.get()
        insert_publisher = selected_publisher.get()

        cursor.execute("INSERT INTO BOOK VALUES(:Book_Id, :Title, :Publisher_Name)", 
            {
                'Book_Id': None, 
                'Title': new_book,
                'Publisher_Name': insert_publisher
            })
        conn.commit()

        cursor.execute("SELECT Book_Id FROM BOOK WHERE Title = ? AND Publisher_Name = ?", (new_book, insert_publisher, ))
        new_book_id = cursor.fetchone()

        cursor.execute("INSERT INTO BOOK_AUTHORS VALUES(:Book_Id, :Author_Name)", 
            {
                'Book_Id': new_book_id[0],
                'Author_Name': new_author
            })
        conn.commit()


        branch_ids = [1, 2, 3, 4, 5]

        for branch_id in branch_ids:
            cursor.execute("INSERT INTO BOOK_COPIES VALUES(:Book_Id, :Branch_Id, :No_Of_Copies)",
            {
                'Book_Id': new_book_id[0],
                'Branch_Id': branch_id,
                'No_Of_Copies': 5 
            })
            conn.commit()

        add_book_window.destroy()
        conn.close()

    add_book_window = Toplevel(root)
    add_book_window.title("Add Book to LMS")
    add_book_window.geometry("425x150")

    book_title = Entry(add_book_window, width = 30)
    book_title.grid(row = 0, column = 1, padx = 20)

    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Publisher_Name FROM PUBLISHER")
    publishers = [row[0] for row in cursor.fetchall()]

    conn.close()

    selected_publisher = StringVar(add_book_window)
    selected_publisher.set("Select Publisher")
    publisher_dropdown = OptionMenu(add_book_window, selected_publisher, *publishers)
    publisher_dropdown.config(width = 26)
    publisher_dropdown.grid(row = 1, column = 1, padx = 20)

    author_name = Entry(add_book_window, width = 30)
    author_name.grid(row = 2, column = 1, padx = 20)

    confirm_button = Button(add_book_window, text="Add Book", command = insert_book)
    confirm_button.grid(row = 3, column = 1, padx=10, pady=20)

    book_label = Label(add_book_window, text = 'Book Title: ')
    book_label.grid(row = 0, column = 0)

    publisher_label = Label(add_book_window, text = 'Publisher: ')
    publisher_label.grid(row = 1, column = 0)

    author_label = Label(add_book_window, text = 'Author: ')
    author_label.grid(row = 2, column = 0)

    add_book_window.grab_set()
    root.wait_window(add_book_window)

def loan_records_by_book():
    
    def perform_search():

        selected_title = selected_book.get()
        search_query = "SELECT BL.Branch_Id, LB.Branch_Name, COUNT(*) FROM BOOK_LOANS BL JOIN BOOK B ON BL.Book_Id = B.Book_Id JOIN BOOK_COPIES BC ON B.Book_Id = BC.Book_Id AND BL.Branch_Id = BC.Branch_Id JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id WHERE B.Title = ? GROUP BY BL.Branch_Id, LB.Branch_Name"
        curs.execute(search_query, (selected_title, ))
        loan_record = curs.fetchall()

        select_book_window.destroy()

        book_record_win = Toplevel(root)
        book_record_win.title("Updated Books Copies")
        book_record_win.geometry("350x150")

        table = prettytable.PrettyTable(['Branch ID', 'Branch Name', 'Number Of Copies'])

        for row in loan_record:
            table.add_row(row)

        text_widget = Text(book_record_win, wrap=NONE, width=600, height=80)
        text_widget.insert(END, table.get_string())
        text_widget.pack(padx=10, pady=10)


        conn.close()

    select_book_window = Toplevel(root)
    select_book_window.title("Search Loans")
    select_book_window.geometry("300x150")

    label1 = Label(select_book_window, text="Select a book to search loan records: ")
    label1.pack(pady=10)

    conn = sqlite3.connect('LMS.db')
    curs = conn.cursor()

    curs.execute("SELECT Title FROM BOOK")
    books = [row[0] for row in curs.fetchall()]

    selected_book = StringVar(select_book_window)
    selected_book.set("Select Book")

    book_dropdown = OptionMenu(select_book_window, selected_book, *books)
    book_dropdown.config(width = 26)
    book_dropdown.pack(pady=10)

    confirm_button = Button(select_book_window, text="Search", command = perform_search)
    confirm_button.pack(pady=10)

    select_book_window.grab_set()
    root.wait_window(select_book_window)



#create Tkinter Window

root = Tk()
root.title('Library Main Menu')
root.geometry("400x500")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create six buttons and add them to the window
button1 = Button(root, text="Check-Out A Book", command=checkout_book)
button2 = Button(root, text="Add A New User", command=add_new_user)
button3 = Button(root, text="Add A New Book", command=add_books)
button4 = Button(root, text="Loan Records By Book Title", command=loan_records_by_book)
button5 = Button(root, text="Find Late Books By Due Date", command=button_click)
button6 = Button(root, text="Book Loan Information", command=button_click)

# Use the grid manager to arrange the buttons in a grid layout
button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=1, column=0, sticky="nsew")
button4.grid(row=1, column=1, sticky="nsew")
button5.grid(row=2, column=0, sticky="nsew")
button6.grid(row=2, column=1, sticky="nsew")

# Make buttons expand to fill the available space
for i in range(3):
    root.rowconfigure(i, weight=1)


root.mainloop()




#=============================================================================================================================================   


