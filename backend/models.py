from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() #instance of ORM


#DB schemas
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    mailid=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    full_name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=True)
    phone_no=db.Column(db.String,nullable=False)
    role=db.Column(db.Integer,default=2)
    scores=db.relationship('Score',cascade='all,delete',backref='user',lazy=True)

class Subject(db.Model):
    __tablename__='subject'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=True)
    #Relationships from parent to child
    chapters=db.relationship('Chapter',cascade='all,delete',backref='subject',lazy=True)
    

class Chapter(db.Model):
    __tablename__='chapter'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=True)
    subject_id=db.Column(db.Integer,db.ForeignKey('subject.id'),nullable=False)
    quizzes=db.relationship('Quiz',cascade='all,delete',backref='chapter',lazy=True)

class Quiz(db.Model):
    __tablename__='quiz'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=True)
    chapter_id=db.Column(db.Integer,db.ForeignKey('chapter.id'),nullable=False)
    questions=db.relationship('Question',cascade='all,delete',backref='quiz',lazy=True)
    scores=db.relationship('Score',cascade='all,delete',backref='quiz',lazy=True)

class Question(db.Model):
    __tablename__='question'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=True)
    opt1=db.Column(db.String,nullable=False)
    opt2=db.Column(db.String,nullable=False)
    opt3=db.Column(db.String,nullable=False)
    opt4=db.Column(db.String,nullable=False)
    correct_opt=db.Column(db.Integer,nullable=False)
    marks=db.Column(db.Integer,nullable=False)
    quiz_id=db.Column(db.Integer,db.ForeignKey('quiz.id'),nullable=False)

class Score(db.Model):
    __tablename__='score'
    id=db.Column(db.Integer,primary_key=True)
    max_marks=db.Column(db.Integer,nullable=False)
    scored_marks=db.Column(db.Integer,nullable=False)
    time_stamp=db.Column(db.DateTime,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    quiz_id=db.Column(db.Integer,db.ForeignKey('quiz.id'),nullable=False)
    



