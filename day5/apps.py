# import flask
from flask import Flask
# 2 create the app
app = Flask(__name__)
# 3 Homepage  router
@app.route('/')
def home():
    return '''
<h1> python notes</h1>
<p>welcome to you study notebook server.</p>
<h2>Available Routes</h2>
<ul>
<li><a href="/test">/test</li>
</ul>
'''
# pri

@app.route('/test')
def test():
    return '''
<h1> test notes</h1>
<p>welcome to you study notebook server.</p>
'''

@app.route('/about')
def about():
    return '''
<h1> about notes</h1>
<p>welcome to you study notebook server.</p>
'''
if __name__ == '__main__':
    app.run(debug=True)
