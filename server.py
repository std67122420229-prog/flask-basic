from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def home():
  return f'''

  <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Flask Basic</title>
    </head>
    <body>
      <h1>Home Page</h1>
      <hr>
    </body>
    </html>
'''

# @app.route('/calculator/addition/<int:num1>/<int:num2>')
# def addition(num1, num2):
#   result = num1 + num2
#   return f'''
#   {num1} + {num2} = {result}  
#   ''' 
@app.route('/user/<username>')
def user(username):
  return f'<h1> name is: {username} </h1>'

@app.route('/calculator/addition/<int:num1>/<int:num2>')
def addition(a, b):
  result = a + b
  return f'<h1> {a} + {b} = {a+b} </h1>'

@app.route('/calculator/division/<int:a>/<int:b>')
def division(a, b):
  result = a - b
  return f'<h1> {a} / {b} = {a-b} </h1>'

@app.route('/calculator/multiplication/<int:a>/<int:b>')
def multiplication(a, b):
  result = a * b
  return f'<h1> {a} * {b} = {result} </h1>'

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
  result = a / b
  return f'<h1> {a} / {b} = {result} </h1>'

@app.route('/secretkey/<uuid:sk')
def My_secretkey(sk):
  return f'<h1> My secret key is: {sk} </h1>'

#if __name__ == '__main__': 
#  app.run(debug=True)