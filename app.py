from flask import Flask,render_template

app=None

def initial_setup():
    app=Flask(__name__)
    app.app_context().push()
    # database setup
    # API setup(optional)
    print("Quiz Master app started...")
    return app


app=initial_setup() # call the above function

from backend.controller import *

if __name__=="__main__":
    app.run(debug=True)
