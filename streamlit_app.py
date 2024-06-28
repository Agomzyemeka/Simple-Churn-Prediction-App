import streamlit as st
import pandas as pd
import joblib
import os
from io import BytesIO
import xlsxwriter  # Import XlsxWriter explicitly

# Load the saved model and scaler with error handling
model_path = os.path.join(os.getcwd(), 'best_model_Random Forest.pkl')
scaler_path = os.path.join(os.getcwd(), 'scaler.pkl')

if not os.path.exists(model_path):
    st.error(f"Model file '{model_path}' not found!")
if not os.path.exists(scaler_path):
    st.error(f"Scaler file '{scaler_path}' not found!")

try:
    best_model = joblib.load(model_path)
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

try:
    scaler = joblib.load(scaler_path)
except Exception as e:
    st.error(f"Error loading scaler: {str(e)}")

# Streamlit UI
st.title('Customer Churn Prediction')

st.header('Enter customer details:')

# Check if both model and scaler were successfully loaded
if 'best_model' in locals() and 'scaler' in locals():
    # Single input prediction
    st.subheader('Single Customer Prediction')
    CreditScore = st.number_input('Credit Score', min_value=300, max_value=900, value=600)
    Geography = st.selectbox('Geography', ('France', 'Spain', 'Germany'))
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Age = st.number_input('Age', min_value=18, max_value=100, value=40)
    Tenure = st.number_input('Tenure (years)', min_value=0, max_value=10, value=5)
    Balance = st.number_input('Balance', min_value=0, value=60000)
    NumOfProducts = st.number_input('Number of Products', min_value=1, max_value=4, value=2)
    HasCrCard = st.selectbox('Has Credit Card?', ('Yes', 'No'))
    IsActiveMember = st.selectbox('Is Active Member?', ('Yes', 'No'))
    EstimatedSalary = st.number_input('Estimated Salary', min_value=0, value=50000)

    # Convert categorical inputs to numerical
    Geography_dict = {'France': 0, 'Spain': 1, 'Germany': 2}
    Gender_dict = {'Male': 0, 'Female': 1}
    HasCrCard_dict = {'No': 0, 'Yes': 1}
    IsActiveMember_dict = {'No': 0, 'Yes': 1}

    # Create a dataframe for the input
    input_data = pd.DataFrame({
        'CreditScore': [CreditScore],
        'Geography': [Geography_dict[Geography]],
        'Gender': [Gender_dict[Gender]],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts],
        'HasCrCard': [HasCrCard_dict[HasCrCard]],
        'IsActiveMember': [IsActiveMember_dict[IsActiveMember]],
        'EstimatedSalary': [EstimatedSalary]
    })

    # Standardize the input data (assuming scaler is already loaded)
    input_data_scaled = scaler.transform(input_data)

    # Predict churn
    if st.button('Predict'):
        prediction = best_model.predict(input_data_scaled)
        if prediction[0] == 1:
            st.write('The customer is likely to churn.')
        else:
            st.write('The customer is not likely to churn.')

    st.subheader('Batch Prediction')

    # File upload
    uploaded_file = st.file_uploader("📁 Choose a file (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            st.write("File successfully uploaded!")
            st.write(data.head())

            # Add a 'CustomerName' column to the DataFrame for identification
            if 'CustomerName' not in data.columns:
                st.error("The uploaded file must contain a 'CustomerName' column.")
            else:
                # Ensure the required columns are in the dataframe
                required_columns = ['CustomerName', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
                if not all(col in data.columns for col in required_columns):
                    st.error("The uploaded file must contain the following columns: " + ", ".join(required_columns))
                else:
                    # Convert categorical inputs to numerical
                    data['Geography'] = data['Geography'].map(Geography_dict)
                    data['Gender'] = data['Gender'].map(Gender_dict)
                    data['HasCrCard'] = data['HasCrCard'].map(HasCrCard_dict)
                    data['IsActiveMember'] = data['IsActiveMember'].map(IsActiveMember_dict)

                    # Standardize the input data
                    input_data_scaled = scaler.transform(data.drop(columns=['CustomerName']))

                    # Predict churn
                    predictions = best_model.predict(input_data_scaled)
                    data['Prediction'] = ['Churn' if pred == 1 else 'No Churn' for pred in predictions]

                    # Show predictions
                    st.write(data[['CustomerName', 'Prediction']])

                    # Button to download the predictions
                    def to_excel(df):
                        output = BytesIO()
                        writer = pd.ExcelWriter(output, engine='xlsxwriter')
                        df.to_excel(writer, index=False, sheet_name='Sheet1')
                        writer.save()  # Save the writer
                        processed_data = output.getvalue()
                        return processed_data

                    df_xlsx = to_excel(data[['CustomerName', 'Prediction']])
                    st.download_button(label='📥 Download Predictions', data=df_xlsx, file_name='churn_predictions.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

st.write("This app was created by Chukwuemeka Agomoh. Thanks!")
