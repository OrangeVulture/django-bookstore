CREATE DATABASE django_db3;
USE django_db3;

DROP TABLE book;

CREATE TABLE book (
	ISBN13 CHAR(14) NOT NULL UNIQUE PRIMARY KEY,
    ISBN10 CHAR(10) NOT NULL UNIQUE,
    title VARCHAR(256) NOT NULL,
    author VARCHAR(256), 
    publisher VARCHAR(256),
    years INT NOT NULL,
    num_copies INT NOT NULL, CHECK(num_copies>=0),
    price REAL NOT NULL, CHECK(price>=0), 
    book_format CHAR(9)  NOT NULL, 
    CHECK(format = 'paperback' OR format='hardcover'), 
    keyword VARCHAR(256), 
    book_subject VARCHAR(256)); 
    
CREATE TABLE customer (
	login_name VARCHAR(256) PRIMARY KEY,
    fullname VARCHAR(256) NOT NULL, 
    login_password VARCHAR(256) NOT NULL,
    credit_card VARCHAR(16) NOT NULL, CHECK( LEN(credit_card)=16), 
    address VARCHAR(256) NOT NULL, 
    phone_num INT NOT NULL); 
    
CREATE TABLE orders (
	login_name VARCHAR(256),
    ISBN13 CHAR(14),
    num_order INT, CHECK(num_order>0),
    order_date DATE NOT NULL, 
    order_status VARCHAR(256) NOT NULL,  
    PRIMARY KEY (login_name,ISBN13),
    FOREIGN KEY (login_name) REFERENCES customer(login_name),
    FOREIGN KEY (ISBN13) REFERENCES book(ISBN13));
    
CREATE TABLE shoppingcart (
	login_name VARCHAR(256),
    ISBN13 CHAR(14),
    num_order INT, CHECK(num_order>0),
    order_date DATE,
    PRIMARY KEY (login_name,ISBN13),
    FOREIGN KEY (login_name) REFERENCES customer(login_name),
    FOREIGN KEY (ISBN13) REFERENCES book(ISBN13));    

CREATE TABLE review(
	login_name VARCHAR(256),
    ISBN13 CHAR(14),
    review_score INT, CHECK (review_score>=0 AND review_score<=10),
    review_text VARCHAR(256),
    review_date DATE,
    PRIMARY KEY( login_name, ISBN13),
    FOREIGN KEY (login_name) REFERENCES customer(login_name),
    FOREIGN KEY (ISBN13) REFERENCES book(ISBN13));
      

CREATE TABLE rate(
	rater VARCHAR(256)  NOT NULL,
    rated VARCHAR(256)  NOT NULL,
    rating INT  NOT NULL, CHECK (rating <=10 AND rating >=1),
    ISBN13 CHAR(14) NOT NULL,
    PRIMARY KEY ( rater, rated, ISBN13),
    FOREIGN KEY (rater) REFERENCES customer(login_name),
    FOREIGN KEY (rated, ISBN13) REFERENCES review(login_name, ISBN13));    
