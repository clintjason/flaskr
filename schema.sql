drop table if exists entries;
create table entries (
id integer primary key autoincrement,
title text not null,
'text' text not null
);

/*
drop table if exits users;
create table users (
	id integer primary key autoincrement,
	username text not null,
	email text not null,
	encrypted_password text not null
);
*/