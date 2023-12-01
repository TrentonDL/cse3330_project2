-- Task 1 Queries

-- Query 1: Add an extra column ‘Late’ to the Book_Loan table. Values will be 0-for non-late retuns, and 1-for late
-- returns. Then update the ‘Late’ column with '1' for all records that they have a return date later than the
-- due date and with '0' for those were returned on time.

ALTER TABLE BOOK_LOANS 
ADD Late INT DEFAULT '0' NOT NULL; 

UPDATE 		BOOK_LOANS
SET 		Late = '1'
WHERE 		DATEDIFF(Returned_date, Due_Date) > 1;

-- Query 2: Add an extra column ‘LateFee’ to the Library_Branch table, decide late fee per day for each branch and
-- update that column.

ALTER TABLE LIBRARY_BRANCH
ADD LateFee INT DEFAULT '5' NOT NULL;

UPDATE		LIBRARY_BRANCH
SET			LateFee = '20'
WHERE		Branch_id = '1';

UPDATE		LIBRARY_BRANCH
SET			LateFee = '15'
WHERE		Branch_id = '2';

UPDATE		LIBRARY_BRANCH
SET			LateFee = '12'
WHERE		Branch_id = '3';

UPDATE		LIBRARY_BRANCH
SET			LateFee = '10'
WHERE		Branch_id = '4';

UPDATE		LIBRARY_BRANCH
SET			LateFee = '2'
WHERE		Branch_id = '5';


-- Query 3: Create a view vBookLoanInfo that retrieves all information per book loan. The view should have the
-- following attributes:

-- • Card_No,
-- • Borrower Name
-- • Date_Out,
-- • Due_Date,
-- • Returned_date
-- • Total Days of book loaned out as 'TotalDays'– you need to change weeks to days
-- • Book Title
-- • Number of days returned late – if returned before or on due_date place zero
-- • Branch ID
-- • Total Late Fee Balance 'LateFeeBalance' – If the book was not retuned late than fee = ‘0’

CREATE VIEW 	vBookLoanInfo AS
SELECT			B.Card_No, B.Name, BL.Date_Out, BL.Due_Date, BL.Returned_date, DATEDIFF(BL.Returned_date, BL.Date_Out) AS TotalDays,
			    
			    CASE
			        WHEN DATEDIFF(BL.Returned_date, BL.Due_Date) > 0 THEN
			            DATEDIFF(BL.Returned_date, BL.Due_Date)
			        ELSE
			            0  -- Set DaysLate to 0 if the book is not returned late
			    END AS DaysLate, BL.Branch_id,

			    CASE
			        WHEN DATEDIFF(BL.Returned_date, BL.Due_Date) > 0 THEN
			            (DATEDIFF(BL.Returned_date, BL.Due_Date)) * LB.LateFee
			        ELSE
			            0  -- No late fee if the book is not returned late
			    END AS LateFeeBalance
			    
FROM			BORROWER AS B
JOIN 			BOOK_LOANS AS BL ON B.Card_No = BL.Card_No 
JOIN 			LIBRARY_BRANCH AS LB ON LB.Branch_id = BL.Branch_id;
































