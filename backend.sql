create database restdb;
use restdb;
select * from delivery;
create table delivery (
	username varchar(20),
    address varchar(30),
    phonenumber bigint,
    reciept varchar(100),
    methodofpayment varchar(20),
    dateoforder varchar(14));

create table reservation (
	Name varchar(20),
    phoneno bigint,
    numberofseats int,
    seattype varchar(6),
    seatnumbers varchar(50),
    dayofarrival varchar(11),
    timeofarrival varchar(50));
