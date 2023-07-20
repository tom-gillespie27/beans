from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.sampleapis.com/coffee/hot')
    drinks = response.json()
    black_coffee = next(drink for drink in drinks if drink['title'].lower() == 'black')  # assuming 'title' is the correct field name
    return render_template('index.html', drinks=drinks, black_coffee=black_coffee)

if __name__ == "__main__":
    app.run(debug=True)
