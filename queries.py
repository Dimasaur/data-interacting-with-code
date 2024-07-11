# pylint: disable=missing-docstring, C0103

import sqlite3


def directors_count(db):
    query = """
    SELECT count(id)
    FROM directors d
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()[0][0]
    print(type(results))

    return results


def directors_list(db):
    query = """
    SELECT name
    FROM directors d
    ORDER BY name ASC
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute(query)
    temp = db.fetchall()
    results = []
    for i in temp:
        results.append(i[0])
    print(results)

    return results

def love_movies(db):
    query = """
    SELECT title
    FROM movies m
    WHERE
	LOWER(title) like "% love %"
	or LOWER(title) like "love %"
	or LOWER(title) like "% love"
	or LOWER(title) like "love"
	or LOWER(title) like "% love'%"
	or LOWER(title) like "% love."
	or LOWER(title) like "love,%"
	or LOWER(title) like " love'%"

    ORDER BY title ASC
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute(query)
    temp = db.fetchall()
    results = []
    for i in temp:
        results.append(i[0])
    return results


def directors_named_like_count(db, name):
    query = """
    SELECT COUNT(name)
    FROM directors d
    WHERE LOWER(name) LIKE ?
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute(query,(f"%{name.lower()}%",))
    results = db.fetchone()[0]
    print(results)
    return results

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = """
    SELECT title
    FROM movies m
    WHERE minutes > ?
    ORDER BY title ASC
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute(query,(min_length,))
    temp = db.fetchall()
    results = []
    for i in temp:
        results.append(i[0])
    print(results)
    return results
