CREATE TABLE PUBLISHER
(
    Publisher_Name  VARCHAR(30)     NOT NULL,
    Phone           CHAR(12),
    Address         VARCHAR(60),

    PRIMARY KEY (Publisher_Name)
);

CREATE TABLE LIBRARY_BRANCH
(
    Branch_Id       INT             AUTO_INCREMENT,
    Branch_Name     VARCHAR(30)     NOT NULL,
    Branch_Address  VARCHAR(60)     NOT NULL,

    PRIMARY KEY (Branch_Id)
);

CREATE TABLE BORROWER
(
    Card_No         INT             AUTO_INCREMENT,
    Name            VARCHAR(30)     NOT NULL,
    Address         VARCHAR(60)     NOT NULL,
    Phone           CHAR(12)        NOT NULL,

    PRIMARY KEY (Card_No)
);

CREATE TABLE BOOK
(
    Book_Id         INT             AUTO_INCREMENT,
    Title           VARCHAR(50)     NOT NULL,
    Publisher_Name  VARCHAR(30)     NOT NULL,

    PRIMARY KEY (Book_Id),
    FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER (Publisher_Name)
    ON UPDATE CASCADE
);

CREATE TABLE BOOK_LOANS
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
);

CREATE TABLE BOOK_COPIES
(
    Book_Id         INT             NOT NULL,
    Branch_Id       INT             NOT NULL,
    No_Of_Copies    INT             NOT NULL,

    PRIMARY KEY (Book_Id, Branch_Id),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id),
    FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE Table BOOK_AUTHORS
(
    Book_Id         INT             NOT NULL,
    Author_Name     VARCHAR(30)     NOT NULL,

    PRIMARY KEY (Book_Id, Author_Name),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
    ON DELETE CASCADE ON UPDATE CASCADE
);






