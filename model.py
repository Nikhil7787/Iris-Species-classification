from flask import Flask, render_template, request, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('irismodel.sav', 'rb'))


@app.route('/')
def home():
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Sepal_length = float(request.form['Sepal_length'])
    Sepal_width = float(request.form['Sepal_width'])
    Petal_length = float(request.form['Petal_length'])
    Petal_width = float(request.form['Petal_width'])
    result = model.predict([[Sepal_length, Sepal_width, Petal_length, Petal_width]])[0]
    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run(debug=True)