from bottle import Bottle,template,request

app=Bottle()

@app.route('/')
def index():
    return template("template.html",message="please enter something")

@app.route('/',method="POST")
def formhandler():
    name=request.forms.__get__("name")
    message="hello"+name
    return template("template.html",message=message)