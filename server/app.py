#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:inp>')
def print_string(inp):
    print(inp)
    return f'{inp}'

@app.route('/count/<int:c>')
def count(c):
    #c, c-1, c-2, until c-x=0
    ret = ""
    for a in range(0, c):
        ret = f'{ret}{a}\n'
        print(a)
    return ret
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if (operation == '+'):
        return f'{num1+num2}'
    elif (operation == '-'):
        return f'{num1-num2}'
    elif (operation == '*'):
        return f'{num1*num2}'
    elif (operation == '%'):
        return f'{num1%num2}'
    else:
        return f'{num1/num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
