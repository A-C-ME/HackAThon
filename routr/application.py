import os
import json
from flask import Flask, g, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import sqlite3
from algorithm import algo

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
route = []
items = {}
count = -1
length = 0
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    with sqlite3.connect("routr.db") as conn:
        c = conn.cursor()
        rows = c.execute('SELECT * FROM cart').fetchall()
        return render_template("index.html",rows=rows)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        if not request.form.get("item"):
            return apology("Error: Cart is Empty")
        else:
            with sqlite3.connect("routr.db") as conn:
                c = conn.cursor()
                print(request.form.get("item"))
                rows = c.execute('INSERT INTO "cart" ("name") VALUES (?)',[request.form.get("item")])
        return redirect("/")
    else:
        redirect("/")

@app.route("/empty", methods=["GET", "POST"])
def empty():
    with sqlite3.connect("routr.db") as conn:
        c = conn.cursor()
        c.execute('DELETE FROM cart;')
        return redirect("/")


@app.route("/route", methods=["GET", "POST"])
def route():
    with sqlite3.connect("routr.db") as conn:
        c = conn.cursor()
        rows = c.execute('SELECT * FROM cart').fetchall()
        if len(rows) < 1:
            return apology("Error, no items added")
        else:
            c = conn.cursor()
            stations = []
            rows = c.execute('SELECT DISTINCT "group" FROM cart c INNER JOIN items i on c.name=i.name').fetchall()
            for row in rows:
                stations.append(c.execute('SELECT "x","y","group" FROM groups WHERE "group" = ?',[row[0]]).fetchone())
            print(stations)
            start = c.execute('SELECT x,y FROM "groups" WHERE "group" = "start"').fetchone()
            checkout = c.execute('SELECT x,y FROM "groups" WHERE "group" = "checkout"').fetchone()
            route = algo(stations,[start[0],start[1],"start"],[checkout[0],checkout[1],"checkout"])
            route = [list(x) for x in route]
            print(route)
            global length
            length = len(route)
            items = {}
            rows = c.execute('SELECT c.name, "group" FROM cart c INNER JOIN items i on c.name = i.name').fetchall()
            for row in rows:
                if row[1] not in items:
                    items[row[1]] = [row[0]]
                else:
                    items[row[1]] = items[row[1]]
            print(items)
            global count
            if count < length:
                count = count + 1
            else:
                count = 0
            print(count)
            return render_template("router.html",route=route,items=items,count=count)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return 'ERROR'


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == '__main__':
    app.run(debug=True)
