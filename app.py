import pathlib
import textwrap
import streamlit as st
import google.generativeai as genai
import PIL.Image

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Configure Google Generative AI with your API key
genai.configure(api_key="AIzaSyDAFriK-ovTVZC2Qp7Brq__8ETWzevZ2oo")

# Load the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# File upload for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    if st.button('Generate Content'):
        # Generate content using Generative AI
        response = model.generate_content(["Do visual text segmentation and extract text in organized form", img], stream=True)
        response.resolve()

        # Display the result in markdown format
        st.markdown(to_markdown(response.text))
