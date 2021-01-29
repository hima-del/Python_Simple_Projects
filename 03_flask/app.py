from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="Himaja"
app.config["MYSQL_PASSWORD"]="sravan@12345"
app.config["MYSQL_DB"]="mydb"

mysql=MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/name",methods=["POST"])
def my_form_post():
    text=request.form["name"]   
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO mytable(name)VALUES(%s)",(text,))
    mysql.connection.commit()
    cur.close()
    return render_template("index.html")

if __name__=="__main__":
    app.run()    