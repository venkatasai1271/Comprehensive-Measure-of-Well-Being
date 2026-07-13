# A Comprehensive Measure of Well-Being

## Overview

A Machine Learning based project that measures and predicts well-being using Human Development Index (HDI) indicators.

The system analyzes important factors such as health, education, and income to generate well-being predictions. The project includes data processing, visualization, machine learning model development, and Flask-based deployment.

---

# Technologies Used

## Development Tools

### Anaconda Navigator
A desktop graphical user interface used to manage Python environments and packages for data science projects.

Link:
https://www.anaconda.com/download

### PyCharm
An Integrated Development Environment (IDE) designed for Python development with debugging and code analysis features.

Link:
https://www.jetbrains.com/pycharm/

---

# Python Libraries

## NumPy
Used for numerical computing and handling multi-dimensional arrays.

Link:
https://numpy.org/

## Pandas
Used for data manipulation, cleaning, and analysis.

Link:
https://pandas.pydata.org/

## Scikit-learn
Machine learning library used for model training, regression, prediction, and evaluation.

Link:
https://scikit-learn.org/

## Matplotlib
Used for creating data visualizations and graphical representations.

Link:
https://matplotlib.org/

## Seaborn
Used for statistical data visualization and advanced charts.

Link:
https://seaborn.pydata.org/

## Flask
A lightweight Python web framework used to deploy the machine learning model as a web application.

Link:
https://flask.palletsprojects.com/

---

# Entity Relationship Diagram

The ER diagram represents the database structure of the Well-Being Prediction System.

GitHub Link:

https://github.com/venkatasai1271/Comprehensive-Measure-of-Well-Being/blob/main/ER_Diagram.md

---

# Project Workflow

The project is developed through a structured workflow consisting of multiple stages covering data collection, analysis, preprocessing, model development, and deployment.

---

# Epic 1: Environment Setup and Package Installation

## Stories:

- Download and install required Python packages, machine learning libraries, and Flask dependencies.

- Create and organize the project folder structure including:
  - Dataset folder
  - Model folder
  - Templates folder
  - Static files
  - Source code files

---

# Epic 2: Importing Required Libraries

## Stories:

- Import required libraries:

  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - Pickle
  - Flask

- Configure the environment for data analysis, machine learning development, and web application creation.

---

# Epic 3: Dataset Download and Understanding

## Stories:

- Download the dataset from Kaggle.

- Load the dataset into the development environment.

- Understand:
  - Dataset structure
  - Features
  - Target variable
  - Data types

- Perform data visualization to identify:
  - Patterns
  - Trends
  - Distributions
  - Relationships between variables

---

# Epic 4: Data Preprocessing and Label Encoding

## Stories:

- Select dependent and independent variables required for model training.

- Check missing values and handle null entries.

- Perform label encoding to convert categorical values into numerical format.

- Prepare the cleaned dataset for machine learning.

---

# Epic 5: Train and Test Data Division

## Stories:

- Split the processed dataset into:

  - Training data
  - Testing data

- Use training data for model learning.

- Use testing data for performance evaluation.

---

# Epic 6: Model Training and Prediction

## Stories:

- Train the Linear Regression model using the training dataset.

- Generate predictions using the trained model.

- Evaluate model performance using regression metrics.

- Analyze prediction results.

---

# Epic 7: Saving the Model

## Stories:

- Save the trained machine learning model using Pickle serialization.

- Store the model file for future prediction and deployment.

Example:

```
model.pkl
```

---

# Epic 8: Flask Web Application Development

## Stories:

- Develop Flask backend to:
  - Receive user inputs
  - Load trained model
  - Generate predictions

- Create HTML templates for user interaction.

- Connect frontend pages with Flask backend.

- Test and validate the complete application.

---

# Project Features

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Machine Learning Model Training
- Well-Being Prediction
- Flask Web Application
- Model Deployment

---

# Project Structure

```
Comprehensive-Measure-of-Well-Being

│
├── dataset/
│
├── models/
│
├── notebooks/
│
├── templates/
│
├── static/
│
├── app.py
│
├── train_model.py
│
├── requirements.txt
│
├── README.md
│
└── ER_Diagram.md
```

---

# Machine Learning Workflow

```
Dataset Collection
        |
        ↓
Data Understanding
        |
        ↓
Data Cleaning
        |
        ↓
Data Visualization
        |
        ↓
Feature Selection
        |
        ↓
Train-Test Split
        |
        ↓
Model Training
        |
        ↓
Prediction
        |
        ↓
Model Saving
        |
        ↓
Flask Deployment
```
