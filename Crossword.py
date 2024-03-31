import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Edinburgh23",
    database = "testdatabase"
)

mycursor = db.cursor()

data = [
    ["Gilks", 5],
    ["Jones", 5],
    ["Lowes", 5],
    ["Smith", 5],
    ["Isaac", 5],
    ["Troen", 5],
    ["Chase", 5],
    ["Fagan", 5],
    ["Irons", 5],
    ["Allon", 5],
    ["Druce", 5],
    ["Milne", 5],
    ["Byrne", 5],
    ["James", 5],
    ["Tofts", 5],
    ["Blake", 5],
    ["Roman", 5],
    ["Martin", 6],
    ["Squire", 6],
    ["Goldup", 6],
    ["Madden", 6],
    ["Baxter", 6],
    ["Cloete", 6],
    ["French", 6],
    ["Friend", 6],
    ["Hemery", 6],
    ["Lyster", 6],
    ["Cotton", 6],
    ["Davies", 6],
    ["Perrin", 6],
    ["Bourne", 6],
    ["Briers", 6],
    ["Lapage", 6],
    ["Larsen", 6],
    ["Tulley", 6],
    ["Twyman", 6],
    ["Jeffery", 7],
    ["Wishart", 7],
    ["Poynter", 7],
    ["Garnett", 7],
    ["Mahmoud", 7],
    ["Watkins", 7],
    ["Franjic", 7],
    ["Killick", 7],
    ["Shravat", 7],
    ["Larlham", 7],
    ["Schwank", 7],
    ["Tanzini", 7],
    ["Blurton", 7],
    ["Maguire", 7],
    ["Vickers", 7],
    ["Babaeva", 7],
    ["Pradera", 7],
    ["Milanova", 8],
    ["Wheatley", 8],
    ["Cereceda", 8],
    ["Charlton", 8],
    ["Fickling", 8],
    ["Mayfield", 8],
    ["Stoyanov", 8],
    ["Treleven", 8],
    ["Bertrand", 8],
    ["Lagoguey", 8],
    ["Harrison", 8],
    ["Thatcher", 8],
    ["Williams", 8]
]


"""
mycursor.execute("CREATE DATABASE Crossword")
mycursor.execute("CREATE TABLE Staff (Name varchar(50) PRIMARY KEY, Length int UNSIGNED)")
db.commit()


insert_query =
INSERT INTO Staff
(Name, Length)
VALUES (%s, %s)

for i in data:
    mycursor.execute(insert_query, i)

AND SUBSTRING(Name, 4, 1) = 'l'

"""

mycursor.execute("SELECT Name FROM Staff WHERE LENGTH(Name) = 7 AND SUBSTRING(Name, 6, 1) = 'l'")
readrecords = mycursor.fetchall()
print("Incoming records:")
for q in readrecords:
    print(q)
