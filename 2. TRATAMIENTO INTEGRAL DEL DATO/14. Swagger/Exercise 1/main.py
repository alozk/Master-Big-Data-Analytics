from flask import Flask, redirect, url_for, render_template, request, flash
 
app = Flask(__name__,template_folder='templates')
 
app.debug = True


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return f'welcome to a POST of {user}'
   else:
      return 'welcome to a GET'
 
app.run(host='localhost', port=99)