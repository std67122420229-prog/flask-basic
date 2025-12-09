from flask import Flask

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

@app.route('/calulator/addition/<int:num1>/<int:num2>')
def addition(num1, num2):
  result = num1 + num2
  return f'''
  {num1} + {num2} = {result}  
  ''' 
