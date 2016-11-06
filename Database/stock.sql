CREATE DATABASE stocks;

USE stocks;

/*  */
CREATE TABLE USER_BASIC_INFO (
	userID integer,
	firstName varchar(200),
	lastName varchar(200),
 	age integer,
	phoneNumber varchar(200),
	password varchar(200),
	email varchar(200),
	/* requstedStock varchar(200), */
	primary key(userID)
);

/* */
CREATE TABLE STOCK_WATCH_LIST (
	stockID integer,
	trend integer,
	amountSold integer, /* */
	userID integer,
	primary key(userID, stockID),
	foreign key(userID) references USER_BASIC_INFO(userID)
);

/* */
CREATE TABLE USER_STOCK_SELECTION (
	userID integer,
	stockID integer,
	dateOfPurchase varchar(200),
	numOfStocksPurchased integer,
	stockPrice integer,
	stockSalePrice integer,
	portionSold integer,
	primary key(userID, stockID),
	foreign key(userID) references USER_BASIC_INFO(userID)
);

CREATE TABLE STOCK_STATIC_INFO (
	stockID integer,
	stockName varchar(200),
	dateOfInitiation varchar(200),
	basicPrice varchar(200),
	primary key(stockID)	
);

CREATE TABLE STOCK_DYNAMIC_INFO (
	stockID integer,
	time_stamp varchar(200),
	stockPrice integer,
	primary key(stockID, time_stamp),
	foreign key(stockID) references STOCK_STATIC_INFO(stockID)
);

CREATE TABLE PREDICTION_INFO (
	stockID integer,
	predictionDate varchar(200),
	predictionValue integer,
	predictionTrend integer,
	primary key(stockID, predictionDate),
	foreign key(stockID) references STOCK_STATIC_INFO(stockID)
);


CREATE TABLE ML_ALGORITHMS (
	algorithmID integer,
	algorithmName varchar(200),
	usageComments varchar(200),
	primary key(algorithmID)
);


CREATE TABLE ML_STOCK (
	stockID integer,
	algorithmID integer,
	trainedClassifier varchar(1000),
	primary key(stockID),
	foreign key(algorithmID) references ML_ALGORITHMS(algorithmID)
);


CREATE TABLE RAW_STOCKS_DATA (
	stockID integer,
	rawDate date,
	high float(10),
	low float(10),
	volume float(10),
	exDividend float(10),
	splitRatio float(10),
	adjOpen float(10),
	adjHigh float(10),
	adjLow float(10),
	adjClose float(10),
	adjVolume float(10),
	primary key(stockID, rawDate),
	foreign key(stockID) references ML_STOCK(stockID)
);

CREATE TABLE TWITTER_FEEDS (
	tweetDate varchar(200),
	issuer varchar(200),
	stockID integer, /*Assuming that a tweet only has information about 1 stock*/
	tweetText varchar(140),
	tweetID varchar(200),
	foreign key(stockID) references STOCK_STATIC_INFO(stockID),
	primary key(tweetID)
);
