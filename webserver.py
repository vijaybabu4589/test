from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def mainn():
    return render_template('index.html')
    #return "welcome"
app.run(debug=True,host="your ip ",port="80")
