import sqlite3

db = 'hotel.db'

def create_db_and_tables():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    '''
    Hotel - id, name
    Location - id, hotel-id, name, i, j 
    Room - id, location-id, room-number, size, price, 
    CustomerAccount - id, first-name, last-name, DOB, username, password
    Reservation - id, start-date, end-date, room-id, cust-id
    Admin - id, username, password, hotel-id
    '''


    c.execute("""
        CREATE TABLE if not exists hotel(
            id integer primary key,
            name text not null unique
        )
    """)

    c.execute("""
        CREATE TABLE if not exists location(
            id integer primary key,
            hotelid integer not null,
            name text not null,
            i integer not null,
            j integer not null,
            foreign key(hotelid) references hotel(id),
            unique(i,j),
            check(i >= 0 and i <= 100 and j >= 0 and j <= 100)
        )
    """)

    c.execute("""
        CREATE TABLE if not exists room(
            id integer primary key,
            locationid integer not null,
            roomnumber integer not null,
            size integer,
            price real not null,
            foreign key(locationid) references location(id)
        )
    """)

    c.execute("""
        CREATE TABLE if not exists customer(
            id integer primary key,
            firstname text not null,
            lastname text not null,
            username text not null unique,
            password text not null
        )
    """)

    c.execute("""
        CREATE TABLE if not exists reservation(
            id integer primary key,
            startdate integer not null,
            enddate integer not null,
            roomid integer not null,
            custid integer not null,
            foreign key(roomid) references room(id),
            foreign key(custid) references customer(id)
        )
    """)

    c.execute("""
        CREATE TABLE if not exists admin(
            id integer primary key,
            username text not null,
            password text not null,
            hotelid integer not null,
            foreign key(hotelid) references hotel(id)
        )
    """)
    conn.commit()
    conn.close()

def insert_new_user(firstname, lastname, username, password):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"insert into customers values ({firstname},{lastname},{username},{password})")
    conn.commit()
    conn.close()

def insert_new_hotel(hotel):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"insert into customers values ({hotel})")
    conn.commit()
    conn.close()

def insert_new_admin(username, password, hotelid):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"insert into customers values ({username},{password},{hotelid})")
    conn.commit()
    conn.close()

def insert_new_location(hotel, name, i,j):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"insert into customers values ({hotel},{name},{i},{j})")
    conn.commit()
    conn.close()

def insert_new_rooms(rooms):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for locid, rn, size, price in rooms:
        c.execute(f"insert into customers values ({locid},{rn},{size},{price})")
    conn.commit()
    conn.close()




if __name__ == '__main__':
    create_db_and_tables()
    

