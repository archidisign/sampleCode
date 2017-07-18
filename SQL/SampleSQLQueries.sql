/*1) Find all borrowers whose loan outstanding amount is greater than $10,000.*/

SELECT t3.bid FROM
(SELECT t2.bid, sumL, sumP FROM
(SELECT Loan.bid AS bid, sum(lramount) AS sumL FROM Loan, LoanRequest WHERE Loan.bid=LoanRequest.bid AND Loan.lrdate=LoanRequest.lrdate group by Loan.bid) t1
INNER JOIN
(SELECT Loan.bid AS bid, sum(pamount) AS sumP FROM Loan, Payment WHERE Loan.LoanID=Payment.LoanID GROUP BY Loan.bid) t2
ON t1.bid=t2.bid
) t3 WHERE 10000 <= (sumL-sumP);

/*2) Find the borrower(s) and their relevant loan request(s) who have failed to repay the loan before the agreed upon deadline maximum number of times.*/

SELECT t5.bid, t5.lrdate FROM
(SELECT t2.bid, t3.lrdate, sumL, sumP, countDeadline FROM
(SELECT Loan.bid AS bid, sum(lramount) AS sumL FROM Loan, LoanRequest WHERE Loan.bid=LoanRequest.bid AND Loan.lrdate=LoanRequest.lrdate group by Loan.bid) t1
INNER JOIN
(SELECT Loan.bid AS bid, sum(pamount) AS sumP FROM Loan, Payment WHERE Loan.LoanID=Payment.LoanID GROUP BY Loan.bid) t2
ON t1.bid=t2.bid
INNER JOIN
(SELECT Loan.bid as bid, Loan.loanid as loanid, LoanRequest.lrdate FROM Loan, LoanRequest WHERE loanRequest.bid=loan.bid) t3
ON t1.bid=t3.bid
INNER JOIN
(SELECT count(*) as countDeadline, Deadline.loanid as loanid FROM Deadline GROUP BY loanID) t4
on t3.loanID=t4.loanID
) t5 WHERE 0 < (sumL-sumP) AND countDeadline>10; --note that here, the max deadline was defaulted as 10


/*3) Find the most “distrustful” borrower for each lender and retrieve the relevant loan details to justify the reasons for their distrustfulness.*/

SELECT t1.lid, t1.bid, t1.WorstScore, t1.loanID, (sumL-sumP) as sumOwned FROM
(SELECT DISTINCT t0.lid as lid, Evaluate.bid as bid, WorstScore, Loan.loanID as loanID FROM
Evaluate, Share, Loan, (SELECT lid, min(trustValue) as WorstScore FROM Evaluate Group by lid) t0
WHERE Evaluate.bid=Loan.bid AND Evaluate.lid=Share.lid AND Share.loanID=Loan.loanID and Evaluate.trustValue=t0.WorstScore) t1
INNER JOIN
(SELECT Loan.bid AS bid, sum(lramount) AS sumL FROM Loan, LoanRequest WHERE Loan.bid=LoanRequest.bid AND Loan.lrdate=LoanRequest.lrdate group by Loan.bid) t2
ON t1.bid=t2.bid
INNER JOIN
(SELECT Loan.bid AS bid, sum(pamount) AS sumP FROM Loan, Payment WHERE Loan.LoanID=Payment.LoanID GROUP BY Loan.bid) t3
ON t2.bid=t3.bid;


/*4) For each borrower, list the details of loan requests that are eventually cancelled.*/

SELECT LoanRequest.bid, LoanRequest.lrdate, lrdesc, grantDate, lramount, paymentPeriod
FROM LoanRequest
LEFT JOIN Loan
ON LoanRequest.bid=Loan.bid AND LoanRequest.lrdate=Loan.lrdate
WHERE Loan.bid IS NULL;

/*5) Find all lenders who have committed to least number of loan requests during a given time period.*/

SELECT TOP 1 nbrCommit, t1.lid
FROM Commitment, (SELECT lid, COUNT(*) AS nbrCommit FROM Commitment GROUP BY lid) t1
WHERE lrdate BETWEEN '2017-01-01' AND '2017-05-01' AND Commitment.lid=t1.lid
ORDER BY nbrCommit ASC;

/*6) Write an SQL command, which deletes all information on ended loans, which is to say loans WHERE the total repaid amount equals the lend amount.*/
DELETE FROM LOAN
WHERE bid=
(SELECT t3.bid FROM
(SELECT t2.bid as bid, sumL, sumP FROM
(SELECT Loan.bid AS bid, sum(lramount) AS sumL FROM Loan, LoanRequest WHERE Loan.bid=LoanRequest.bid AND Loan.lrdate=LoanRequest.lrdate group by Loan.bid) t1
INNER JOIN
(SELECT Loan.bid AS bid, sum(pamount) AS sumP FROM Loan, Payment WHERE Loan.LoanID=Payment.LoanID GROUP BY Loan.bid) t2
ON t1.bid=t2.bid) t3 WHERE sumL = sumP);
