from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/home')
def home_page():
    arr = ["Yasar", "Hamouz", "Khalil"]
    d = {
        'first_name': "Motaz",
        'last_name': "Zahdah",
        'age': 24
    }
    return render_template('home.html', isOdd=True, arr=arr, dictionary=d)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)