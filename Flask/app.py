import os
import pickle
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)


# --------------------------------
# Load trained model
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "HDI.pkl")


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


print("=" * 50)
print("Model Loaded Successfully")
print("Model Path:", MODEL_PATH)

if hasattr(model, "feature_names_in_"):
    print("Features:", model.feature_names_in_)
    print("Total Features:", len(model.feature_names_in_))

print("=" * 50)



# --------------------------------
# Home Page
# --------------------------------

@app.route("/")
def home():
    return render_template("home.html")



# --------------------------------
# Prediction Input Page
# --------------------------------

@app.route("/Prediction")
def prediction():
    return render_template("index.html")



# --------------------------------
# Home Button
# --------------------------------

@app.route("/Home")
def Home():
    return render_template("home.html")



# --------------------------------
# Prediction Logic
# --------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Getting values from HTML form

        life = float(request.form["Life expectancy"])

        school = float(request.form["Mean years of schooling"])

        gni = float(
            request.form["Gross national income (GNI) per capita"]
        )

        internet = float(
            request.form["Internet users"]
        )


        # Creating dataframe for model

        input_data = pd.DataFrame({

            "Life expectancy": [life],

            "Mean years of schooling": [school],

            "Gross national income (GNI) per capita": [gni],

            "Internet users": [internet]

        })


        print("\nInput Data:")
        print(input_data)



        # Model Prediction

        prediction = model.predict(input_data)


        print("Raw Prediction:", prediction)



        # Convert prediction to float

        score = float(prediction[0])

        score = round(score, 2)



        # HDI Classification

        if score >= 0.80:

            result = "Very High HDI"


        elif score >= 0.70:

            result = "High HDI"


        elif score >= 0.55:

            result = "Medium HDI"


        else:

            result = "Low HDI"



        return render_template(

            "resultnew.html",

            prediction_text=result,

            score=score

        )


    except Exception as e:


        print("ERROR:", e)


        return render_template(

            "resultnew.html",

            prediction_text="Prediction Error",

            score=e

        )




# --------------------------------
# Run Flask Application
# --------------------------------

if __name__ == "__main__":

    app.run(debug=True)