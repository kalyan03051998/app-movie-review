from flask import Flask,render_template,request
from joblib import load



app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
   request_type_str = request.method
   if request_type_str == "GET":
    return render_template('hi.html', href='static/Base.png')
   else:
    text = request.form["text"]
    model = load('app/model.joblib')
    vector= load('app/vector.joblib')
    pred= model.predict(vector.transform([text]))[0]
    if pred == 0:
      return render_template('hi.html', href='static/negative.png')
    else:
      return render_template('hi.html', href='static/positive.png')


if __name__ == '__main__':
   app.run(debug=True)


