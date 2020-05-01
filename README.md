# HotelRes
Hotel Reservation App - CS370 Project 2b

Map
Customers
Hotels
Search Engine
Current Date

# Map
Don't need password to view map
Map - 0-100 grid, Location (i, j)

# Reservation Search Engine - Customer view
Search by
- Hotel
- Room size
- Price 
- Location

# My Reservations

# Customer Account
- login
- register

# Hotel Page
- Rooms - type
- rates
- availability

# Hotel Admin Account
- locations
- Add new location
- Who's checked in to which rooms

# Current date


import sqlite3

def create_db_and_tables():
    sqlite3.connect('game.db')
    c.execute("""

    
    
    """)










import sqlite3
from pprint import pprint

def getData():
    conn = sqlite3.connect('game.db')
    c = conn.cursor()

    # c.execute(""" CREATE TABLE players
    # (
    #     username text,
    #     password text,
    #     email text,
    #     highscore real
    # )
    # """)

    # c.execute("INSERT INTO players VALUES ('SSM','pass','iun@iun.com','78343.43')")

    c.execute('select * from players')
    # data = []
    # for username, password, email, highscore in c.fetchall():
    #     data.append({
    #         "username":username,
    #         "password":password,
    #         "email":email,
    #         "highscore":highscore
    #     })
    data = "||".join(["::".join((un, pw, str(hs))) for un, pw, email, hs in c.fetchall()])
    print(data)
    conn.commit()
    conn.close()
    return data

def insert(data):
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO players VALUES {data}")
    conn.commit()
    conn.close()

def scores():
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute('select distinct username, highscore from players order by highscore desc')
    data = "||".join(["::".join((a, str(b))) for a,b in c.fetchall()])
    print(data)
    conn.commit()
    conn.close()
    return data


def update(username, score):
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute(f"select distinct highscore from players where username = '{username}' ")
    if c.fetchone()[0] < float(score):
        # print(c.fetchone()[0] < score)
        c.execute(f"UPDATE players SET highscore = {score} WHERE username = '{username}'")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    getData()
    scores()
    update("JSM", 118)
