from flask import Flask, render_template,request,redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/user',mehod=['post'])
def index():
    print('get post information')
    print(req)
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
