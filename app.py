import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings("ignore", message="`label` got an empty value", category=UserWarning)

# Load the model

with open('final_model.sav', 'rb') as file:
    load_model = pickle.load(file)
rockimage_path = 'data/rock.png'
st.sidebar.image(rockimage_path, use_column_width=True)

selected_page = st.sidebar.radio("", ["Home", "About Us", "Contact Us"])
if selected_page == "Home":
    st.balloons()
    st.markdown("""
    <style>
    .block-container {
    padding-top: 3rem;
    text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    image = 'https://i.pinimg.com/564x/e2/c3/de/e2c3de471b7a387883c66ae9b8efff98.jpg'  # Replace with your image URL
    st.image(image, width=None, use_column_width=True)

    # Function for detecting fake news
    def detecting_fake_news(var):
        prediction = load_model.predict([var])
        prob = load_model.predict_proba([var])
        return prediction[0], prob[0][1]

    # Streamlit app

    # User input
    var = st.text_area('Enter the news text you want to verify:')
    if st.button('Verify News'):
        if var:
            st.write(f'You entered: {var}')

            # Run prediction
            prediction, probability = detecting_fake_news(var)

            # Display results
            st.write(f'The given statement is: {prediction}')

elif selected_page == "About Us":
    st.snow()
    st.title("Squad ")
    st.markdown("""
    The team which built the model🥂 
    """)
    # Add the image below the title "Team"
    team_image_path = "data/TEAM.png"  # Replace with your actual image path
    st.image(team_image_path, use_column_width=True)

elif selected_page == "Contact Us":
    st.title("Contact Us")
    st.write("Please fill out the form below to get in touch with us.")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")
        if submit:
            st.write(f"Thank you, {name}! We will get back to you at {email} as soon as possible.")
