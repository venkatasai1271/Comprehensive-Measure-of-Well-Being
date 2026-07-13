import os
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------
# Load trained model
# -------------------------------
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


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -------------------------------
# Prediction Page
# -------------------------------
@app.route("/Prediction")
def prediction():
    return render_template("index.html")


# -------------------------------
# Home Button
# -------------------------------
@app.route("/Home")
def Home():
    return render_template("home.html")


# -------------------------------
# Predict
# -------------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Read input values
        life = float(request.form["Life expectancy"])
        school = float(request.form["Mean years of schooling"])
        gni = float(request.form["Gross national income (GNI) per capita"])
        internet = float(request.form["Internet users"])

        # Create dataframe
        df = pd.DataFrame({
            "Life expectancy": [life],
            "Mean years of schooling": [school],
            "Gross national income (GNI) per capita": [gni],
            "Internet users": [internet]
        })

        print("\nInput Data")
        print(df)

        # Prediction
        prediction = model.predict(df)

        print("Raw Prediction:", prediction)

        # Convert prediction into float
        if isinstance(prediction, (list, tuple)):
            score = float(prediction[0])
        else:
            try:
                score = float(prediction[0][0])
            except:
                score = float(prediction[0])

        score = round(score, 2)

        # HDI Category
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
            prediction_text="Error",
            score=str(e)
        )


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)