from flask import Flask, render_template, request
from flask import app
import random
import string

from datetime import datetime

app = Flask(__name__)

def random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        params = {}

        username = request.form['username']
        ran_id = random_id()
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(username, ran_id, dt)

        params = {'username': username, 'id': ran_id, 'dt': dt}

        return render_template('result.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)
