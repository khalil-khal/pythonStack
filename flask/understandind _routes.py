from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)
@app.route("/")
def hello():
    return "hello world"

@app.route("/dojo")
def dojo():
    return "dojo"

@app.route("/say/<name>")
def say(name):
    return f"hi {name}"


@app.route("/say/<int:num>/hello")
def repeat(num):
    return f"hello " * num








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)