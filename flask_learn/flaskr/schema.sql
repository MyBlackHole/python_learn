drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title string not null,
	text string not null
);
select title,text from entries order by id desc
