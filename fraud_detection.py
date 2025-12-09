import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('fraud_detection_model.pkl')

st.title('Fraud Detection Model')

st.markdown("Please input the transaction details below to predict whether it is fraudulent or not.")
st.divider()

# User Inputs
transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT', 'CASH_IN'])
amount = st.number_input('Transaction Amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input('Old Balance of Origin Account', min_value=0.0, value=9000.0)
newbalanceOrig = st.number_input('New Balance of Origin Account', min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input('Old Balance of Destination Account', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('New Balance of Destination Account', min_value=0.0, value=0.0)

# Prediction Button
if st.button('Predict Fraud'):

    # Create input dataframe
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Output
    st.subheader(f'Prediction Result: {int(prediction)}')

    if prediction == 1:
        st.error('The transaction is predicted to be **FRAUDULENT**.')
    else:
        st.success('The transaction is predicted to be **LEGITIMATE**.')