import numpy as np
import pickle
import streamlit as st
import pandas as pd


# loading the saved model
loaded_model = pickle.load(open('Model.pkl','rb'))


# creating a function for Prediction

def co2_prediction(input_data,c,t):
    user_input = pd.DataFrame([[input_data,c,t]], columns=['Base location', 'Destination', 'Mode of transport'])
    predicted_co2 = loaded_model.predict(user_input)
    print("Predicted CO2 Emission (in Kg):", predicted_co2[0])
    return np.round(predicted_co2[0],2)
	  
		
	  
def main():
    
    
    # giving a title
    st.title('Co2 Emission Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Base_location = st.text_input('Base Location')
    Destination = st.text_input('Destination Location')
    Mode_of_transport = st.text_input('Mode of Transport')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Co2 (kg) Prediction Result'):
        diagnosis = co2_prediction(Base_location, Destination, Mode_of_transport)
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    