from flask import Flask, render_template, request
from config import host, user, password, database, auth_plugin
import mysql.connector

app = Flask(__name__)

dbconfig = {
    "host": host,
    "user": user,
    "password": password,
    "database": database,
    "auth_plugin": auth_plugin
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    u = request.headers.get("User-Agent")

    conn = mysql.connector.connect(pool_name="poolofagents",
                    pool_size=16,
                    **dbconfig)

    cursor = conn.cursor()

    for r in cursor.execute("SELECT * FROM Agents WHERE UA='%s'"%(u), multi=True):
        if r.with_rows:
            res = r.fetchall()
            conn.close()
            break

    if len(res) == 0:
        data = {'msg' : "stop! you're not allowed in here >:)",
                'denied': True}
        return render_template("login.html", data=data)

    if len(res) > 1:
        data = {'msg': "hey! close, but no bananananananananana!!!! (there are many secret agents of course)",
                'close': True}
        return render_template("login.html", data=data)

    data = {'msg': "Welcome, %s" % (res[0][1])}
    return render_template("login.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
