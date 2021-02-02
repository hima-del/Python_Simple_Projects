from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
from flask import jsonify
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
    response=jsonify("value added successfully")
    return response

@app.route("/name",methods=["GET"])
def my_form_get():
    sql_select_Query="SELECT * FROM mytable"
    cur=mysql.connection.cursor()
    cur.execute(sql_select_Query)
    data=cur.fetchall()
    print("data",data)
    for row in data:
        print(row[0])  
    response=jsonify(data)             
    return response

if __name__=="__main__":
    app.run()    