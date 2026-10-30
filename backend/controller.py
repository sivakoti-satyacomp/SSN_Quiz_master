from flask import render_template,request
from flask import current_app as app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def user_login():
    if request.method=="POST":
        #Get data from the form
        mailid=request.form.get("uname")
        pwd=request.form.get("password")
        #print(mailid,", ",pwd)

    return render_template("login.html")


@app.route("/signup",methods=["GET","POST"])
def user_signup():
    if request.method=="POST":
        mailid=request.form.get("uname")
        pwd=request.form.get("password")
        f_name=request.form.get("full_name")
        address=request.form.get("address")
        phone=request.form.get("phno")
        # print(f_name)

        
    return render_template("signup.html")



@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html",admin_name="IITM")

@app.route("/user")
def user_dashboard():
    return render_template("user_dashboard.html",user_name="SSN")


@app.route("/subject/add",methods=["GET","POST"])
def add_subject():
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        
    return render_template("add_subject.html")


@app.route("/chapter/add",methods=["GET","POST"])
def add_chapter():
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        
    return render_template("add_chapter.html")


@app.route("/quiz/add",methods=["GET","POST"])
def add_quiz():
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
            
    return render_template("add_quiz.html")


@app.route("/question/add",methods=["GET","POST"])
def add_question():
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        opt_1=request.form.get("opt_1")
        opt_2=request.form.get("opt_2")
        opt_3=request.form.get("opt_3")
        opt_4=request.form.get("opt_4")
        correct_choice=request.form.get("correct_choice")
        
        
    return render_template("add_question.html")


# Routes for user dashboard
@app.route("/quiz/details",methods=["GET","POST"])
def show_quiz():
    return render_template("view_quiz.html")