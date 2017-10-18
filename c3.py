
m datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class Movie(db.Entity):
    id = PrimaryKey(int, auto=True)
    genre = Required('Genre')
    age_rating = Required('Age_rating')
    dvds = Set('Dvd')
    name = Optional(str)
    length = Optional(int)
    description = Optional(str)
    poster = Optional(str)
    producer = Optional(str)
    year_of_realease = Optional(date)


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    firstname = Optional(str)
    lastname = Optional(str)
    email = Optional(str)
    address = Optional(LongStr)
    phone_number = Optional(str)
    family = Optional(str)
    blacklisted = Optional(bool)
    cust_dvds = Set('Cust_dvd')


class Shelf(db.Entity):
    id = PrimaryKey(int, auto=True)
    dvds = Set('Dvd')
    racks = Optional(int)
    max_capacity = Optional(int)


class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    movies = Set(Movie)
    name = Optional(str)
    description = Optional(str)


class Age_rating(db.Entity):
    id = PrimaryKey(int, auto=True)
    movies = Set(Movie)
    min_age = Optional(int)
    name = Optional(str)


class Dvd(db.Entity):
    id = PrimaryKey(int, auto=True)
    movie = Required(Movie)
    shelf = Required(Shelf)
    cust_dvds = Set('Cust_dvd')


class Cust_dvd(db.Entity):
    customers = Required(Customer)
    dvds = Required(Dvd)
    date_in = Optional(datetime)
    date_out = Optional(datetime)
    lent_out = Optional(bool)
    PrimaryKey(customers, dvds)



db.generate_mapping()
