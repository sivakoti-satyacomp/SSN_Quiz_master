from flask import Flask
from backend.models import *

app=None

def initial_setup():
    app=Flask(__name__)
    # database setup
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///quiz_data.sqlite3"
    db.init_app(app) #db is connected to app
    app.app_context().push()
    print("Quiz Master app started...")
    return app


app=initial_setup() # call the above function

from backend.controller import *

if __name__=="__main__":
    app.run(debug=True)
