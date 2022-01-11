from flask import Flask,render_template,request
from calculator import Calculator

app = Flask(__name__)

@app.route("/calculate", methods=['POST','GET'])
def web_calculate():
    c = Calculator()
    result = ''
    status = ''
    error_message = ''
    if request.method=='POST' and 'expression' in request.form:
        expression = str(request.form.get('expression'))
        # result = c.calculate(expression)
        # import pdb;pdb.set_trace()
        try:
            result = c.calculate(expression)
            status = "OK"
            return render_template("index.html",result=result, status=status)
        except Exception as errors:
            status='ERROR'
            error_message = errors
            return render_template("index.html",error_message=error_message, status=status)