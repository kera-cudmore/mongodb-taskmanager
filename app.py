"""
Import OS, Flask, Pymongo, ObjectId, generate password hash & check password hash
"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    """
    finds tasks in the db and renders the Tasks page(home page)
    """
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    register page
    """
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username is in use, flash message & redirect to register page
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # if no existing username - gather info from form to be added to db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Calls the users collection on MongoDB &
        # inserts the register variable dictionary
        mongo.db.users.insert_one(register)

        # Put the new user into the 'session'
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login functionality
    """
    if request.method == "POST":
        # check to see if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # invalid password match - By using and/or incorrect
                #  - makes harded to brute force an account
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist - By using and/or incorrect
            #  - makes harded to brute force an account
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    
    # the get statement acts as the else in the above condition
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Profile page for user - pass username as function argument
    grabs the session user's username from the database
    if session is truthy - return appropriate profile template
    if not true or doesn't exist return user to login template
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #remove user from session cookies - removes the user session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task")
def add_task():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)


# IMPORTANT! debug should be set to false before deployment & submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
