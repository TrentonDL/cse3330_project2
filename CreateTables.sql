CREATE TABLE PUBLISHER
(
    Publisher_Name  VARCHAR(30)     NOT NULL,
    Phone           CHAR(10),
    Address         VARCHAR(50),

    PRIMARY KEY (Publisher_Name)
);

CREATE TABLE LIBRARY_BRANCH
(
    Branch_Id       INT             NOT NULL,
    Branch_Name     VARCHAR(10),
    Branch_Address  VARCHAR(50),

    PRIMARY KEY (Branch_Id)
);

CREATE TABLE BORROWER
(
    Card_No         CHAR(6)         NOT NULL,
    Name            CHAR(20)        NOT NULL,
    Phone           CHAR(10)        NOT NULL,

    PRIMARY KEY (Card_No)
);

CREATE TABLE BOOK
(
    Book_Id         INT             NOT NULL,
    Title           VARCHAR(10)     NOT NULL,
    Publisher_Name  VARCHAR(30)     NOT NULL,

    PRIMARY KEY (Book_Id)
)

CREATE TABLE BOOK_LOANS
(
    Book_Id         INT             NOT NULL,
    Branch_Id       INT             NOT NULL,
    Card_No         CHAR(6)         NOT NULL,
    Date_Out        CHAR(8),
    Date_In         CHAR(8),
    Returned_date   CHAR(8),

    PRIMARY KEY (Book_Id, Branch_Id, Card_No),
    FOREIGN KEY (Book_Id, Branch_Id, Card_No)
);

CREATE TABLE BOOK_COPIES
(
    
);

CREATE Table BOOK_AUTHORS
(

);