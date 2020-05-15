# How to get set up:
1. download the following if you don't already have it:
  - ```python3```, this will install ```pip``` (python package manager) as well
  - git
2. once git is installed you can, from the command line (```cmd``` on windows, ```terminal``` on mac), cd into your preferred location and run ```git clone https://github.com/Hotels-Website/Hotel-370.git``` to download this repository into that folder.
3. run ```pip install -r requirements.txt``` to install the dependencies
4. to run the app, cd into the just cloned repository and type ```python app.py```
5. if you run into an error such as ```ModuleNotFoundError: No module named 'flask'``` or something similar, run "pip install flask" or whichever module was mentioned, to install the required library
6. When the app is successfully running, a local server is started.  You should see this...

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

7. type http://127.0.0.1:5000/ into your address bar to see the website on your local computer
8. flask has live reloading, so as you save changes the server reloads automatically.
9. bootstrap and jquery are already imported - you don't need to use either but you can.

--------------------------------------------------
the important files to look at are app.py, queries.py and templates/

# Technologies
1. git - version control - how we can all work together and not step on each others toes
2. flask - web framework (handles server routes and sessions, etc.) - https://flask.palletsprojects.com/en/1.1.x/quickstart/
3. sqlite3 - simple db that stores in a single file
4. bootstrap (css framework) - https://getbootstrap.com/docs/4.4/getting-started/introduction/ - makes css way easier to use imho.
5. html, css, javascript
6. jinja - if you see code that looks like ```{% something %}``` in the html files, this is jinja.  it's used by flask to pass data to the html files before they get rendered. 
7. XMLHttpRequest - A way of sending asyncronous http requests from javascript
8. python Decorators - you will see ```@something``` above some functions in the python code - https://book.pythontips.com/en/latest/decorators.html - these essentially wrap the following function with some other code. They "decorate" the function, so to speak.  

```
def my-decorator(func):
  def decorated_function():
    print("some code before")
    func()
    print("some code after")
  return decorated_function
  
  
@my-decorator
def hello_world():
  print("hello world")
  
>>> hello_world()
Some code before
hello world
some code after

```

The live website is here https://protected-falls-95338.herokuapp.com/

------------------------------------------------------------------------

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


#git commands

mkdir
cd
cls
git init //you souldnt need this
git status
git add
git branch // to view branches
git checkout -b [newbranchname] // create and enter new branch





step1 - download git and install
step2 - go to github and click on "clone or download"
step3 - copy link
step4 - go to folder (cd) you want to host the repo within 
step5 - "git clone http://(the link)
step6 - create a new branch for yourself - "git checkout -b sean"
step7 - make your changes 
= "git add filename" or "git add ." then git commit -m "your message" 
step8 - git push
step9 - if your branch doesn't exist on github, you will be prompted to type
        git push --set-upstream origin "nameofyourbranch"