from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about/')
def about():
    return 'This is the about page'

@app.route('/squared/<num>')
def squared(num):
    num2 = int(num) * int(num)
    return f"Your entered number squared is: {num2}"

if __name__ == "__main__":
    app.run(debug=True)
