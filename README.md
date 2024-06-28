# Simple Churn Prediction App

<img src="assets/app_cover_image.jpg" alt="App Cover Image" width="400"/>

<a href="https://www.freepik.com/free-vector/leadership-originality-concept-run-opportunities-growing-leadership-success-leadership-businessman-opportunities-leader-worker-vector-illustration_11059462.htm#query=customer%20churn&position=39&from_view=keyword&track=ais_user&uuid=5667185d-e7d7-4e17-aef2-b2f9d2db66c3">Image by macrovector</a> on Freepik

## Overview
Welcome to the Simple Churn Prediction App! This app is designed to predict whether a customer will churn or not based on several features such as credit score, geography, gender, age, tenure, balance, number of products, credit card ownership, membership status, and estimated salary.

## Repository Structure
- **best_model_Random Forest.pkl**: This file contains the saved Random Forest model trained on the customer churn dataset.
- **scaler.pkl**: This file contains the scaler used to standardize the features before feeding them into the model.
- **requirements.txt**: This file lists all the dependencies required to run the app.
- **streamlit_app.py**: This is the main script that runs the Streamlit app.
- **assets/**: This folder contains images and other static files used in the README or the app.
- **generated_customer_data.csv**: Contains Sample batch data of customers to run Churn Prediction on using the app.

## Using the App
You can use the app to predict customer churn by inputting various customer details. The app will then use the trained model to make a prediction. Here’s how you can use it:

### Single Customer Prediction
1. **CreditScore**: Enter the customer's credit score.
2. **Geography**: Select the customer's country (France, Germany, or Spain).
3. **Gender**: Select the customer's gender (Male or Female).
4. **Age**: Enter the customer's age.
5. **Tenure**: Enter the number of years the customer has been with the bank.
6. **Balance**: Enter the customer's account balance.
7. **NumOfProducts**: Enter the number of products the customer has.
8. **HasCrCard**: Select whether the customer has a credit card (Yes or No).
9. **IsActiveMember**: Select whether the customer is an active member (Yes or No).
10. **EstimatedSalary**: Enter the customer's estimated salary.

### Batch Prediction
1. **Upload File**: Click on the 📁 icon to upload a CSV or Excel file containing multiple customer details.
2. **View Results**: The app will display the predictions for each customer in the file.
3. **Download Report**: Click on the 📥 icon to download the prediction results as an Excel report.

### Steps to Use the App
1. **Input Values**: Fill in the required fields in the app.
2. **Predict**: Click the predict button to get the prediction.
3. **View Results**: The app will display whether the customer is likely to churn or not.
   
You can access the 'generated_customer_data.csv' in the repo to run test on batch prediction
You can access the app using this link: [Simple Churn Prediction App](https://simple-churn-prediction-app.streamlit.app/).

## How the Model Works
The model uses a Random Forest classifier, which is an ensemble learning method based on constructing multiple decision trees. It considers the input features to make predictions about customer churn. The features are standardized before being fed into the model to improve performance.

## Business Applications
Businesses can use this app to:
- Predict which customers are at risk of churning.
- Develop targeted retention strategies for high-risk customers.
- Improve customer satisfaction and reduce churn rates.
- Make data-driven decisions to enhance overall business productivity.

## Feedback
We encourage you to try out the app and provide feedback. Let us know if you find it useful for your business and if there are any improvements you'd like to see.

## CODSOFT Project Repository
If you want to see my CODSOFT Task repository where the notebook used for training the Churn Prediction Model was trained, you can visit my GitHub repository [here](https://github.com/Agomzyemeka/Simple-Churn-Prediction-App).

## Contact
Feel free to reach out to me at <emyagomoh54321@gmail.com> if you have any questions or suggestions. Your feedback is highly appreciated!
