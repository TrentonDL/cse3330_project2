CREATE TABLE PUBLISHER
(
    Publisher_Name  VARCHAR(30)     NOT NULL,
    Phone           CHAR(12),
    Address         VARCHAR(60),

    PRIMARY KEY (Publisher_Name)
);

CREATE TABLE LIBRARY_BRANCH
(
    Branch_Id       INTEGER         PRIMARY KEY        AUTOINCREMENT,
    Branch_Name     VARCHAR(30)     NOT NULL,
    Branch_Address  VARCHAR(60)     NOT NULL
);

CREATE TABLE BORROWER
(
    Card_No         INTEGER         PRIMARY KEY        AUTOINCREMENT,
    Name            VARCHAR(30)     NOT NULL,
    Address         VARCHAR(60)     NOT NULL,
    Phone           CHAR(12)        NOT NULL
);

CREATE TABLE BOOK
(
    Book_Id         INTEGER         PRIMARY KEY        AUTOINCREMENT,
    Title           VARCHAR(50)     NOT NULL,
    Publisher_Name  VARCHAR(30)     NOT NULL,

    FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER (Publisher_Name)
    ON UPDATE CASCADE
);

CREATE TABLE BOOK_LOANS
(
    Book_Id         INTEGER         NOT NULL,
    Branch_Id       INTEGER         NOT NULL,
    Card_No         INTEGER         NOT NULL,
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
);

CREATE TABLE BOOK_COPIES
(
    Book_Id         INTEGER         NOT NULL,
    Branch_Id       INTEGER         NOT NULL,
    No_Of_Copies    INTEGER         NOT NULL,

    PRIMARY KEY (Book_Id, Branch_Id),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id),
    FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE Table BOOK_AUTHORS
(
    Book_Id         INTEGER         NOT NULL,
    Author_Name     VARCHAR(30)     NOT NULL,

    PRIMARY KEY (Book_Id, Author_Name),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
    ON DELETE CASCADE ON UPDATE CASCADE
);





