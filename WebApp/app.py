## importing flask
from flask import Flask,render_template
## Declare a Flask app
app = Flask(__name__)







## route function in Flask

## Syntax: basedomain/ ,basedomain/home ,Localhost:5000/home
## @app.route("/"),@app.route("/home")

@app.route("/home")
def main():
    return render_template('index.html')

## Add Page route
@app.route("/add")
def add():
    return render_template('add.html')

## update page route
@app.route("/update")
def update():
    return render_template('update.html')

## delete page route
@app.route("/delete")
def delete():
    return render_template('delete.html')

## Call the Flask app

if __name__ =="__main__":
  app.run()


