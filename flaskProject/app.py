from flask import Flask,render_template,url_for,request
import pickle
# import joblib

app = Flask(__name__)

# model = pickle.load(open('./model/finalized_model.pkl', 'rb'))
model = pickle.load(open('./model/finalized_model2.pkl', 'rb'))
# model = joblib.load(open('./model/finalized_model.sav', 'rb'))

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        Gender = int(request.form.get('Gender'))
        Marital_Status = int(request.form.get('Marital_Status'))
        Dependents = int(request.form.get('Dependents'))
        Education = int(request.form.get('Education'))
        Self_Employed = int(request.form.get('Self_Employed'))
        ApplicantIncome = float(request.form.get('ApplicantIncome'))
        CoapplicantIncome = float(request.form.get('CoapplicantIncome'))
        LoanAmount = float(request.form.get('LoanAmount'))
        Loan_Amount_Term = float(request.form.get('Loan_Amount_Term'))
        Credit_History = float(request.form.get('Credit_History'))
        Property_Area = int(request.form.get('Property_Area'))

        features = [[Gender, Marital_Status, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]]

        print(features)

        prediction = model.predict(features)
        lc = [str(i) for i in prediction]

        prediction = int("".join(lc))
        print(prediction)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
