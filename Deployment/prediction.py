import streamlit as st
import pandas as pd
import numpy as np
import joblib, pickle
import json

#Load All Files

#load model dan files yang sudah di save pada framing
# with open('model_rf.pkl', 'rb') as file_1:
#     model_rf = pickle.load(file_1)
# # model_patch = 'model_rf.pkl'
# model_rf = joblib.load(model_patch)
# with open('list_num_cols.txt', 'r') as file_1:
#   list_num_cols = json.load(file_1)
# with open('list_cat_cols.txt', 'r') as file_2:
#     list_cat_cols = json.load(file_2)
with open('model_rf.pkl', 'rb') as file3:
    loaded_model = pickle.load(file3)

def run():

    with st.form('deposito_simulation'):
        #Field Umur
        Age = st.number_input('Age', min_value = 17, max_value = 75, value = 25, step = 1, help = 'Customers Age')
        #Field Nama
        Job = st.selectbox('Job', ('admin.', 'technician', 'services','management','retired','blue-collar','unemployed','entrepreneur','housemaid','unknown','self-employed','student'), index = 1)
        #Marital Status
        Marital = st.selectbox('Marital Status', ('married', 'single', 'divorced'), index = 1)
        #Education Status
        Education = st.selectbox('Education', ('secondary', 'tertiary', 'primary', 'unknown'), index = 1)
        #Default Status
        Default = st.selectbox('Default', ('no', 'yes'), index = 1, help = 'has credit in default?')
        #Field Pace Total
        Balance = st.number_input('Balance', min_value = 0, max_value=999999, value = 50)
        #Housing Status
        Housing = st.selectbox('Housing', ('yes', 'no'), index = 1, help = 'has housing loan?')
        #Loan Status
        Loan = st.selectbox('Loan', ('no', 'yes'), index = 1, help = 'has personal loan?')
        #Contact Status
        Contact = st.selectbox('Contact', ('unknown', 'cellular', 'telephone'), index = 1)
        #Day
        Day = st.number_input('Day', min_value = 1, max_value=31, value = 1, help = 'last contact day of the month')
        #Month
        Month = st.selectbox('Month', ('may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'jan', 'feb', 'mar', 'apr', 'sep'), index = 1, help = 'last contact month of year')
        #Duration
        Duration = st.number_input('Duration', min_value = 0, max_value=999999, value = 50, help = 'last contact duration, in seconds')
        #Day
        Campaign = st.number_input('Campaign', min_value = 1, max_value=100, value = 1, help = 'number of contacts performed during this campaign and for this client')
        #pDyas
        Pdays = st.number_input('Pdays', min_value = -1 , max_value=9999999, value = 0, help = 'number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted')
        #Previous
        Previous = st.number_input('Previous', min_value = 0, max_value=100, value = 0, help = 'previous: number of contacts performed before this campaign and for this client')
        #Poutcome Status
        Poutcome = st.selectbox('P Outcome', ('unknown', 'other', 'failure', 'success'), index = 1, help = 'outcome of the previous marketing campaign')


        #bikin submit button
        submitted = st.form_submit_button('Predict')

    #Inference
    data_inf = {
        'age' : Age,
        'job' : Job,
        'marital' : Marital,
        'education' : Education,
        'default' : Default,
        'balance' : Balance,
        'housing' :Housing,
        'loan': Loan,
        'contact' : Contact,
        'day' :Day,
        'month' :Month,
        'duration':Duration,
        'campaign': Campaign,
        'pdays':Pdays,
        'previous':Previous,
        'poutcome': Poutcome,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    #Logic ketika predic button ditekan

    if submitted:
        
        #predict using pipe rf model
        predictions = loaded_model.predict(data_inf)
        
        st.write('## Deposit : ', str(int(predictions)))

if __name__ == '__main__':
   run()