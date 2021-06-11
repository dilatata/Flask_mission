from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__)


@app.route('/')
def hello():
    
    return render_template('mission_request.html')


@app.route('/signup', methods=['post'])
def signup():
    id = request.form.get('id')
    
    info = {"name":"주영", "age": 26}
    return render_template('mission_response.html', new_id = id, userinfo = info)




if __name__ == '__main__':
    app.run(debug=True)


