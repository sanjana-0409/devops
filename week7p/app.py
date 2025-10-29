from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/') 
def index():
    return render_template('myform.html')
@app.route('/submit',methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    return render_template('greetings.html',name=username,mail=email)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)