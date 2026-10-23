from flask import Flask,render_template


app=Flask("__name__")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html",admin_name="IITM")

@app.route("/user")
def user_dashboard():
    return render_template("user_dashboard.html",user_name="SSN")


#main code
app.run(debug=True)
