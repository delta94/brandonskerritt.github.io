---
title: "SQLite guide in Python"
categories:
  - Maths
---

I got annoyed that there were either guides on standalone sqlite or not-so-good guides on sqlite in Python, so I decided to make a guide on sqlite in python. In this guide, we will be making a ToDo list database in order to teach Sqlite fundamentals.

# What is Sqlite?
Sqlite is a databasing standalone library which does not need to be configured before use. It has many advantages, stated here
* Does not require a seperate server to operate
* Does not need to be configured prior to use
* Very small and lightweight
* Supports most of the query language features from SQL
* Is available on all platforms and in most languages

# Diving right in

## Setting up

Our ToDo list app will have 4 columns in a single table

id | task | dateDue | dateAdded
--- | --- | --- | ---

and will look roughly like the above table. So first step is to create a database. But before that, we need to open a connection to the SQLite database.

```Python
import sqlite3
conn = sqlite3.connect("todo.db")
c = conn.cursor()
```

Now thankfully the file doesn't have to exist, if it doesn't exist SQlite will make the file. Since in this app I will be using more than just one databse object. I decided to make a database controller class and create a new object for every database we make, since I plan on making more than one database.

```Python
class Database_controller():
	def __init__(self, table_name):
		self.cursor = db.cursor()
		self.db = db
```

So using this new class, we can _instanstiate_ an object which contains the cursor and the database for the database we have chosen.

So in our example, we can just write

```Python
import sqlite3
database_handler_todo = Database_controller("todo.db")
```
and it'll allow us to control the database using an object.

I wanted to make the database controller into an object because this program is a part of a larger program and may have multiple databases open, so it was best to really differentiate the databases like this.

The next step is to create the table we defined above.
```Python
def ToDo_create():
	db_handler = Database_controller("todo.db")
	db_handler.cursor.execute("""CREATE TABLE
		todo(id INTEGER PRIMARY KEY, task TEXT,
		datetime TEXT, addedWhen TEXT)""")
    db_handler.db.commit()
```

This causes a slight problem. What if we call the create table function again? It'll error. People online have suggested using a try and except loop or seeing if the table already exists, but there's an easier way.
```Python
def ToDo_create():
	db_handler = Database_controller("todo.db")
	db_handler.cursor.execute("""CREATE TABLE IF NOT EXISTS
		todo(id INTEGER PRIMARY KEY, task TEXT,
		dateDue TEXT, dateAdded TEXT)""")
    db_handler.db.commit()
```

The "IF NOT EXISTS" part is very useful to us, since if the table does exist it doesn't recreate it. It only creates the table if it doesn't exist. Also, id is a primary key.

A primary key is a unique identifier for each _record_ in a table. A record is simply a row of data, one data object. We need to be able to identify each row uniquely, so we use a primary key. The primary key is auto-incremental, so we don't need to increment it ourselves. Also, no 2 records in the table can have the same id. Sqlite does this for us, so we don't need to worry.

Also notice how we execute commands using the cursor. Everytime we want to 'save' the database, we need to commit it using db.commit().

Most SQL commands are written in capital letters. 

Our next step is to add data to our database.
``` Python
def ToDo_add(tuple):
	# Adds new entry to todo table.
	from datetime import datetime
	task = tuple[0]
	dateCreated = tuple[2]
	db_handler.cursor.execute("""INSERT INTO todo(task, datetime, addedWhen) VALUES (?, ?, ?)""", (task, datetime1, (datetime.now())))
	db_handler.db.commit()
```

So ToDo_add receives a tuple in the format (taskName, taskConfidence, dateCreated). taskConfidence is ignored as this application is using natural language processing, however we won't delve into that here.

We take the values out of the tuples and execute an INSERT into statement.

The next step is to create a view table function. This function will be able to view the table and present it in a neat manner for the user.

We can start of with
```Python
db_handler.cursor.execute("""SELECT * FROM todo""")
```
but this isn't presented so well. Let's say we have some data in our database already, when we execute this query we get

```Python
[(1, 'say goodnight to my dog', '1513857600.0', '2017-12-20 18:59:19.307472'), (2, 'watch Amelie', '1513857600.0', '2017-12-20 18:59:26.187179')]
```
Which isn't very human readable.
There is a Python in library design to print things in a pretty way, let's try that

```Python
def ToDo_view():
	from pprint import pprint
	db_handler = Database_controller("todo.db")
	db_handler.cursor.execute("""SELECT * FROM todo""")
	values = db_handler.cursor.fetchall()
	pprint(values)
```

Results in

```Python
[(1, 'say goodnight to my dog', '1513857600.0', '2017-12-20 18:59:19.307472'),
 (2, 'watch Amelie', '1513857600.0', '2017-12-20 18:59:26.187179')]
 ```

Hmm. That wasn't any better. We can execute a better query, but I want to perform some maths. I want the added\_when function to display the _age_ of a task and the datetime to be human readable. Since we get a list of tuples, we can simply just access each item in it.

Firstly, I want the name of each column. We can hardcode this in, or we can use a list comprehension.

```Python
names = [description[0] for description db_handler.cursor.description]
```

This results in

```
['id', 'task', 'datetime', 'addedWhen']
```

Now I want the screen to look a little pretty...

```Python
print("id\ttask\tdue\tage")
print("-"*10)
```
Okay, now the hard part. We'll try this out first.

```Python
for i in values:
	print(str(i[0] + "\t" + str(i[1]) + "\t"))
```

```Python
id      task    due     age
----------
1       say goodnight to my dog
2       watch Amelie
```

Okay, that's better! 

Okay, slight change. The code is now

```Python
def ToDo_view():
	from pprint import pprint
	db_handler = Database_controller("todo.db")
	db_handler.cursor.execute("""SELECT * FROM todo""")
	values = db_handler.cursor.fetchall()
	# names is every single column name
	names = [description[0] for description in db_handler.cursor.description]

	# gets a list of all tasks
	list_of_tasks = []
	for i in values:
		list_of_tasks.append(i[1])

	longest_task = (len(max(list_of_tasks, key=len)) - 4)
	# gets the length of the longest task - a tab length
	spaces = (" " * longest_task)
	# gets how many spaces the longest task is
	print("id\ttask{}due\tage".format(spaces))
	# formarts it so the due column isn't direclty over the longest task
	print("-"*10)

	for i in values:
		# prints the values of things
		print(str(i[0]) + " " + str(i[1]) + "\t")
```






