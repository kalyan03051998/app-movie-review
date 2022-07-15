from flask import Flask,render_template,request
from joblib import load
from textblob import TextBlob


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
   request_type_str = request.method
   if request_type_str == "GET":
    return render_template('hi.html', href='static/Base.png')
   else:
    text = request.form["text"]
    score=TextBlob(text).sentiment.polarity
    if score >= 0.1:
      return render_template('hi.html', href='static/positive.png')
    elif score <= -0.1:
      return render_template('hi.html', href='static/negative.png')
    else: 
      return render_template('hi.html', href='static/neutral.png')


if __name__ == '__main__':
   app.run(debug=True)


