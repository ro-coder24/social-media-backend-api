from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/message")
def message():
    return jsonify({"message": "Welcome to your Social Media Backend API!"})

@app.route("/api/posts")
def get_posts():
    return jsonify([{"id": 1, "content": "First post!"}])

if __name__ == "__main__":
    app.run(debug=True)