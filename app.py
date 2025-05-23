from flask import Flask, jsonify, render_template, request
import re

app = Flask(__name__)

#imports the index.html
@app.route('/')
def home():
    return render_template('index.html')

#title
@app.route("/api/message")
def message():
    return jsonify({"message": "Welcome to your Social Media Backend API!"})

#email/reg
#email validation check
def valid_email(email):
    regex = r'^[^\s@]+@[^\s@+\.[^\s@]+$'
    return re.match(regex, email) is not None
#existing email
def email_exists(email):
    #placeholder-replace with actual database check, need to test as well
    return False
#call valid email function
@app.route("/register", methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    if not valid_email(email):
        return jsonify({"message": "Invalid email format."}), 400
    if email_exists(email):
        return jsonify({"Message": "Email is already registered."}), 400

#sample post
@app.route("/api/posts")
def get_posts():
    return jsonify([{"id": 1, "content": "First post!"}])

if __name__ == "__main__":
    app.run(debug=True)