from flask import Flask,render_template,request
from calculator import Calculator

app = Flask(__name__)

@app.route("/calculate", methods=['POST','GET'])
def web_calculate():
    c = Calculator()
    result = ''
    if request.method=='POST' and 'expression' in request.form:
        expression = str(request.form.get('expression'))
        result = c.calculate(expression)
    return render_template("index.html",result=result)