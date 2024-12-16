import streamlit as st
import numpy as np
import pickle


try:
    loaded_model = pickle.load(open('classifier.pkl', 'rb'))
except FileNotFoundError:
    st.error('Model file not found. Please ensure "classifier.pkl" exists in the project directory.')
    st.stop()

# Prediction function
def banknote_predict(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return 'The Note is Authentic' if prediction[0] == 0 else 'The Note is Fake'

# App layout
st.title('💵 Banknote Authentication Web App')
st.markdown('This application predicts whether a banknote is **authentic** or **fake** based on given features.')

st.divider()
with st.expander('Project Features'):
    st.write('*This project analyzes the following features of banknotes:*')
    st.caption('1. Variance')
    st.caption('2. Skewness')
    st.caption('3. Curtosis')
    st.caption('4. Entropy')

# Main logic
def main():
    st.subheader('Enter the Features of the Banknote')
    
    #  input fields
    variance = st.text_input('Enter the value of Variance')
    skewness = st.text_input('Enter the value of Skewness')
    curtosis = st.text_input('Enter the value of Curtosis')
    entropy = st.text_input('Enter the value of Entropy')

    prediction = ''  

    if st.button('Predict The Result'):
        if not (variance and skewness and curtosis and entropy):
            st.warning('Please fill in all the input fields.')
        else:
            try:
                # Convert inputs to float
                input_features = [float(variance), float(skewness), float(curtosis), float(entropy)]
                prediction = banknote_predict(input_features)
                if prediction == 'The Note is Authentic':
                    st.success('✔️ The Note is Authentic')
                else:
                    st.error('❌ The Note is Fake')
            except ValueError:
                st.error('Please enter valid numeric values for all features.')

    st.divider()
    st.subheader('Made with 💌 by Tanmay Shukla')

if __name__ == '__main__':
    main()
