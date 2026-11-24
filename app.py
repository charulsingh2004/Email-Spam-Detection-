import streamlit as st
import joblib

# Load the trained spam detection model
model = joblib.load("spam_detection_model.pkl")

st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detection System")
st.write("Enter an email message to check whether it is Spam or Ham.")

email = st.text_area("Enter your email message:")

if st.button("Check Email"):
    if email.strip():
        prediction = model.predict([email])[0]
        probabilities = model.predict_proba([email])[0]
        classes = list(model.classes_)

        confidence = probabilities[classes.index(prediction)] * 100

        if prediction == 1:
            st.error("🚨 SPAM EMAIL")
        else:
            st.success("✅ HAM (NORMAL EMAIL)")

        st.write(f"**Model Confidence:** {confidence:.2f}%")
        st.write(
            f"**HAM Probability:** "
            f"{probabilities[classes.index(0)] * 100:.2f}%"
        )
        st.write(
            f"**SPAM Probability:** "
            f"{probabilities[classes.index(1)] * 100:.2f}%"
        )
    else:
        st.warning("Please enter an email message.")