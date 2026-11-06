from flask import render_template,request,redirect,url_for
from flask import current_app as app
from backend.models import *

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def user_login():
    if request.method=="POST":
        mailid=request.form.get("uname")
        pwd=request.form.get("password")
        #search
        user=User.query.filter_by(mailid=mailid,password=pwd).first()
        if user and user.role==2:
            return redirect(url_for('user_dashboard',user_id=user.id))
        elif user and user.role==1:
            return redirect(url_for('admin_dashboard',user_id=user.id))
        
    return render_template("login.html",err_msg='Incorrect credentials')


@app.route("/signup",methods=["GET","POST"])
def user_signup():
    if request.method=="POST":
        mailid=request.form.get("uname")
        pwd=request.form.get("password")
        f_name=request.form.get("full_name")
        address=request.form.get("address")
        phone=request.form.get("phno")
        #Add/save record
        user=User(mailid=mailid,password=pwd,full_name=f_name,address=address,phone_no=phone)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_login')) #Goto the route

        
    return render_template("signup.html")


# Routes for admin
@app.route("/admin/<int:user_id>",methods=["GET","POST"])
def admin_dashboard(user_id):
    user=User.query.get_or_404(user_id) #search primary key
    subjects=Subject.query.all()
    return render_template("admin_dashboard.html",user=user,subjects=subjects)


@app.route("/subject/add/<int:user_id>",methods=["GET","POST"])
def add_subject(user_id):
    user=User.query.get_or_404(user_id)
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        subject=Subject(title=title,description=description)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('admin_dashboard',user_id=user.id))
        
    return render_template("add_subject.html",user=user)


@app.route("/chapter/add/<int:user_id>/<int:sub_id>",methods=["GET","POST"])
def add_chapter(user_id,sub_id):
    user=User.query.get_or_404(user_id)
    subject=Subject.query.get_or_404(sub_id)
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        chapter=Chapter(title=title,description=description,subject_id=sub_id)
        db.session.add(chapter)
        db.session.commit()
        return redirect(url_for('admin_dashboard',user_id=user.id))

        
    return render_template("add_chapter.html",user=user,subject=subject)


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
@app.route("/user/<string:user_id>",methods=["GET","POST"])
def user_dashboard(user_id):
    return render_template("user_dashboard.html",user_name=user_id)


@app.route("/quiz/details",methods=["GET","POST"])
def show_quiz():
    return render_template("view_quiz.html")