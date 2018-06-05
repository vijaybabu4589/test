from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def mainn():
    return render_template('index.html')
    #return "hi
app.run(debug=True,host="192.168.0.101",port="80")
