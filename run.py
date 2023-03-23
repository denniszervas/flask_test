from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key='d30056aabc35f5236dc6185a0d3ca92f'


@app.route('/')
def index():
    print("### Index Route start ###")
    return render_template('/index.html')

@app.route('/test')
def test():
    print("### Test Route start ###")
    return render_template('/test.html')
