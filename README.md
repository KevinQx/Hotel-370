# How to get set up:
1. download the following if you don't already have it:
  - ```python3```, this will install ```pip``` (python package manager) as well
  - git
2. once git is installed you can, from the command line (```cmd``` on windows, ```terminal``` on mac), cd into your preferred location and run ```git clone https://github.com/Hotels-Website/Hotel-370.git``` to download this repository into that folder.
3. to run the app, cd into the just cloned repository and run ```python app.py```
4. if you run into an error such as ```ModuleNotFoundError: No module named 'flask'``` or something similar, run "pip install flask" of whichever module was mentioned to install the required library
5. When the app is successfully running, a local server is started.  You should see this...

```
(hotelRes) C:\Users\Joseph\Desktop\HotelRes>python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 841-872-074
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

--------------------------------------------------
the important files to look at are app.py, queries.py and templates/ 



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
