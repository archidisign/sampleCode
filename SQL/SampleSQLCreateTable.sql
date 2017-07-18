CREATE TABLE	Borrower (
	bid			REAL	PRIMARY KEY,
	bname		VARCHAR(40) NOT NULL,
	baddress	VARCHAR(60) NOT NULL
);

CREATE TABLE	Lender (
	lid			REAL	PRIMARY KEY,
	lname		VARCHAR(40) NOT NULL,
	laddress	VARCHAR(60) NOT NULL
);

CREATE TABLE	Evaluate (
	bid			REAL	FOREIGN KEY REFERENCES Borrower(bid) ON UPDATE CASCADE ON DELETE CASCADE,
	lid			REAL	FOREIGN KEY REFERENCES Lender(lid) ON UPDATE CASCADE ON DELETE CASCADE,
	trustValue	REAL,
	CONSTRAINT check_trustValue CHECK (trustValue >= 0 AND trustValue <= 100),
	PRIMARY KEY (bid, lid)
);

CREATE TABLE	LoanRequest (
	bid				REAL NOT NULL 	FOREIGN KEY REFERENCES Borrower(bid) ON UPDATE CASCADE ON DELETE NO ACTION,
	lrdate			DATE,
	lrdesc			VARCHAR(100),
	grantDate		DATE NOT NULL,	
	lramount		REAL NOT NULL,
	paymentPeriod	REAL NOT NULL,
	PRIMARY KEY(bid, lrdate),
	/* CHECK (paymentPeriod > grantDate) Should period be a date, also why the comparison?*/
);

CREATE TABLE	Intermediary (
	iid			REAL	PRIMARY KEY,
	iname		VARCHAR(40) NOT NULL,
	iaddress	VARCHAR(60) NOT NULL
);

CREATE TABLE	Loan (
	loanid		REAL	PRIMARY KEY,
	loandate	DATE 	NOT NULL,
	bid			REAL,
	lrdate		DATE,
	iid 		REAL NOT NULL FOREIGN KEY REFERENCES  Intermediary(iid) ON UPDATE CASCADE ON DELETE NO ACTION,
	CONSTRAINT Loan_foreign FOREIGN KEY (bid, lrdate) REFERENCES LoanRequest(bid, lrdate) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT Loan_constraint CHECK (loandate > lrdate)
);

CREATE TABLE	Payment (
	loanid	REAL NOT NULL FOREIGN KEY REFERENCES Loan(loanid) ON UPDATE CASCADE ON DELETE CASCADE,
	pdate	DATE,
	pamount	REAL NOT NULL,
	PRIMARY KEY(loanid, pdate)
);

CREATE TABLE	Deadline (
	loanid	REAL NOT NULL FOREIGN KEY REFERENCES Loan(loanid) ON UPDATE CASCADE ON DELETE CASCADE,
	ddate	DATE
	PRIMARY KEY(loanid, ddate)
);

CREATE TABLE	Share (
	loanid	REAL,
	pdate	DATE,
	lid		REAL NOT NULL FOREIGN KEY REFERENCES Lender(lid) ON UPDATE CASCADE	ON DELETE NO ACTION,
	CONSTRAINT Share_foreign FOREIGN KEY (loanid, pdate) REFERENCES Payment(loanid, pdate) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(loanid, pdate, lid)
);

CREATE TABLE	Commitment (
	bid		REAL,
	lrdate	DATE,
	lid		REAL NOT NULL FOREIGN KEY REFERENCES Lender(lid) ON UPDATE CASCADE ON DELETE NO ACTION,
	camount	REAL NOT NULL,
	CONSTRAINT Commit_foreign FOREIGN KEY (bid, lrdate) REFERENCES LoanRequest(bid, lrdate) ON UPDATE CASCADE ON DELETE NO ACTION,
	PRIMARY KEY(bid, lrdate, lid)
);
