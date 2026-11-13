from flask import render_template, request, redirect, url_for
from flask import current_app as app
from backend.models import *


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        mailid = request.form.get("uname")
        pwd = request.form.get("password")
        # search
        user = User.query.filter_by(mailid=mailid, password=pwd).first()
        if user and user.role == 2:
            return redirect(url_for("user_dashboard", user_id=user.id))
        elif user and user.role == 1:
            # Call the function
            return redirect(url_for("admin_dashboard", user_id=user.id))

    return render_template("login.html", err_msg="Incorrect credentials")


@app.route("/signup", methods=["GET", "POST"])
def user_signup():
    if request.method == "POST":
        mailid = request.form.get("uname")
        pwd = request.form.get("password")
        f_name = request.form.get("full_name")
        address = request.form.get("address")
        phone = request.form.get("phno")
        # Add/save record
        user = User(
            mailid=mailid,
            password=pwd,
            full_name=f_name,
            address=address,
            phone_no=phone,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_login"))  # Goto the route

    return render_template("signup.html")


# Routes for admin
@app.route("/admin/<int:user_id>", methods=["GET", "POST"])
def admin_dashboard(user_id):
    user = User.query.get_or_404(user_id)  # search primary key
    subjects = Subject.query.all()
    return render_template("admin_dashboard.html", user=user, subjects=subjects)


# Add new subject
@app.route("/subject/add/<int:user_id>", methods=["GET", "POST"])
def add_subject(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        subject = Subject(title=title, description=description)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for("admin_dashboard", user_id=user.id))

    return render_template("add_subject.html", user=user)


# Edit Subject
@app.route("/subject/edit/<int:user_id>/<int:sub_id>", methods=["GET", "POST"])
def edit_subject(user_id, sub_id):
    user = User.query.get_or_404(user_id)
    subject = Subject.query.get_or_404(sub_id)
    if request.method == "POST":
        new_title = request.form.get("title")
        new_description = request.form.get("description")
        subject.title = new_title
        subject.description = new_description
        db.session.commit()
        return redirect(url_for("admin_dashboard", user_id=user.id))

    return render_template("edit_subject.html", user=user, subject=subject)


# Delete Subject
@app.route("/subject/delete/<int:user_id>/<int:sub_id>")
def delete_subject(user_id, sub_id):
    user = User.query.get_or_404(user_id)
    subject = Subject.query.get_or_404(sub_id)
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for("admin_dashboard", user_id=user.id))


# New chapter
@app.route("/chapter/add/<int:user_id>/<int:sub_id>", methods=["GET", "POST"])
def add_chapter(user_id, sub_id):
    print("Hello")
    user = User.query.get_or_404(user_id)
    subject = Subject.query.get_or_404(sub_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        chapter = Chapter(title=title, description=description, subject_id=subject.id)
        db.session.add(chapter)
        db.session.commit()
        return redirect(url_for("admin_dashboard", user_id=user.id))

    return render_template("add_chapter.html", user=user, subject=subject)


# Edit Chapter
@app.route("/chapter/edit/<int:user_id>/<int:chapter_id>", methods=["GET", "POST"])
def edit_chapter(user_id, chapter_id):
    user = User.query.get_or_404(user_id)
    chapter = Chapter.query.get_or_404(chapter_id)
    if request.method == "POST":
        new_title = request.form.get("title")
        new_description = request.form.get("description")
        chapter.title = new_title
        chapter.description = new_description
        db.session.commit()
        return redirect(url_for("admin_dashboard", user_id=user.id))

    return render_template("edit_chapter.html", user=user, chapter=chapter)


# Delete Chapter
@app.route("/chapter/delete/<int:user_id>/<int:chapter_id>")
def delete_chapter(user_id, chapter_id):
    user = User.query.get_or_404(user_id)
    chapter = Chapter.query.get_or_404(chapter_id)
    db.session.delete(chapter)
    db.session.commit()
    return redirect(url_for("admin_dashboard", user_id=user.id))


# Quiz management
@app.route("/quizzes/<int:user_id>", methods=["GET", "POST"])
def manage_quizzes(user_id):
    user = User.query.get_or_404(user_id)  # search primary key
    quizzes = Quiz.query.all()
    return render_template("quiz_management.html", user=user, quizzes=quizzes)


# Add quiz
@app.route("/quiz/add/<int:user_id>", methods=["GET", "POST"])
def add_quiz(user_id):
    chapters = Chapter.query.all()
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        chapter_id = request.form.get("chapter_id")
        quiz = Quiz(title=title, description=description, chapter_id=chapter_id)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for("manage_quizzes", user_id=user.id))

    return render_template("add_quiz.html", user=user, chapters=chapters)


@app.route("/question/add/<int:user_id>/<int:quiz_id>", methods=["GET", "POST"])
def add_question(user_id, quiz_id):
    user = User.query.get_or_404(user_id)
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        opt_1 = request.form.get("opt_1")
        opt_2 = request.form.get("opt_2")
        opt_3 = request.form.get("opt_3")
        opt_4 = request.form.get("opt_4")
        correct_choice = request.form.get("correct_choice")
        marks = request.form.get("marks")
        question = Question(
            title=title,
            description=description,
            opt1=opt_1,
            opt2=opt_2,
            opt3=opt_3,
            opt4=opt_4,
            correct_opt=int(correct_choice),
            marks=marks,
            quiz_id=quiz_id,
        )
        db.session.add(question)
        db.session.commit()

        return redirect(url_for("manage_quizzes", user_id=user.id))

    return render_template("add_question.html", user=user, quiz=quiz)


# Routes for user dashboard
@app.route("/user/<string:user_id>", methods=["GET", "POST"])
def user_dashboard(user_id):
    return render_template("user_dashboard.html", user_name=user_id)


@app.route("/quiz/details", methods=["GET", "POST"])
def show_quiz():
    return render_template("view_quiz.html")


# function
# def update_exam_status():
#     exam.status="Completed" #draft/slot creation/opened/completed
#     <query1> to get all the slots of the exams where exam_date is passed
#     Exams.relationshiop=slots
#     Exams.slots.exam_date<Date then completed
